from sqlalchemy.orm import Session
from sqlalchemy.exc import OperationalError

from models.co2 import Co2
from config import engine

from co2 import get_data
from time import sleep

while True:
    try:
        dajet = get_data()

        s = Session(bind=engine)

        s.add(Co2(
            temp = dajet["temp"],
            co2 = dajet["co2"],
        ))
        s.commit()
        s.close()

        sleep(55)
    except OperationalError as OE:
        engine.connect()