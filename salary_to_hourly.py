#!/usr/local/bin/python3
#Calculating your yearly pay into bi weekky and hourly rates

import sys
import os

def letter_error():
    print("numbers only, no commas or letters, restarting")
    os.execv(__file__, sys.argv)


yearly_salary = float(input("Enter Yearly Salary: "))
try:
    yearly_salary_ival = int(yearly_salary)
except:
    yearly_salary_ival = -1
    if yearly_salary_ival > 0:
        print("Thanks, moving on")
    else:
        letter_error()

#using int to check for a number else restart script. Also float to accomidate for decimal points

extra_income_question = input("Do you want to include a extra income?: ")
if extra_income_question in ("Yes", "yes", "y", "Y"):
    extra_income = input("Enter Bonus: ")
    try:
        extra_income_ival = int(float(extra_income))
    except:
        extra_income_ival = -1
        if extra_income_ival > 0:
            print(" ")
        else:
            letter_error()
elif extra_income_question in ("No", "no", "n", "N"):
    extra_income = 0.0
else:
    print("Expecting 'Yes' or 'No', restarting")
    os.execv(__file__, sys.argv)

# if yes or no is not provided the script stops here and will need to be ran again to complete

total_pay = float(yearly_salary) + float(extra_income)
print("Total Yearly Pay:" , total_pay)
biweekly_salary = float(yearly_salary) / float(26)
hourly_salary = float(biweekly_salary) / float(80)
print("You make:" , round(biweekly_salary) , "dollars Bi Weekly before tax")
print("You make:" , round(hourly_salary) , "dollars an hour before tax")
print("Restarting for next use")
os.execv(__file__, sys.argv)