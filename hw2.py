# 1..write a python code to find compund interest of an amount
#  A= P(1+(r/n))^(nt), where A is the final amount, 
# P is the principal, r is the annual interest rate (as a decimal), 
# n is the number of times interest is compounded per year, an
# t is the number of years the money is invested or borrowed.

principle= float(input("enter principle amount:"))
rate= float(input("enter rate of interest percentage:"))
time= float(input("enter time (in years):"))
n= int(input("enter number of times interest is compounded per year:"))

rate_of_interest = ( rate / 100 )  #converting the percentage to decimal

amount = principle * (1 + (rate_of_interest/n))**(n * time)

print(f"the final amount of compund interest after {time} years is {amount} " )


 
# 2.. find the area of a circle
radius = float(input("enter the radius(in cm):"))

pi = 3.1416

area = pi * (radius ** 2)

print(f"the area of the circle is {area} cm^2 ")

