from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Write code for classes here
class Artist(Base):
    __tablename__ = 'artists'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    genre = Column(String)
    age = Column(Integer)
    hometown = Column(String)

    def __init__(self, name, genre, age, hometown):
        self.name = name
        self.genre = genre
        self.age = age
        self.hometown = hometown

class Song(Base):
    __tablename__ = 'songs'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    length = Column(Integer)

    def __init__(self, name, length):
        self.name = name
        self.length = length


engine = create_engine('sqlite:///artists.db')
Base.metadata.create_all(engine)
