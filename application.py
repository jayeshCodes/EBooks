from config.database import get_db
from sqlalchemy.orm import Session
from models.user import User
from views import main_menu_view, admin_view, faculty_view, ta_view, student_view

class PersonService:
    def __init__(self, db: Session):
        self.db = db

    def get_person_by_username(self, username: str):
        return self.db.query(User).filter(User.email == username).first()

class Application:
    def __init__(self, db_session_factory):
        self.db_session_factory = db_session_factory

    def run(self):
        while True:
            choice = main_menu_view.display_main_menu()
            if choice == '5':
                print("Exiting the application. Goodbye!")
                break
            elif choice in ('1', '2', '3', '4'):
                self.login(choice)
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")

    def login(self, user_type):
        username = input("Enter username: ")
        password = input("Enter password: ")

        with self.db_session_factory() as db:
            person_service = PersonService(db)
            user = person_service.get_person_by_username(username)

            if user and user.password == password:
                if user_type == '1' and user.role == 'Admin':
                    admin_view.admin_home()
                elif user_type == '2' and user.role == 'Faculty':
                    faculty_view.faculty_home()
                elif user_type == '3' and user.role == 'Teaching Assistant':
                    ta_view.ta_home()
                elif user_type == '4' and user.role == 'Student':
                    student_view.student_home()
                else:
                    print("Invalid role for this user. Please try again.")
            else:
                print("Invalid credentials. Please try again.")