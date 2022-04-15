#Even though forerunner is 'just' the database, it shall at the minimum verify its integrity though an automated script
# Task 1 - run and ensure that the sqlite db is created and the table is created
from src.Controller.AppFR_Deamon import AppFR_Deamon
from src.Controller.WebAppFR_Engine import WebAppFR_Engine


def main():
    print("Welcome to Forerunner Database Management engine")
    obj_app = AppFR_Deamon()
    obj_app.load()
    obj_app.start()

    obj_webApp = WebAppFR_Engine()
    obj_webApp.load()
    obj_webApp.main()


if __name__ == '__main__':
    main()
