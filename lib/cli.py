from models import Patient, Doctor, Unit, Visit
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

# from helpers import (
#     function_1, function_2,
#     function_3, function_4,
#     function_5, function_6,
#     function_7, function_8,
#     function_9, function_10
# )

def print_welcome_message():
    os.system('clear')
    print(' ')
    print("    _   _      _ _ ")
    print("   | | | | ___| | | ___ ")
    print("   | |_| |/ _ \ | |/ _ \ ")
    print("   |  _  |  __/ | | (_) |")
    print("   |_| |_|\___|_|_|\___/ ")
    print(' ')
    print(' Welcome to the Hospital Database!')

def print_main_menu():
    print(' ')
    print('    MAIN MENU   ')
    print('-----------------')
    print(' ')
    print('( x to exit, / to clear screen) ')
    print(' ')
    print(' A. View Patients')
    print(' B. View Doctors')
    print(' C. View Units')
    print(' D. View Visits')
    print('-----------------')
    print(' ')
    
def print_patient(patient):
        print(' ')
        print(f'Name: {patient.first_name} {patient.last_name}')
        print(' ')

def print_patients(patients):
        print(' ')
        print('** Patients **')
        print(' ')
        for index, patient in enumerate(patients):
            print(f'{index + 1}. {patient.first_name} {patient.last_name}')
        print(' ')
            
def print_doctor(doctor):
    print(' ')
    print(f'Name: {doctor.first_name} {doctor.last_name}')
    print(' ')
    
def print_doctors(doctors):
    print(' ')
    print('** Doctors **')
    print(' ')
    for index, doctor in enumerate(doctors):
        print(f'{index + 1}. {doctor.first_name} {doctor.last_name}')
    
def print_unit(unit):
    print(' ')
    print(f'Unit Name: {unit.name}  Location: {unit.location}')
    print(' ')
    
def print_units(units):
    print(' ')
    print('** Units **')
    print(' ')
    for index, unit in enumerate(units):
        print(f'{index + 1}. Unit Name: {unit.name}  Location: {unit.location}')

def print_visit(visit):
    print(' ')
    print(f'Patient ID: {visit.patient_id} Doctor ID: {visit.doctor_id} Unit ID: {visit.unit_id} Status: {visit.status}')
    print(' ')
    
def print_visits(visits):
    print(' ')
    print('** Visits **')
    print(' ')
    for index, visit in enumerate(visits):
        print(f'{index + 1}. Patient ID: {visit.patient_id} Doctor ID: {visit.doctor_id} Unit ID: {visit.unit_id} Status: {visit.status}')
        
class CLI:
    def __init__(self):
        self.patients = [patient for patient in session.query(Patient)]
        self.doctors = [doctor for doctor in session.query(Doctor)]
        self.units = [unit for unit in session.query(Unit)]
        self.visits = [visit for visit in session.query(Visit)]
        self.start()
    
    def start(self):
        patient_ids = [patient.id for patient in self.patients]
        patient_names = [patient.first_name for patient in self.patients]
        doctor_ids = [doctor.id for doctor in self.doctors]
        doctor_names = [doctor.last_name for doctor in self.doctors]
        unit_ids = [unit.id for unit in self.units]
        unit_names = [unit.name for unit in self.units]
        p_id_visit = [visit.patient_id for visit in self.visits]
        
        exit = False
        print_welcome_message()
        while exit == False:
            print_main_menu()
            user_input = input("Select Option: ")
            
            if user_input =="A" or user_input == "a":
                print_patients(self.patients)
                user_input = input("Select Patient (M for Main, x to Exit): ")
                print(' ')
                if (user_input == "m") or (user_input == "M"):
                    os.system('clear')
                    
                elif (int(user_input) in patient_ids) and (int(user_input) in p_id_visit):    
                    for visit in self.visits:
                        if visit.patient_id == int(user_input):
                            print(f"{(patient_names[int(user_input)-1])} is seeing Dr. {doctor_names[visit.doctor_id - 1 ]} in the {unit_names[visit.unit_id - 1]} unit and is {visit.status}")
                
            elif user_input =="B" or user_input == "b":
                print_doctors(self.doctors)

            elif user_input =="C" or user_input == "c":
                print_units(self.units)

            elif user_input =="D" or user_input == "d":
                print_visits(self.visits)
            
            elif user_input =="/":
                os.system('clear')
                    
            elif user_input =="X" or user_input == "x":
                exit = True

if __name__ == '__main__':
    engine = create_engine('sqlite:///hospital.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    CLI()