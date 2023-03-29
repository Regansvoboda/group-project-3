#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

from models import Patient, Doctor, Unit, Visit

if __name__ == '__main__':
    
    engine = create_engine('sqlite:///hospital.db')
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    session.query(Patient).delete()
    session.query(Doctor).delete()
    session.query(Unit).delete()
    session.query(Visit).delete()

    scott_henry = Patient(
        first_name="Scott",
        last_name="Henry",
    )
    
    regan_svoboda = Patient(
        first_name="Regan",
        last_name="Svoboda",
    )
    
    connor_sheets = Patient(
        first_name="Connor",
        last_name="Sheets",
    )
    
    doctor_bad = Doctor(
        first_name="Bad",
        last_name="Doctor",
    )
    
    doctor_good = Doctor(
        first_name="Good",
        last_name="Doctor",
    )
    
    doctor_feelgood = Doctor(
        first_name="Doctor",
        last_name="Feelgood",
    )

    unit_1 = Unit(
        name="Recovery",
        location="A Wing",
    )
    
    unit_2 = Unit(
        name="Emergency",
        location="B Wing",
    )  
    
    visit_1 = Visit(
        patient_id=1,
        doctor_id=2,
        unit_id=1,
        status="Dead",
    )
    
    visit_2 = Visit(
        patient_id=2,
        doctor_id=2,
        unit_id=2,
        status="Discharged",
    )
    
    visit_3 = Visit(
        patient_id=2,
        doctor_id=3,
        unit_id=2,
        status="AWESOME!",
    )

    session.bulk_save_objects([scott_henry, regan_svoboda, connor_sheets, doctor_bad, doctor_good, doctor_feelgood, unit_1, unit_2, visit_1, visit_2, visit_3])
    session.commit()
    # session.close()


    
    
    

