from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Write code for classes here


engine = create_engine('sqlite:///artists.db')
Base.metadata.create_all(engine)
