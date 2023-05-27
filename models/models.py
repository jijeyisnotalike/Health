from sqlalchemy import *
from sqlalchemy.orm import *
from db import Base
from datetime import *

class Registration(Base):
    __tablename__ = 'registration'
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    middle_name = Column(String, nullable=False)
    passport_id = Column(String, nullable=False)
    location = Column(String, nullable=False)
    profession = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)
    email = Column(String, nullable=False)
    create_at = Column(DateTime, default=datetime.now)
    update_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

class Appointment(Base):
    __tablename__ = 'appointment'
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    middle_name = Column(String, nullable=False)
    passport_id = Column(String, nullable=False)
    doctors_name = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)
    email = Column(String, nullable=False)
    empty_spaces = Column(String, nullable=False)
    create_at = Column(DateTime, default=datetime.now)
    update_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)


class Question(Base):
    __tablename__ = 'question'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False)
    text = Column(String, nullable=False)
    create_at = Column(DateTime, default=datetime.now)
    update_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    
    answer = relationship('Answer', back_populates='question')
    

class Answer(Base):
    __tablename__ = 'answer'
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, nullable=False)
    question_id = Column(Integer, ForeignKey('question.id'))
    create_at = Column(DateTime, default=datetime.now)
    update_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    
    question = relationship('Question', back_populates='answer')