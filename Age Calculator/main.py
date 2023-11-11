"""Calculates your Age"""

# Import Relevent Modules
from datetime import datetime
from dateutil.relativedelta import relativedelta

def AgeCalculator(user_input:str):

    # Convert str to datetime format
    today = datetime.now()
    birth_date = datetime.strptime(user_input, '%d/%m/%Y') # Converting date str to datetime
    delta = relativedelta(today, birth_date)

    # Check if the input date is from future
    if delta.days < 0:
        raise ValueError("Please enter a valid birth date")
    
    return f"Your Age is {delta.years} Years {delta.months} Months {delta.days} Days"

if __name__ == __name__:
    print("*****Age Calculator*****")
    user_input = input("Enter birth date in DD/MM/YYYY format: ")
    age = AgeCalculator(user_input)
    print(age)

