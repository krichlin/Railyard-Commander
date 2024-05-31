#!/usr/bin/env python3
# lib/seed.py

from models.__init__ import CONN, CURSOR
from models.train import Train
from models.car import Car

def reset_database():
    # Reinitialize all the tables here
    Train.drop_table()
    Car.drop_table()

    Train.create_table()
    Car.create_table()

    # Populate the tables with some test data
    passenger_1 = Train.create("Passenger Express", "Stephenson Rocket")
    cargo_1 = Train.create("Cargo Special", "0-4-0 Dewitt Clinton")
    mail_1 = Train.create("Mail Train", "4-2-0 Prussian")
    passenger_2 = Train.create("Passenger All Stops", "Trevithick-1")

    car_1 = Car.create("Mail Car", "Pullman Red", mail_1.id)
    car_2 = Car.create("Engine", "Stevenson Rocket", cargo_1.id)
    car_3 = Car.create("Passenger Car", "Pullman Special", passenger_1.id)
    car_4 = Car.create("Passenger Car", "Pullman Special", passenger_2.id)

reset_database() # reset the database and populate filler data