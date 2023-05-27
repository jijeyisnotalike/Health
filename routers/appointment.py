from fastapi import *
from fastapi.requests import Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.security import HTTPBearer
from sqlalchemy import *
from sqlalchemy.orm import *
from db import get_db
import crud
from models import appointmentSchema, Appointment


appointment_router = APIRouter()

@appointment_router.post('/appointment')
def appointment(req: appointmentSchema, db: Session = Depends(get_db)):
    try:
        result = crud.appointment(req, db)
        if result == -1:
            return JSONResponse(status_code=status.HTTP_416_REQUESTED_RANGE_NOT_SATISFIABLE, content={'result': 'Failed to sign up'})
        elif result:
            return JSONResponse(status_code=status.HTTP_201_CREATED, content={'result': 'Successfully sign up'})
        else:
            return JSONResponse(status_code=status.HTTP_406_NOT_ACCEPTABLE, content={'result': 'User already exists'})
    except Exception as e:
        print(e)
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Something went wrong')


@appointment_router.get('/get_patient')
def get_patient(db: Session = Depends(get_db)):
    try:
        result = crud.read_patient(db)
        result = jsonable_encoder(result)
        return JSONResponse(status_code=status.HTTP_200_OK, content=result)
    except Exception as e:
        print(e)
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Something went wrong')