"""Calculates your Age"""

# Import Relevent Modules
from datetime import datetime
from dateutil.relativedelta import relativedelta
import PySimpleGUI as sg

def AgeCalculator(user_input:str):

    # Convert str to datetime format
    today = datetime.now()
    birth_date = datetime.strptime(user_input, '%d/%m/%Y') # Converting date str to datetime
    date_delta = relativedelta(today, birth_date)

    # Check if the input date is from future
    if date_delta.days < 0:
        raise ValueError("Please enter a valid birth date")
    
    return f"Your Age is {date_delta.years} Years {date_delta.months} Months {date_delta.days} Days"

if __name__ == "__main__":
    layout = [
    [sg.Text("What's your Birth Date?")],
    [sg.InputText()],
    [sg.Button('Ok'), sg.Button('Cancel')]
    ]

    # Create the window
    window = sg.Window('Age Calculator', layout)
    # Event loop
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':
            break
        print(AgeCalculator(values[0]))

    window.close()
    

