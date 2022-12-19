# Write your code for lab 8C (remove) here.
from cal_abstraction import *
from cal_ui import *

def remove(cal_name: str, day: int, month: str, start: str) -> None:
    day = new_day(day)
    mon = new_month(month)
    start = new_time_from_string(start)
<<<<<<< HEAD
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
 
=======
    cal_year = get_calendar(cal_name)

    new_date(day, mon)

    if 'the time doesnt exist' and False:
        1
    else:
        # Get a new CalendarYear with the new appointment...
        new_year = minus_appointment(cal_year, day, mon, start)
        # ...and let the calendar name refer to this CalendarYear instead.
        if new_year == None:
            print('There is no appointment to remove at that time')

        else:
            insert_calendar(cal_name, new_year)
            print("The appointment has been removed.")
    

def minus_appointment(
    cal_year: CalendarYear,
    day: Day,
    mon: Month,
    start: Time
) -> CalendarYear:
    """
    Return a new CalendarYear where an appointment, specified by the parameters,
    has been removed in the appropriate CalendarDay.

    This is a helper function using our internal data types.  See also the remove()
    function in lab8c.py, which provides an external user interface to be called
    by users.
    """

    # removes an appointment by taking apart a calendar year, removing the
    # appointment in the correct calendar day, and then putting it back together.

    # This function does not modify any structures, but rather builds a new one.
    # The new calendar year generated by minus_appointment should then be used
    # by the caller to replace the old calendar year.

    old_cal_month = cy_get_month(mon, cal_year)
    old_cal_day = cm_get_day(old_cal_month, day)

    for appointment in cd_iter_appointments(old_cal_day):
        if start == ts_start(app_span(appointment)):
            new_cal_day = cd_minus_appointment(old_cal_day, appointment)
            new_cal_month = cm_plus_cd(old_cal_month, new_cal_day)
            new_cal_year = cy_plus_cm(cal_year, new_cal_month)
            return new_cal_year


def cd_minus_appointment(cal_day: CalendarDay, appointment: Appointment) -> CalendarDay:
    """
    Returns a copy of the given CalendarDay, where the given Appointment
    has been removed.
    """
    ensure_type(appointment, Appointment)
    ensure_type(cal_day, CalendarDay)

    def remove_appointment(app: Appointment, appointments: List[Appointment]):
        new_appointments = appointments.copy()
        new_appointments.remove(app)
        return new_appointments

>>>>>>> 077da47ea01be90787ff92d96010ad35a5ffdcb1

    return new_calendar_day(
        cd_day(cal_day), remove_appointment(appointment, cal_day.appointments)
    )

            
def test_labc():
    create("Jayne")
    create("Jayne")
    book("Jayne", 20, "sep", "12:00", "14:00", "Rob train")
    book("Jayne", 20, "sep", "15:00", "16:00", "Escape with loot")
    show("Jayne", 20, "sep")
    remove("Jayne", 20, "sep", "15:00")
    show("Jayne", 20, "sep")

test_labc()