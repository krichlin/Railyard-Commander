# lib/cli.py
#! /usr/bin/env python3

from helpers import (
    exit_program,
    view_all_trains,
    view_all_cars,
    view_train_by_id,
    view_car_by_id,
    add_new_train,
    view_train_by_name,
    view_all_cars_on_train,
    add_new_train,
    remove_train_by_id,
    # add_car_to_train,
    # remove_car_from_train
)

def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            view_all_trains()
        elif choice == "2":
            view_all_cars()
        elif choice == "3":
            view_train_by_id()
        elif choice == "4":
            view_car_by_id()
        elif choice == "5":
            add_new_train()
        elif choice == "6":
            view_train_by_name()
        elif choice == "7":
            view_all_cars_on_train()
        elif choice == "8":
            add_new_train()
        elif choice == "9":
            remove_train_by_id()
        # elif choice == "10":
        #     add_car_to_train()
        # elif choice == "11":
        #     remove_car_from_train()
        else:
            print("Invalid choice")


def menu():
    print("WELCOME TO RAILYARD COMMANDER!")
    print("Please Select an Option: ")
    print("0. Exit the program")
    print("1. View All Trains")
    print("2. View All Cars")
    print("3. View Train by ID")
    print("4. View Car by ID")
    print("5. Add a New Train")
    print("6. View Train by Name")
    print("7. View all Cars on a Train")
    print("8. Add a New Train")
    print("9. Remove a Train by ID")
    # print("10. Add a Car to a Train")
    # print("11. Remove a Car from a Train")

if __name__ == "__main__": #only run this script if called from command line
    main() 