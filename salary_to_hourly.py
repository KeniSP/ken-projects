#!/usr/local/bin/python3
#Calculating your yearly pay into bi weekky and hourly rates

while True:
    print()
    yearly_salary = float(input("Enter Yearly Salary: "))
    extra_income_question = input("Do you want to include a extra income?: ")
    if extra_income_question in ("y", "yes", "Yes", "Y"):
        extra_income = input("Enter Total Extra Income: ")
        try:
            extra_income = float(extra_income)
        except ValueError:
            print("Extra Income was an invalid number")
            extra_income = 0.0
    else:
        extra_income = 0.0

    #math below is based on 26 paychecks a year and a 40 hour work week. Aka 80 hours in 2 weeks

    total_pay = yearly_salary + extra_income
    print("Total Yearly Pay:" , total_pay)
    biweekly_salary = yearly_salary / 26
    hourly_salary = biweekly_salary / 80
    print("You make:" , round(biweekly_salary) , "dollars Bi Weekly before tax")
    print("You make:" , round(hourly_salary) , "dollars an hour before tax")
