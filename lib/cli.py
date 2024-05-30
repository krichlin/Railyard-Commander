# lib/cli.py
#! /usr/bin/env python3

from helpers import (
    exit_program,
    helper_1,
    helper_2,
    helper_3,
    helper_4,
    helper_5,
    helper_6,
    helper_7,
    helper_8,
    helper_9,
    # helper_10,
    # helper_11
)

def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            helper_1()
        elif choice == "2":
            helper_2()
        elif choice == "3":
            helper_3()
        elif choice == "4":
            helper_4()
        elif choice == "5":
            helper_5()
        elif choice == "6":
            helper_6()
        elif choice == "7":
            helper_7()
        elif choice == "8":
            helper_8()
        elif choice == "9":
            helper_9()
        # elif choice == "10":
        #     helper_10()
        # elif choice == "11":
        #     helper_11()
        else:
            print("Invalid choice")


def menu():
    print("WELCOME TO RAILYARD COMMANDER!")
    print("Please Select an Option: ")
    print("0. Exit the program")
    print("1. View All Trains")
    print("2. View All Cars")
    print("3. Show Train by ID")
    print("4. Show Car by ID")
    print("5. Add a New Train")
    print("6. Show Train by Name")
    print("7. Show all Cars on a Train")
    print("8. Add a New Train")
    print("9. Remove a Train by ID")
    # print("10. Add a Car to a Train")
    # print("11. Remove a Car from a Train")

if __name__ == "__main__": #only run this script if called from command line
    main() 