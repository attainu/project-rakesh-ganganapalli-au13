1.ParkingLot

->Design a parking lot using Python

2.Description

->This repository gives an overview of how we can design a basic parking lot in Python. It creates parking lot with given number of slots. The cars follow Greedy approach while being parked in the slots.

3.ParkingLot.py script defines the following functions -

->create_parking_lot n - Given n number of slots, create a parking lot
->park car_regno car_color - Parks a vehicle with given registration number and color in the nearest empty slot possible. If there are no more empty slots available, it shows a message "Sorry, parking lot is full".
->status - Prints the slot number, registration number and color of the parked vehicles.
->leave x - Removes vehicle from slot number x
->There are few query functions to retrieve slot number from registration number of car, get registration numbers of cars with particular color etc.
->main.py can be run through shell.

->Vehicle.py is a separate class where we can define the type of vehicles that can be parked. As of now, it only contains class Car
->parking_lot.py is separate class where we can define all the funvtion related to parking lot
->main.py is separate file where we can run and take user inputs from terminal