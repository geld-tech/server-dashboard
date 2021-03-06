import datetime
from sqlalchemy import Column, ForeignKey, Integer, BigInteger, Float, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Server(Base):
    __tablename__ = 'server'
    id = Column(Integer, primary_key=True)
    hostname = Column(String(250), nullable=False)


class SystemInformation(Base):
    __tablename__ = 'system_information'
    id = Column(Integer, primary_key=True)
    platform = Column(String(250))
    system = Column(String(128))
    release = Column(String(128), nullable=False)
    server_id = Column(Integer, ForeignKey('server.id'))
    server = relationship(Server)


class SystemStatus(Base):
    __tablename__ = 'system_status'
    id = Column(Integer, primary_key=True)
    cpu_percent = Column(Float)
    vmem_percent = Column(Float)
    swap_percent = Column(Float)
    cpu_temp = Column(Float)
    date_time = Column(DateTime(timezone=True), default=datetime.datetime.utcnow)
    timestamp = Column(BigInteger)
    server_id = Column(Integer, ForeignKey('server.id'))
    server = relationship(Server)


class Process(Base):
    __tablename__ = 'processes'
    id = Column(Integer, primary_key=True)
    pid = Column(String(16))
    name = Column(String(1024))
    cpu_percent = Column(Float)
    date_time = Column(DateTime(timezone=True), default=datetime.datetime.utcnow)
    timestamp = Column(BigInteger)
    server_id = Column(Integer, ForeignKey('server.id'))
    server = relationship(Server)
