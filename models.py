from flask_login import UserMixin
from __init__ import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

class Main(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

class Station(db.Model):

    operator = db.Column(db.String(100))
    station = db.Column(db.String(100),nullable=False)
    date = db.Column(db.String(100), primary_key=True)
    acreg = db.Column(db.String(100),nullable=False)
    fltno = db.Column(db.String(100), primary_key=True)
    actype = db.Column(db.String(100))
    sector = db.Column(db.String(100))
    sta = db.Column(db.String(100))
    std = db.Column(db.String(100))
    ata = db.Column(db.String(100))
    atd = db.Column(db.String(100))
    aircraftcheck = db.Column(db.String(100))
    defect = db.Column(db.String(1000))
    rectification = db.Column(db.String(1000))
    delay = db.Column(db.String(100))
    engineer = db.Column(db.String(100))
    technician = db.Column(db.String(100))
    month = db.Column(db.String(100))
    status = db.Column(db.String(100), nullable=False)
    comment = db.Column(db.String(1000))

    def __init__(self,operator,station,date,acreg,fltno,actype,sector,sta,std,ata,atd,aircraftcheck,defect,rectification,
                 delay,engineer,technician,month,status, comment):

        self.operator=operator
        self.station=station
        self.date=date
        self.acreg=acreg
        self.fltno=fltno
        self.actype=actype
        self.sector=sector
        self.sta=sta
        self.std=std
        self.ata=ata
        self.atd=atd
        self.aircraftcheck=aircraftcheck
        self.defect=defect
        self.rectification=rectification
        self.engineer=engineer
        self.delay=delay
        self.technician=technician
        self.month=month
        self.status=status
        self.comment=comment


class AME(db.Model):
        id = db.Column(db.Integer, primary_key=True, auto_increment=True )
        amename = db.Column(db.String(100), unique=True, nullable=False)

def __init__(self, id, amename):
        self.id = id
        self.amename = amename

class FlightNO(db.Model):
        id = db.Column(db.Integer, primary_key=True, auto_increment=True )
        fltno = db.Column(db.String(100), unique=True, nullable=False)

def __init__(self, id, fltno):
        self.id = id
        self.fltno = fltno


class WorkOrder(db.Model):
    ticketno=db.Column(db.String(100), primary_key=True , nullable=False)
    date = db.Column(db.String(100),  db.ForeignKey('station.date'), nullable=False)
    fltno = db.Column(db.String(100), db.ForeignKey('station.fltno'), nullable=False)
    charges = db.Column(db.Double(), nullable=False)
    rectification = db.Column(db.String(100))
    recticharge = db.Column(db.Double(), nullable=False)
    gseprovided = db.Column(db.String(100))
    gsecharge = db.Column(db.Double(), nullable=False)
    fluidprovided = db.Column(db.String(100))
    fluidcharge = db.Column(db.Double(), nullable=False)
    remarks = db.Column(db.String(1000))

    def __init__(self,ticketno,date,fltno,charges,rectification,recticharge,gseprovided,gsecharge,
                 fluidprovided,fluidcharge,remarks):

        self.ticketno = ticketno
        self.date = date
        self.fltno = fltno
        self.charges =charges
        self.rectification = rectification
        self.recticharge = recticharge
        self.gseprovided =gseprovided
        self.gsecharge = gsecharge
        self.fluidprovided = fluidprovided
        self.fluidcharge = fluidcharge
        self.remarks =remarks
