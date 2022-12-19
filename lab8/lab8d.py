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

def show_free(cal_name, day, month, start: Time, end: Time) -> None:
    start = new_time_from_string(start)
    end = new_time_from_string(end)
    day = new_day(day)
    mon = new_month(month)
    cal_year = get_calendar(cal_name) #gets the year
    cal_month = cy_get_month(mon, cal_year) # gets the month
    cal_day = cm_get_day(cal_month, day) # get the date 


    free_tss = free_spans(cal_day, start, end)
    show_time_spans(free_tss)

def free_spans(cal_day: CalendarDay, start: Time, end: Time) -> TimeSpanSeq:

    if start == end:
        print('start and end are the same')

    else: # check for the first appointment of the day see start and go from "start" to that start and repeat at the end
        ts_list = [app_span(app) for app in cd_iter_appointments(cal_day)]
        ts_list = refine_list(ts_list, start, end)
        return check_free(start, end, ts_list)



def check_free(start, end, ts_list, tss = None):
    if ts_list == []:
        tss = tss_plus_span(tss, new_time_span(start, end))
        return tss

    if tss == None:
        tss = new_time_span_seq()

    if time_precedes(start, ts_start(ts_list[0])):
        tss = tss_plus_span(tss, new_time_span(start, ts_start(ts_list[0])))

    return check_free(ts_end(ts_list[0]), end, ts_list[1:], tss)


def refine_list(ts_list, start, end):
    #TODO fixa så den lägger in de korrekta tiderna
    new_ts_list = []
    for ts in ts_list:
        if time_precedes_or_equals(start, ts_start(ts)) and time_precedes_or_equals(ts_end(ts), end):
            new_ts_list.append(ts)

        elif time_precedes(ts_start(ts), start) and time_precedes(start, ts_end(ts)):
            new_ts_list.append(new_time_span(start, ts_end(ts)))

        elif time_precedes(ts_start(ts), end) and time_precedes(end, ts_end(ts)):
            new_ts_list.append(new_time_span(ts_start(ts), end))

    return new_ts_list


if __name__ == "__main__":
    create("Jayne")
    book("Jayne", 20, "sep", "15:00", "16:00", "Escape with loot")
    book("Jayne", 20, "sep", "10:00", "11:00", "Escape with loot")
    book("Jayne", 20, "sep", "18:00", "20:00", "Escape with loot")
    book("Jayne", 20, "sep", "07:00", "09:00", "Escape with loot")

    show_free("Jayne", 20, "sep", "08:00", "19:00")
