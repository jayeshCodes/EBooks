# main.py
from utils.db_check import initialize_database
import sys


def main():
    """
    Main application entry point
    """
    print("Initializing E-Textbook Platform...")
    print("\nChecking database connection...")

    # Check database connection
    if not initialize_database():
        print("\nFatal Error: Could not establish database connection. Exiting...")
        sys.exit(1)

    print("\nStarting application...")
    # Your application logic here
    # start_application()


if __name__ == "__main__":
    main()