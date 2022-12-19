# Write your code for lab 8d here.
from cal_abstraction import *
from cal_booking import *
from cal_ui import *
from settings import CHECK_AGAINST_FACIT

if CHECK_AGAINST_FACIT:
    try:
        from facit_la8_uppg import TimeSpanSeq
    except:
        print("*" * 100)
        print("*" * 100)
        print("Kan inte hitta facit; ändra CHECK_AGAINST_FACIT i test_driver.py till False")
        print("*" * 100)
        print("*" * 100)
        raise
else:
    from lab8b import *


def free_spans(cal_name, day, month, start: Time, end: Time) -> TimeSpanSeq:
    start = new_time_from_string(start)
    end = new_time_from_string(end)
    ts = new_time_span(start, end)
    day = new_day(day)
    mon = new_month(month)
    cal_year = get_calendar(cal_name) #gets the year
    cal_month = cy_get_month(mon, cal_year) # gets the month
    cal_day = cm_get_day(cal_month, day) # get the date 
    print(cal_day)

    if is_booked_during(cal_day, ts) == False:
        print(ts)
    else: # check for the first appointment of the day see start and go from "start" to that start and repeat at the end
        for app in cd_iter_appointments(cal_day):
            print(app[0])

create("Jayne")
book("Jayne", 20, "sep", "15:00", "16:00", "Escape with loot")
free_spans("Jayne", 20, "sep", "08:00", "19:00")