from sqlalchemy.orm import Session
from sqlalchemy.orm import joinedload
from sqlalchemy import or_, and_
from models import signupSchema, Registration, questionSchema, answerSchema, appointmentSchema


def signUp(req, db: Session):
    signup = db.query(Registration).filter(
        or_(
            Registration.first_name == req.first_name,
            Registration.last_name == req.last_name,
            Registration.middle_name == req.middle_name,
            Registration.passport_id == req.passport_id,
            Registration.location == req.location,
            Registration.profession == req.profession,
            Registration.phone_number == req.phone_number,
            Registration.email == req.email
        )
    ).first()
    new_add = Registration(**req.dict())
    db.add(new_add)
    db.commit()
    db.refresh(new_add)
    return True

def read_users(db: Session):
    result = db.query(
        Registration,
    ).all()
    return result




def appointment(req, db: Session):
    signup = db.query(Appointment).filter(
        or_(
            Appointment.first_name == req.first_name,
            Appointment.last_name == req.last_name,
            Appointment.middle_name == req.middle_name,
            Appointment.passport_id == req.passport_id,
            Appointment.doctors_name == req.doctors_name,
            Appointment.phone_number == req.phone_number,                      
            Appointment.email == req.email,
            Appointment.empty_spaces == req.empty_spaces
        )
    ).first()
    new_add = Appointment(**req.dict())
    db.add(new_add)
    db.commit()
    db.refresh(new_add)
    return True

def read_patient(db: Session):
    result = db.query(
        Appointment,
    ).all()
    return result



def create_qa(req, model, db: Session):
    new_add = model(**req.dict())
    db.add(new_add)
    db.commit()
    db.refresh(new_add)
    return new_add


def read_questions(db: Session):
    result = db.query(Question).options(joinedload(Question.answer)).all()
    return result