from config.database import get_db
from application import Application

def main():
    print("Initializing E-Textbook Platform...")

    print("Starting application...")
    app = Application(get_db)
    app.run()

if __name__ == '__main__':
    main()