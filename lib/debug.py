#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import CONN, CURSOR
from models.train import Train
from models.car import Car

import ipdb

# passenger_express = Train("Passenger Express", "Stephenson Rocket")
# print(passenger_express)  

# passenger_express.save()  #persist to db, assign object id attribute
# print(passenger_express)

# mail_train = Train("Mail Train", "John Bull")
# print(mail_train)

# mail_train.save() # persist to db, assign object id attribute
# print(mail_train)

# train_1 = Train.create("Cargo Special", "0-4-0 Dewitt Clinton")
# print(train_1)  

# train_2 = Train.create("Mail Train", "4-2-0 Prussian")
# print(train_2)

# train_2.name = 'MAILY JOE'
# train_2.type = "Trevithick-1"
# train_2.update()
# print(train_2)

# print("Delete the Cargo Special")
# train_1.delete() # delete from db table, object remains in memory
# print(train_1)

def reset_database():

    # Reinitialize all the tables here

    Train.drop_table()
    Car.drop_table()

    Train.create_table()
    Car.create_table()

    # Fill them with some filler data
    passenger_1 = Train.create("Passenger Express", "Stephenson Rocket")
    cargo_1 = Train.create("Cargo Special", "0-4-0 Dewitt Clinton")
    mail_1 = Train.create("Mail Train", "4-2-0 Prussian")
    passenger_2 = Train.create("Passenger All Stops", "Trevithick-1")

    car_1 = Car.create("Mail Car", "Pullman Red", mail_1.id)
    car_2 = Car.create("Engine", "Stevenson Rocket", cargo_1.id)
    car_3 = Car.create("Passenger Car", "Pullman Special", passenger_1.id)


reset_database() # reset the database
ipdb.set_trace()
pass # need some code to live after set_trace to avoid errors