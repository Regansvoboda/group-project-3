#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.models import Patient, Doctor, Unit, Visit

if __name__ == '__main__':
    engine = create_engine('sqlite:///db/hospital.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    patients = [patient for patient in session.query(Patient)]
    doctors = [doctor for doctor in session.query(Doctor)]
    units = [unit for unit in session.query(Unit)]
    visits = [visit for visit in session.query(Visit)]
    breakpoint()

    print("working")

    import ipdb; ipdb.set_trace
