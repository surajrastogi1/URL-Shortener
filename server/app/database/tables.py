from sqlalchemy.orm import declarative_base
from sqlalchemy import DateTime,Column,String,Integer
from pydantic import BaseModel, HttpUrl
from datetime import datetime

Base = declarative_base()



class URL(Base):
    __tablename__ = "urls"

    id = Column(Integer,primary_key=True)
    long_url = Column(String, nullable=False)
    short_code = Column(String,unique=True, nullable=False)
    created_at = Column(DateTime,default = datetime.utcnow,nullable=False)


class URLCreate(BaseModel):
    long_url : HttpUrl
