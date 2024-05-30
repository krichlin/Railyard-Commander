# lib/helpers.py
from models.train import Train
from models.car import Car

# don't forget to give all these methods better names

def helper_1():
    print("You chose: View All Trains")
    all_the_trains = Train.get_all() # iterate through to make pretty?
    # [row for row in allthetrains]?
    print("All The Trains: \n")
    # for i in allthetrains:?
    print(f"{all_the_trains}>")

def helper_2():
    print("You chose: View All Cars") # iterate through to make it pretty?
    all_the_cars = Car.get_all()    
    print("All the Cars: \n")
    print(f"{all_the_cars}")

def helper_3():
    print("You chose: Show Train by ID")
    input_id = input("Enter Train ID: ")
    train_by_id = Train.find_by_id(input_id)
    print("Train by ID")
    print(f"{train_by_id}")

def helper_4():
    print("You chose: Show Car by ID")
    input_id = input("Enter Car ID: ")
    car_by_id = Car.find_by_id(input_id)
    print("Car by ID")
    print(f"{car_by_id}")

def helper_5():
    print("You chose: Add a new Train")
    input_name = input("Enter New Train Name: ")
    input_type = input("Enter New Train Type: ")
    new_train = Train.create(input_name, input_type)
    print(f"New Train {new_train} Added!")

def helper_6():
    print("You chose: Show Train by name")
    input_name = input("Enter Train Name: ")
    train_by_name = Train.find_by_name(input_name)
    print("Train by Name: ")
    print(f"{train_by_name}")

def helper_7():
    print("You chose: Show all Cars on a Train")
    input_id = 0
    input_id = input("Enter Train ID: ")
    cars_on_train = Train.cars(input_id)
    print("Cars on this Train: ")
    print(f"{cars_on_train}")

def helper_8():
    print("You chose: Add a Car to a Train")

def helper_9():
    print("You chose: Remove a Car from a Train")

def helper_10():
    print("You chose: Add a New Train")

def helper_11():
    print("You chose: Remove a Train by ID")

def exit_program():
    print("Goodbye!")
    exit()