# Write your code for lab 8C (remove) here.
from cal_abstraction import *
from cal_ui import *

def remove(cal_name: str, day: int, month: str, start: str) -> None:
    day = new_day(day)
    mon = new_month(month)
    start = new_time_from_string(start)
    cal_year = get_calendar(cal_name)
    cal_month = cy_get_month(mon, cal_year)
    cal_day = cm_get_day(cal_month, day)

    for appointment in cal_day.appointments:
        if start == ts_start(app_span(appointment)):
            cal_day.appointments.remove(appointment)




def test_labc():
    create("Jayne")
    book("Jayne", 20, "sep", "12:00", "14:00", "Rob train")
    book("Jayne", 20, "sep", "15:00", "16:00", "Escape with loot")
    show("Jayne", 20, "sep")
    remove("Jayne", 20, "sep", "15:00")
    show("Jayne", 20, "sep")

test_labc()