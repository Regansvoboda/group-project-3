from db.models import Patient, Doctor, Unit, Visit
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# from helpers import (
#     function_1, function_2,
#     function_3, function_4,
#     function_5, function_6,
#     function_7, function_8,
#     function_9, function_10
# )


class CLI:
    def __init__(self):
        self.patients = [patient for patient in session.query(Patient)]
        self.doctors = [doctor for doctor in session.query(Doctor)]
        self.units = [unit for unit in session.query(Unit)]
        self.visits = [visit for visit in session.query(Visit)]

        print(' ')
        print('Welcome to the Hospital Database!')
        print(' ')

        exit = False
        while exit == False:
            print('Name: ' + self.patients[0].first_name + ' ' + self.patients[0].last_name)
            print('Attending Physician: ' + self.doctors[0].first_name + ' ' + self.doctors[0].last_name)
            print('Unit: ' + self.units[1].name)
            print('Status: ' + self.visits[0].status)
            print(' ')
            print('Name: ' + self.patients[1].first_name + ' ' + self.patients[1].last_name)
            print('Attending Physician: ' + self.doctors[1].first_name + ' ' + self.doctors[1].last_name)
            print('Unit: ' + self.units[0].name)
            print('Status: ' + self.visits[2].status)
            print(' ')
            print('Name: ' + self.patients[2].first_name + ' ' + self.patients[2].last_name)
            print('Attending Physician: ' + self.doctors[2].first_name + ' ' + self.doctors[2].last_name)
            print('Unit: ' + self.units[0].name)
            print('Status: ' + self.visits[2].status)
            print(' ')
            user_input = input("Would you like to exit now? (Type y/n): ")
            print(' ')
            if user_input == "y" or user_input == 'T':
                exit = True
            else:
                print("OK, let's keep going!")
                print(' ')

if __name__ == '__main__':
    engine = create_engine('sqlite:///db/hospital.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    CLI()
    
    