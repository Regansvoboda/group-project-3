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
        self.start()


    def start(self):
        exit = False
        while exit == False:
            print(' ')
            print('Welcome to the Hospital Database!')
            user_input = input("Press A to view Patients, B for Doctors, C for Units or X to Exit:")
            print(' ')
            if user_input =="A" or user_input == "a":
            # def print_grapes(patients):
                print(' ')
                print('** Patients **')
                print(' ')
                
                
                for index, patient in enumerate(self.patients):
                    print(f'{index + 1}. first: {patient.first_name} last: {patient.last_name}')
            
            elif user_input =="B" or user_input == "b":
            

                print(' ')
                print('** Doctors **')
                print(' ')
                
                
                for index, doctor in enumerate(self.doctors):
                    print(f'{index + 1}. first: {doctor.first_name} last: {doctor.last_name}')

            elif user_input =="C" or user_input == "c":

                print(' ')
                print('** Units **')
                print(' ')
                
                for index, unit in enumerate(self.units):
                    print(f'{index + 1}. name: {unit.name} location: {unit.location}')

            user_input = input("Would you like to see Visits? Y/n")
            if user_input =="Y" or user_input == "y":
                # exit = True
                print(' ')
                print('** Visits **')
                print(' ')
                for index, visit in enumerate(self.visits):
                    print(f'{index + 1}. Patient ID: {visit.patient_id} Doctor ID: {visit.doctor_id} Status: {visit.status}')
            elif user_input == "N" or user_input == "n":
                exit = True
if __name__ == '__main__':
    engine = create_engine('sqlite:///db/hospital.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    CLI()
    
    