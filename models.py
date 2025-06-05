from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy.orm import class_mapper
import uuid
from datetime import datetime
from decimal import Decimal

from sqlalchemy import Column, Integer, String, Boolean, DateTime, Time, Float, Text, ForeignKey, JSON, Numeric, Date, \
    TIMESTAMP, UUID
from sqlalchemy.ext.declarative import declarative_base


@as_declarative()
class Base:
    id: int
    __name__: str

    # Auto-generate table name if not provided
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    # Generic to_dict() method
    def to_dict(self):
        """
        Converts the SQLAlchemy model instance to a dictionary, ensuring UUID fields are converted to strings.
        """
        result = {}
        for column in class_mapper(self.__class__).columns:
            value = getattr(self, column.key)
                # Handle UUID fields
            if isinstance(value, uuid.UUID):
                value = str(value)
            # Handle datetime fields
            elif isinstance(value, datetime):
                value = value.isoformat()  # Convert to ISO 8601 string
            # Handle Decimal fields
            elif isinstance(value, Decimal):
                value = float(value)

            result[column.key] = value
        return result




class Addresses(Base):
    __tablename__ = 'addresses'
    id = Column(Integer, primary_key=True)
    street = Column(String, primary_key=False)
    city = Column(String, primary_key=False)
    state = Column(String, primary_key=False)
    country = Column(String, primary_key=False)
    postal_code = Column(String, primary_key=False)
    created_at = Column(Time, primary_key=False)
    updated_at = Column(Time, primary_key=False)


class Persons(Base):
    __tablename__ = 'persons'
    rollnumber = Column(Integer, primary_key=True)
    fullname = Column(String, primary_key=False)
    age = Column(Integer, primary_key=False)
    profession = Column(String, primary_key=False)
    to_be_deleted = Column(Integer, primary_key=False)


class HelloasTesting(Base):
    __tablename__ = 'helloas_testing'
    id = Column(Integer, primary_key=True)


class TestingTempo(Base):
    __tablename__ = 'testing_tempo'
    id = Column(Integer, primary_key=True)


