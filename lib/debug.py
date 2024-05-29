#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import CONN, CURSOR
from models.train import Train
import ipdb

# Reinitialize all the tables here
Train.drop_table()
Train.create_table()

# passenger_express = Train("Passenger Express", "Stephenson Rocket")
# print(passenger_express)  

# passenger_express.save()  #persist to db, assign object id attribute
# print(passenger_express)

# mail_train = Train("Mail Train", "John Bull")
# print(mail_train)

# mail_train.save() # persist to db, assign object id attribute
# print(mail_train)

train_1 = Train.create("Cargo Special", "0-4-0 Dewitt Clinton")
print(train_1)  

train_2 = Train.create("Mail Train", "4-2-0 Prussian")
print(train_2)

train_2.name = 'MAILY JOE'
train_2.type = "Trevithick-1"
train_2.update()
print(train_2)

print("Delete the Cargo Special")
train_1.delete() # delete from db table, object remains in memory
print(train_1)

ipdb.set_trace()
pass # need some code to live after set_trace to avoid errors