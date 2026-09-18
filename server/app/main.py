from fastapi import FastAPI
from app.database.tables import Base
from app.database.connection import engine
from app.routes.url_routes import router


app = FastAPI()

Base.metadata.create_all(engine)

@app.get("/")
def health():
    return  {"message": "Api is running"} 
app.include_router(router)
