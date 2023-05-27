from pydantic import BaseModel


class signupSchema(BaseModel):
    first_name: str
    last_name: str
    middle_name: str
    passport_id: str
    location: str
    profession: str
    phone_number: str
    email: str

class appointmentSchema(BaseModel):
    first_name: str
    last_name: str
    middle_name: str
    passport_id: str
    doctors_name: str
    phone_number: str
    email: str
    empty_spaces: str

class questionSchema(BaseModel):
    username: str
    email: str
    text: str
    
    
class answerSchema(BaseModel):
    text: str
    question_id: int