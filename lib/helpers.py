# lib/helpers.py
from models.train import Train
from models.car import Car

# don't forget to give all these methods better names

def view_all_trains():
    print("You chose: View All Trains")
    all_the_trains = Train.get_all() # iterate through to make pretty?
    # [row for row in allthetrains]?
    print("All The Trains: \n")
    # for i in allthetrains:?
    print(f"{all_the_trains}>")

def view_all_cars():
    print("You chose: View All Cars") # iterate through to make it pretty?
    all_the_cars = Car.get_all()    
    print("All the Cars: \n")
    print(f"{all_the_cars}")

def view_train_by_id():
    print("You chose: View Train by ID")
    input_id = input("Enter Train ID: ")
    train_by_id = Train.find_by_id(input_id)
    print("Train by ID")
    print(f"{train_by_id}") if train_by_id else print(f'Train {input_id} not found')

def view_car_by_id():
    print("You chose: View Car by ID")
    input_id = input("Enter Car ID: ")
    car_by_id = Car.find_by_id(input_id)
    print("Car by ID")
    print(f"{car_by_id}") if car_by_id else print (f'Car {input_id} not found')

def add_new_train():
    print("You chose: Add a new Train")
    input_name = input("Enter New Train Name: ")
    input_type = input("Enter New Train Type: ")
    try:
        new_train = Train.create(input_name, input_type)
        print(f"New Train {new_train} Added!")
    except Exception as exc:
        print("Error creating new train: ", exc)

def view_train_by_name():
    print("You chose: View Train by name")
    input_name = input("Enter Train Name: ")
    train_by_name = Train.find_by_name(input_name)
    print("Train by Name: ")
    print(f"{train_by_name}") if train_by_name else print(f'Train {input_name} not found')

def view_all_cars_on_train():
    print("You chose: Show all Cars on a Train")
    input_id = 0
    input_id = input("Enter Train ID: ")
    try: 
        cars_on_train = Train.cars(input_id)
        print("Cars on this Train: ")
        print(f"{cars_on_train}")
    except Exception as exc:
        print (f"Error Finding Train {input_id} ")

def add_new_train():
    print("You chose: Add a New Train")
    input_name = input("Enter Train Name: ")
    input_type = input("Enter Train Type: ")
    try: 
        new_train = Train.create(input_name, input_type)
        print(f"New Train {new_train} Created!")
    except Exception as exc:
        print ("Error creating new Train: ", exc)

def remove_train_by_id():
    print("You chose: Remove a Train by ID")
    # input_id = 0
    input_id = input("Enter Train ID to Remove: ")
    removed_train = Train.find_by_id(input_id)
    if (removed_train):
        print(f"You removed the Train {removed_train}.")
        removed_train.delete()
    else:
        print(f'Train {input_id} not found')

    # removed_train.delete()
    # removed_train = Train.delete(input_id)

# def add_car_to_train():
#     print("You chose: Add a Car to a Train")
#     # print(f"Car {} added to Train!")

# def remove_car_from_train():
#     print("You chose: Remove a Car from a Train")

def exit_program():
    print("Goodbye!")
    exit()