from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import datetime


def main():
    calculate_salary()
    print(datetime.now())
    get_employees()
    print(datetime.now())
if __name__ == '__main__':
    main()
    

    
