from fastapi import FastAPI
from app.database.tables import Base
from app.database.connection import engine
from app.routes.url_routes import router
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

Base.metadata.create_all(engine)

@app.get("/")
def health():
    return  {"message": "Api is running"} 
app.include_router(router)
