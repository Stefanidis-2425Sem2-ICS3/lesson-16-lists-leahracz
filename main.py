#Name: Leah Raczkowski
#Date: March 25th, 2025
#Title: Lesson 16
#Description: List of 100 numbers from 0-100, then finds average

#List
import random
number_list = []

#Loop to get 100 numbers
for i in range(100):
    num = random.randint(0,100)
    number_list.append(num)

#Print
print(number_list)
average = sum(number_list)/len(number_list)
print("The average is:",average)