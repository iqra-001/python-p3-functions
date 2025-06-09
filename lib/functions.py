#!/usr/bin/env python3

def greet_programmer():
    print ("Hello, programmer!")

greet_programmer()


def greet(name = "Naureen"):
   print(f"Hello, {name}!")


greet()

 

def greet_with_default(name="programmer"):
    print (f"Hello, {name}!")


print(greet_with_default("iqra"))

   

def add(num1, num2):
    result = num1 + num2
    return result

add(1,2)


def halve(number):
    return number/2

halve(4)