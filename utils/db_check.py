# utils/db_check.py
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
import sys
import time
from typing import Tuple, Optional


def test_database_connection(engine, max_retries: int = 3, retry_delay: int = 5) -> Tuple[bool, Optional[str]]:
    """
    Test the database connection with retry mechanism.

    Args:
        engine: SQLAlchemy engine instance
        max_retries: Maximum number of connection attempts
        retry_delay: Delay between retries in seconds

    Returns:
        Tuple[bool, Optional[str]]: (Success status, Error message if any)
    """
    retry_count = 0

    while retry_count < max_retries:
        try:
            # Create a connection
            with engine.connect() as connection:
                # Execute a simple query
                result = connection.execute(text("SELECT 1"))
                result.close()

                # Test if we can actually query any table
                connection.execute(text("SHOW TABLES"))

                return True, None

        except SQLAlchemyError as e:
            retry_count += 1
            error_msg = str(e)

            if retry_count < max_retries:
                print(f"Connection attempt {retry_count} failed. Retrying in {retry_delay} seconds...")
                time.sleep(retry_delay)
            else:
                detailed_error = f"""
Database connection failed after {max_retries} attempts.
Error: {error_msg}
Please check:
1. Database server is running
2. Credentials are correct
3. Database exists
4. Network connectivity to database server
5. Firewall settings
"""
                return False, detailed_error

        except Exception as e:
            return False, f"Unexpected error: {str(e)}"

    return False, "Maximum retry attempts reached"


def initialize_database() -> bool:
    """
    Initialize database connection and perform connectivity test.
    Returns: bool indicating success/failure
    """
    try:
        # Import here to avoid circular imports
        from config.database import engine

        # Test the connection
        success, error_message = test_database_connection(engine)

        if success:
            print("✓ Database connection successful!")

            # Get and display some basic database information
            with engine.connect() as conn:
                # Get database version
                result = conn.execute(text("SELECT VERSION()"))
                version = result.scalar()

                # Get character set
                result = conn.execute(text("SELECT @@character_set_database"))
                charset = result.scalar()

                print(f"\nDatabase Information:")
                print(f"- Version: {version}")
                print(f"- Character Set: {charset}")
                print(f"- Connected to: {engine.url.database}")

            return True

        else:
            print("\n❌ Database connection failed!")
            print(error_message)
            return False

    except Exception as e:
        print(f"\n❌ Error during database initialization: {str(e)}")
        return False


if __name__ == "__main__":
    # This allows running this module directly to test database connectivity
    success = initialize_database()
    sys.exit(0 if success else 1)