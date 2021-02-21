#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 11:17:07 2021

@author: invadgir07
"""

#in pounds
w = input("what is the weight? ")
weight = float(w)
#cost based on package weight(price per pound)
cost = float()
#for regular ground shipping only
flat_charge = int()

#cost of ground premium shipping(flat rate)
premium_shipping = 125
#ground shipping
if weight <= 2:
  cost = 1.50
  flat_charge = 20
elif weight > 2 and weight <= 6:
  cost = 3.00
  flat_charge = 20
elif weight > 6 and weight <= 10:
  cost = 4.00
  flat_charge = 20
else:
  cost = 4.75
  flat_charge = 20
#total cost to ship
total = float(weight) * float(cost) + int(flat_charge)
print("ground shipping is: ", total)
print("premium shipping is: ", premium_shipping)

#Drone shipping
if weight <= 2:
  cost = 4.50
  flat_charge = 0
elif weight > 2 and weight <= 6:
  cost = 9
  flat_charge = 0
elif weight > 6 and weight <= 10:
  cost = 12
  flat_charge = 0
else:
  cost = 14.25
  flat_charge = 0
total = weight * cost + flat_charge
print("drone shipping is: ", float(total))