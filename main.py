from datetime import datetime
import os

import mysql
from sqlalchemy.orm import declarative_base
from sqlalchemy import (
    Column,
    String,
    DateTime,
    Integer,
    create_engine,
)

BASE_DIR = os.path.join(os.path.realpath(__file__))
engeni = create_engine(f"mysql://scott:tiger@localhost/{BASE_DIR}/task.db")
Base = declarative_base()


class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer(), primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    date_created = Column(DateTime(), default=datetime.utcnow)

    def __str__(self):
        return f"<Task name={self.name}>"
    
    
    