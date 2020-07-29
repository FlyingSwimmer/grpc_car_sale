from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
db_string = "postgresql://postgres:password@localhost:5432/car_sale"

connection = create_engine(db_string, echo=True)

Base = declarative_base()

import database.models

Base.metadata.create_all(connection)

Session = sessionmaker(connection)