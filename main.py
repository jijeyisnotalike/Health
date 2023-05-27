from fastapi import FastAPI
# from fastapi.staticfiles import StaticFiles
from db import Base, engine
from routers import authentication_router, appointment_router, qa_router


app = FastAPI()


Base.metadata.create_all(engine)



app.include_router(authentication_router, tags=['Authentication'])
app.include_router(appointment_router, tags=['Appointment'])
app.include_router(qa_router, tags=['Q&A'])
