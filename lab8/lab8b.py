from cal_abstraction import *
from cal_output import *

# =========================================================================
# Type definition
# =========================================================================

# Define the type somehow...  The initial "" is simply here as a placeholder.
TimeSpanSeq = NamedTuple(
    "TimeSpanSeq", [("TimeSpans", List[TimeSpan])]
)

# =========================================================================
#  Function implementations
# =========================================================================

# Implement these functions!  Also determine if you need *additional* functions.

def new_time_span_seq(TimeSpans: List[TimeSpan] = None) -> TimeSpanSeq:
    """ Create and return a sorted TimeSpanSeq out of a list of Timespans """

    if TimeSpans is None:
        tss = TimeSpanSeq([])

    else:
        ensure_type(TimeSpans, List[TimeSpan])

        tss = TimeSpanSeq([TimeSpans[0]])
        
        for ts in TimeSpans[1:]:
            tss = tss_plus_span(tss, ts)

    return tss


def tss_timespans(tss: TimeSpanSeq) -> list[TimeSpan]:
    return tss.TimeSpans


def tss_is_empty(tss: TimeSpanSeq) -> bool:
    """ Return true if the given TimeSpanSeq has no TimeSpans. """
    ensure_type(tss, TimeSpanSeq)
    return not tss_timespans(tss)


def tss_plus_span(tss: TimeSpanSeq, ts: TimeSpan) -> TimeSpanSeq:
    """
    Returns a copy of the given TimeSpanSeq, where the given TimeSpan
    has been added in its proper position.
    """
    ensure_type(tss, TimeSpanSeq)
    ensure_type(ts, TimeSpan)

    def add_ts(ts: TimeSpan, ts_list: list[TimeSpan]):
        ensure_type(ts, TimeSpan)
        ensure_type(ts_list, list[TimeSpan])
        if not ts_list or time_precedes(
                ts_start(ts), ts_start(ts_list[0])
        ):
            return [ts] + ts_list
        else:
            return [ts_list[0]] + add_ts(ts, ts_list[1:])

    return TimeSpanSeq(add_ts(ts, tss_timespans(tss)))


def tss_iter_spans(tss: TimeSpanSeq) -> TimeSpan:
    """To be used as `for TimeSpan in tss_iter_spans(tss)"""
    ensure_type(tss, TimeSpanSeq)

    for TimeSpan in tss_timespans(tss):
        yield TimeSpan


def show_time_spans(tss: TimeSpanSeq) -> None:
    """ Prints a list of the TimeSpans in the given TimeSpanSeq """
    ensure_type(tss, TimeSpanSeq)

    for TimeSpan in tss_iter_spans(tss):
        show_ts(TimeSpan)
        print(' ')
    

# Keep only time spans that satisfy pred.
# You do not need to modify this function.
def tss_keep_spans(tss, pred):
    result = new_time_span_seq()
    for span in tss_iter_spans(tss):
        if pred(span):
            result = tss_plus_span(result, span)

    return result


def test_8b_sorting():
    """ Tests if new TimeSpanSeq are sorted correctly """
    t_start = new_time(new_hour(12),new_minute(0))
    t_end = new_time(new_hour(13),new_minute(0))
    ts_1 = new_time_span(t_start, t_end)

    t_start = new_time(new_hour(11),new_minute(0))
    t_end = new_time(new_hour(17),new_minute(0))
    ts_2 = new_time_span(t_start, t_end)

    t_start = new_time(new_hour(13),new_minute(0))
    t_end = new_time(new_hour(16),new_minute(0))
    ts_3 = new_time_span(t_start, t_end)

    tss_1 = new_time_span_seq([ts_3,ts_1,ts_2])

    tss_2 = new_time_span_seq([ts_1,ts_2,ts_3])

    assert tss_1 == tss_2


def test_8b_empty():
    """ Tests if tss_is_empty returns the correct values """
    empty_tss = new_time_span_seq()

    assert tss_is_empty(empty_tss) == True


    t_start = new_time(new_hour(12),new_minute(0))
    t_end = new_time(new_hour(13),new_minute(0))
    ts_1 = new_time_span(t_start, t_end)

    not_empty_tss = new_time_span_seq([ts_1])

    assert tss_is_empty(not_empty_tss) == False


def test_8b_show():
    """ Tests the show function, if it prints a list of timespans it works """
    t_start = new_time(new_hour(12),new_minute(0))
    t_end = new_time(new_hour(13),new_minute(0))
    ts_1 = new_time_span(t_start, t_end)

    t_start = new_time(new_hour(11),new_minute(0))
    t_end = new_time(new_hour(17),new_minute(0))
    ts_2 = new_time_span(t_start, t_end)

    t_start = new_time(new_hour(13),new_minute(0))
    t_end = new_time(new_hour(16),new_minute(0))
    ts_3 = new_time_span(t_start, t_end)

    tss_1 = new_time_span_seq([ts_3,ts_1,ts_2])

    show_time_spans(tss_1)


def test_8b():
    test_8b_sorting()
    test_8b_empty()
    test_8b_show()
    print('all tests passed :)')

if __name__ == "__main__":
    test_8b()