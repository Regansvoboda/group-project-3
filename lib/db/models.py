#!/usr/bin/env python3

from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///hospital.db')

Base = declarative_base()


class Patient(Base):
    __tablename__ = 'patients'

    id = Column(Integer(), primary_key=True)
    first_name = Column(String())
    last_name = Column(String())
    visits = relationship('Visit', backref=backref('patients'))
    
    def __repr__(self):
        return f"Patient: {self.id}: " \
                + f"Name: {self.first_name}, {self.last_name}"

class Doctor(Base):
    __tablename__ = 'doctors'

    id = Column(Integer(), primary_key=True)
    first_name = Column(String())
    last_name = Column(String())
    visits = relationship('Visit', backref=backref('doctors'))
    
    def __repr__(self):
        return f"Doctor: {self.id}: " \
                + f"Name: {self.first_name}, {self.last_name}"

class Unit(Base):
    __tablename__ = 'units'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    location = Column(String())
    visits = relationship('Visit', backref=backref('units'))
    
    def __repr__(self):
        return f"Unit: {self.id}: " \
                + f"Name: {self.name}" \
                + f"Location: {self.location}"
class Visit(Base):
    __tablename__ = 'visits'

    id = Column(Integer(), primary_key=True)
    patient_id = Column(Integer(), ForeignKey('patients.id'))
    doctor_id = Column(Integer(), ForeignKey('doctors.id'))
    unit_id = Column(Integer(), ForeignKey('units.id'))
    status = Column(String())

    def __repr__(self):
        return f"Visit: {self.id}: " \
                + f"Patient: {self.patient_id}" \
                + f"Doctor: {self.doctor_id}" \
                + f"Unit: {self.unit_id}" \
                + f"Status: {self.status}" \

if __name__ == '__main__':
    engine = create_engine('sqlite:///hospital.db')
    Base.metadata.create_all(engine)

