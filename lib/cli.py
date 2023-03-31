from models import Patient, Doctor, Unit, Visit
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
import cursor
import curses

from helpers import car_animation, car_crash_animation, loading, print_goodbye

def print_welcome_message():
    os.system('clear')
    cursor.hide()
    loading()
    car_animation(0.075)
    car_crash_animation(0.075)
    print("    _   _      _ _ ")
    print("   | | | | ___| | | ___ ")
    print("   | |_| |/ _ \ | |/ _ \ ")
    print("   |  _  |  __/ | | (_) |")
    print("   |_| |_|\___|_|_|\___/ ")
    print(' ')
    print(' Welcome to the Hospital!')
    cursor.show()

def print_main_menu():
    print(' ')
    print(' ------------------')
    print(' |    MAIN MENU   |')
    print(' ------------------')
    print(' ')
    print(' (x to Exit) ')
    print(' ')
    print(' A. View Patients')
    print(' B. View Doctors')
    print(' C. View Units')
    print(' D. View Visits')
    print(' ------------------')
    print(' ')
    
def print_patient_menu(patients):
    os.system('clear')
    print(' ')
    print('--------------------')
    print('|   PATIENT MENU   |')
    print('--------------------')
    print(' ')
    print('(x to Exit, m for Main Menu) ')
    print_patients(patients)
    print('--------------------')
    print(' ')

def print_doctor_menu(doctors):
    os.system('clear')
    print(' ')
    print('--------------------')
    print('|    DOCTOR MENU   |')
    print('--------------------')
    print(' ')
    print('(x to Exit, m for Main Menu) ')
    print_doctors(doctors)
    print('-------------------')
    print(' ')

def print_unit_menu(units):
    os.system('clear')
    print(' ')
    print('------------------')
    print('|   UNIT MENU    |')
    print('------------------')
    print(' ')
    print('(x to Exit, m for Main Menu) ')
    print_units(units)
    print('-------------------------------')
    print(' ')
    
def print_patient(patient):
        print(' ')
        print(f'Name: {patient.first_name} {patient.last_name}')
        print(' ')

def print_patients(patients):
        print(' ')
        print('***** Patients *****')
        print('--------------------')
        for index, patient in enumerate(patients):
            print(f'{index + 1}. {patient.first_name} {patient.last_name}')
            
def print_doctor(doctor):
    print(' ')
    print(f'Name: {doctor.first_name} {doctor.last_name}')
    print(' ')
    
def print_doctors(doctors):
    print(' ')
    print('***** Doctors *****')
    print('-------------------')
    for index, doctor in enumerate(doctors):
        print(f'{index + 1}. {doctor.first_name} {doctor.last_name}')
    
def print_unit(unit):
    print(' ')
    print(f'Unit Name: {unit.name}  Location: {unit.location}')
    print(' ')
    
def print_units(units):
    print(' ')
    print('      ***** Units *****')
    print('-------------------------------')
    for index, unit in enumerate(units):
        print(f'{index + 1}. {unit.name}  Location: {unit.location}')

def print_visit(visit, patients, doctors):
    print(f"{patients[visit.patient_id - 1].first_name} is with Dr. {doctors[visit.doctor_id -1].last_name}. Patient Status: {visit.status}.")
    # print(' ')
    # print(f'Patient ID: {visit.patient_id} Doctor ID: {visit.doctor_id} Unit ID: {visit.unit_id} Status: {visit.status}')
    # print(' ')
    
