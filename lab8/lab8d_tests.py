# Write your code for lab 8d here.

from test_driver import store_test_case, run_free_spans_tests


# Create additional test cases, and add to them to create_tests_for_free_span().

def create_tests_for_free_span() -> dict:
    """Create and return a number of test cases for the free_spans function"""
    test_cases = dict()

    store_test_case(
        test_cases, #Premade test
        1,
        start_str="08:00",  # Search interval starts
        end_str="21:00",  # Search interval ends
        booking_data=["07:00-09:00", "13:00-18:00"],  # This day's appointments
        exp_result=["09:00-13:00", "18:00-21:00"],
    )  # Expected free time

    # -------- YOUR TEST CASES GO HERE -----------------------
    # For each case, add a brief description of what you want to test.

    store_test_case(
        test_cases, #Tests bookings over the start and end times
        2,
        start_str="08:00",  # Search interval starts
        end_str="19:00",  # Search interval ends
        booking_data=["07:00-09:00", "10:00-11:00", "15:00-16:00", "18:00-20:00"],  # This day's appointments
        exp_result=["09:00-10:00", "11:00-15:00", "16:00-18:00"],
    )  # Expected free time

    store_test_case(
        test_cases, #Tests empty booking
        3,
        start_str="08:00",  # Search interval starts
        end_str="19:00",  # Search interval ends
        booking_data=[],  # This day's appointments
        exp_result=["08:00-19:00"],
    )  # Expected free time

    store_test_case(
        test_cases, #Tests fully booked
        4,
        start_str="08:00",  # Search interval starts
        end_str="19:00",  # Search interval ends
        booking_data=["08:00-19:00"],  # This day's appointments
        exp_result=[],
    )  # Expected free time

    store_test_case(
        test_cases, #Tests booking before the start time
        5,
        start_str="11:00",  # Search interval starts
        end_str="19:00",  # Search interval ends
        booking_data=["08:00-10:00"],  # This day's appointments
        exp_result=["11:00-19:00"],
    )  # Expected free time

    store_test_case(
        test_cases, #Tests connected booking
        6,
        start_str="08:00",  # Search interval starts
        end_str="19:00",  # Search interval ends
        booking_data=["08:00-10:00", "10:00-12:00"],  # This day's appointments
        exp_result=["12:00-19:00"],
    )  # Expected free time

    store_test_case(
        test_cases, #Tests booking from before start time to after the end time
        7,
        start_str="08:00",  # Search interval starts
        end_str="19:00",  # Search interval ends
        booking_data=["06:00-21:00"],  # This day's appointments
        exp_result=[],
    )  # Expected free time


    print("Test cases generated.")

    return test_cases


if __name__ == '__main__':
    # Actually run the tests, using the test driver functions
    tests = create_tests_for_free_span()
    run_free_spans_tests(tests)
