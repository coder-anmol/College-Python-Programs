# Input : data
# Output: Today's Day

from datetime import datetime


def get_weekday(input_date):
    new_date = datetime.strptime(input_date, "%d-%m-%Y")
    return new_date.strftime("%A")


my_date = input("Enter date in this format (Day-Month-Year): ")
print(get_weekday(my_date))
