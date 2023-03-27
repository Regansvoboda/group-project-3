#!/usr/bin/env python3

from sqlalchemy import Column, Integer, String, create_engine

from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///trivia.db')

Base = declarative_base()


class Question(Base):
    __tablename__ = 'questions'

    id = Column(Integer(), primary_key=True)
    question = Column(String())
    answer1 = Column(String())
    answer2 = Column(String())
    answer3 = Column(String())
    answer4 = Column(String())
    correct_answer = Column(String())


if __name__ == '__main__':
    engine = create_engine('sqlite:///trivia.db')
    Base.metadata.create_all(engine)