def print_visits(visits, patients, doctors, units):
    print(' ')
    print('                    ***** Curent Visits ******')
    print('---------------------------------------------------------------------')
    for index, visit in enumerate(visits):
        print(f"{patients[visit.patient_id -1].first_name} is with Dr. {doctors[visit.doctor_id -1].last_name} in the {units[visit.unit_id-1].name} unit. {patients[visit.patient_id -1].first_name} is {visit.status}.")
    print('---------------------------------------------------------------------')
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
            user_input = input(" Select Option: ")
            
            if user_input.lower() == "a":
                print_patients(self.patients)
                print_patient_menu(self.patients)
                print(' ')
                print(' ')

                user_input = input("Select Patient (m for Main Menu, x to exit): ")
                print(' ')
                exit_patient = False
                while exit_patient == False:
                    if user_input.lower() == "m":
                        os.system('clear')
                        exit_patient = True
                    elif user_input.lower() == "x":
                        return
                    else:
                        try:
                            patient_id = int(user_input)
                        except ValueError:
                            print('Invalid input. Please enter a valid patient ID or option.\n')
                            user_input = input("Select Patient (m for Main Menu, x to exit): ")

                        if patient_id not in patient_ids:
                            print(' ')
                            print('Invalid Patient ID')
                            print(' ')
                            user_input = input("Select Patient (m for Main Menu, x to exit): ")
                        else:
                            os.system('clear')
                            print_patient_menu(self.patients)
                            for visit in self.visits:
                                if visit.patient_id == patient_id:
                                    print(f"{(patient_names[patient_id - 1])} is seeing Dr. {doctor_names[visit.doctor_id - 1 ]} in the {unit_names[visit.unit_id - 1]} unit and is {visit.status}")
                            print(' ')
                            user_input = input("Select Patient (m for Main Menu, x to exit): ")
                    
            elif user_input =="B" or user_input == "b":
                print_doctors(self.doctors)
                print_doctor_menu(self.doctors)
                print(' ')
                print(' ')

                user_input = input("Select Doctor (m for Main Menu, x to exit): ")
                print(' ')
                exit_doctor= False
                while exit_doctor == False:
                    if user_input.lower() == "m":
                        os.system('clear')
                        exit_doctor = True
                    elif user_input.lower() == "x":
                        return
                    else:
                        try:
                            doctor_id = int(user_input)
                        except ValueError:
                            print('Invalid input. Please enter a valid option.\n')
                            user_input = input("Select Doctor (m for Main Menu, x to exit): ")

                        if doctor_id not in doctor_ids:
                            print(' ')
                            print('Invalid Doctor ID')
                            print(' ')
                            user_input = input("Select Doctor (m for Main Menu, x to exit): ")
                        else:
                            os.system('clear')
                            print_doctor_menu(self.doctors)
                            for visit in self.visits:
                                if (int(user_input) in doctor_ids):
                                    if visit.doctor_id == int(user_input):
                                        print(f"Dr. {doctor_names[visit.doctor_id-1]} is seeing {patient_names[visit.patient_id -1 ]} in the {unit_names[visit.unit_id-1]} unit. {patient_names[visit.patient_id -1 ]} is {visit.status}.")
                            print(' ')
                            user_input = input("Select Doctor (m for Main Menu, x to exit): ")
                        
            elif user_input =="C" or user_input == "c":
                print_units(self.units)
                print_unit_menu(self.units)
                print(' ')
                print(' ')
                print(' ')
                user_input = input("Select Unit to see active visits (m for Main Menu, x to exit): ")
                print(' ')
                exit_units= False
                while exit_units == False:
                    if user_input.lower() == "m":
                        os.system('clear')
                        exit_units = True
                    elif user_input.lower() == "x":
                        return
                    else:
                        try:
                            unit_id = int(user_input)
                        except ValueError:
                            print('Invalid input. Please enter a valid option.\n')
                            user_input = input("Select Unit to see active visits (m for Main Menu, x to exit): ")

                        if unit_id not in unit_ids:
                            print(' ')
                            print('Invalid Unit ID')
                            print(' ')
                            user_input = input("Select Unit to see active visits (m for Main Menu, x to exit): ")
                        else:
                            os.system('clear')
                            print_unit_menu(self.units)
                            print(f'Visits in Unit {user_input}:')
                            print('-----------------')
                            if (int(user_input) in unit_ids):
                                for visit in self.visits:
                                    if visit.unit_id == int(user_input):
                                        print_visit(visit, self.patients, self.doctors )
                            print(' ')
                            user_input = input("Select Unit to see active visits (m for Main Menu, x to exit): ")
                
            elif user_input =="D" or user_input == "d":
                os.system('clear')
                print_visits(self.visits, self.patients, self.doctors, self.units)
                print('')
                user_input = input("m for Main Menu, x to exit: ")
                exit_visits= False
                while exit_visits == False:
                    if user_input.lower() == "m":
                        os.system('clear')
                        exit_visits = True
                    if user_input.lower() == "x":
                        return

            elif user_input =="/":
                os.system('clear')
                print_welcome_message()
                print_main_menu()
                user_input = input("Select Option: ")
                
            elif user_input =="X" or user_input == "x":
                os.system('clear')
                print_goodbye()
                exit = True

if __name__ == '__main__':
    engine = create_engine('sqlite:///hospital.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    CLI()