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
    """ Prints the free time in a given day using other functions """

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
    """ Returns a TimeSpanSeq of the free time in a given cal_day between start and end """

    if time_equals(end, start):
        print('start and end time is the same, there is no time to print')
        return new_time_span_seq()

    elif not cal_day.appointments:
        return new_time_span_seq([new_time_span(start,end)])

    else: # check for the first appointment of the day see start and go from "start" to that start and repeat at the end
        ts_list = [app_span(app) for app in cd_iter_appointments(cal_day)]
        ts_list = refine_list(ts_list, start, end)
        
        return free_tss(start, end, ts_list)


def free_tss(start: Time, end: Time, ts_list: List[TimeSpan], tss: TimeSpanSeq = None) -> TimeSpanSeq:
    """ Creates a TimeSpanSeq with all the free time between start and end """

    if tss == None:
        tss = new_time_span_seq()

    if ts_list == []:
        if not time_equals(start, end):
            tss = tss_plus_span(tss, new_time_span(start, end))
        return tss

    if time_precedes(start, ts_start(ts_list[0])):
        tss = tss_plus_span(tss, new_time_span(start, ts_start(ts_list[0])))

    return free_tss(ts_end(ts_list[0]), end, ts_list[1:], tss)


def refine_list(ts_list: List[TimeSpan], start: Time, end: Time) -> List[TimeSpan]:
    """ Creates a new list from the given ts_list so that all the times are within the start and end """

    new_ts_list = []

    for ts in ts_list:
        if time_precedes_or_equals(start, ts_start(ts)) and time_precedes_or_equals(ts_end(ts), end):
            new_ts_list.append(ts)

        elif time_precedes(ts_start(ts), start) and time_precedes(end, ts_end(ts)):
            new_ts_list.append(new_time_span(start, end))

        elif time_precedes(ts_start(ts), start) and time_precedes(start, ts_end(ts)):
            new_ts_list.append(new_time_span(start, ts_end(ts)))

        elif time_precedes(ts_start(ts), end) and time_precedes(end, ts_end(ts)):
            new_ts_list.append(new_time_span(ts_start(ts), end))

    return new_ts_list


if __name__ == "__main__":
    create("Andreas")
    book("Andreas", 26, "sep", "08:00", "15:00", "School")
    book("Andreas", 26, "sep", "17:00", "21:00", "Birthday party")
    show_free("Andreas", 26, "sep", "00:00", "23:00")