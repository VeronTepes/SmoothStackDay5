# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 15:37:52 2022

@author: owner
"""

#Day 5 –Weekend exercise work – please use functions for this problem
#Let us apply our programming skills to some quasi-scientific problem - since it is bit dull to learn only abstract things.
#The simple measure of body constitution was proposed at the middle of XIX century. It depends only on the height and weight of a person - and is called Body Mass Index or BMI. It is defined as:
#BMI = weight / height^2
#Where weight is taken in kilograms and height in meters.
#Four general grades are proposed:
#Underweight     -           BMI < 18.5
#Normal weight   -   18.5 <= BMI < 25.0
#Overweight      -   25.0 <= BMI < 30.0
#Obesity         -   30.0 <= BMI
#For example, if I have weight of 80 kg and height of 1.73 m I can calculate:
#BMI = 80 / (1.73)^2 = 26.7
#i.e. somewhat overweight.
#We will not discuss how proper or improper this gradation is. Instead you should simply calculate grades for several people.
#Input data contain number of people in the first line.
#Other lines will contain two values each - weight in kilograms and height in metres.
#Answer should contain words under, normal, over, obese for each corresponding test-case, separated with spaces. For example:
#input data:
#3
#80 1.73
#55 1.58
#49 1.91

#answer:
#over normal under

#get number of people
numpeople = input("How many people are we calculating the BMI for? ")

BMI = []

#for all people get height and weight on same line.
for i in range(0, int(numpeople)):
    #get height and weight on same line.
    weight, height = input("Please enter person {}'s weight and height (i.e. 80 1.73): ".format(i)).split()
    
    #make height and weight into floating instead of strings.
    height = float(height)
    weight = float(weight)
    #print(type(height))
    #print(type(weight))
    
    #calculate BMI
    BMI.append((weight/pow(height,2)))
    
#output the bmi's
for i in range(0, int(numpeople)):
    if BMI[i] < 18.5:
        print("Person number {} is Underweight.".format(i+1))
    elif BMI[i] < 25:
        print("Person number {} is a Normal Weight.".format(i+1))
    elif BMI[i] < 30:
        print("Person number {} is Overweight.".format(i+1))
    else:
        print("Person number {} is Obese.".format(i+1))