# Write your code for lab 8C (remove) here.
from cal_abstraction import *
from cal_ui import *

def remove(cal_name: str, day: int, month: str, start: str) -> None:
    day = new_day(day)
    mon = new_month(month)
    start = new_time_from_string(start)
    cal_year = get_calendar(cal_name) #gets the year
    cal_month = cy_get_month(mon, cal_year) # gets the month
    cal_day = cm_get_day(cal_month, day) # get the date 
    new_cal_day = []
    for app in cal_day.appointments:
        new_cal_day.append(cd_plus_appointment(cal_day, app))
    new_cal_month = cm_plus_cd(cal_month, new_cal_day)
    new_cal_year = cy_plus_cm(cal_year, new_cal_month)

    for appointment in new_cal_day.appointments:  # checks if the start time exists in the date
        if start == ts_start(app_span(appointment)):
            new_cal_day.appointments.remove(appointment)
    return new_cal_year
 

def test_labc():
    create("Jayne")
    create("Jayne")
    book("Jayne", 20, "sep", "12:00", "14:00", "Rob train")
    book("Jayne", 20, "sep", "15:00", "16:00", "Escape with loot")
    show("Jayne", 20, "sep")
    remove("Jayne", 20, "sep", "15:00")
    show("Jayne", 20, "sep")

test_labc()