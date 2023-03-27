#!/usr/bin/env python3

from sqlalchemy import Column, Integer, String, create_engine

from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///trivia.db')

Base = declarative_base()


class Question(Base):
    __tablename__ = 'questions'

    id = Column(Integer(), primary_key=True)
    question = Column(String())
    answer = Column(String())
    category = Column(String())
    difficulty = Column(String())




if __name__ == '__main__':
    engine = create_engine('sqlite:///trivia.db')
    Base.metadata.create_all(engine)

