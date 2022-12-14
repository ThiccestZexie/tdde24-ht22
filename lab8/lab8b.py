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
    """ Create and return a list of Timespans """

    if TimeSpans is None:
        TimeSpans = []

    else:
        ensure_type(TimeSpans, List[TimeSpan])

    return TimeSpanSeq(TimeSpans)

def tss_timespans(tss):
    return tss.TimeSpans

def tss_is_empty(tss):
    """Return true iff the given TimeSpanSeq has no TimeSpans."""
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
        if not ts_list or time_precedes(
                ts_start(ts), ts_start(ts_list[0])
        ):
            return [ts] + ts_list
        else:
            return [ts_list[0]] + add_ts(ts, ts_list[1:])

    return new_time_span_seq(add_ts(ts, tss_timespans(tss)))


def tss_iter_spans(tss):
    """To be used as `for TimeSpan in tss_iter_spans(tss)"""
    ensure_type(tss, TimeSpanSeq)

    for TimeSpan in tss_timespans(tss):
        yield TimeSpan


def show_time_spans(tss):
    """ Prints a list of the TimeSpans in the given TimeSpanSeq """
    ensure_type(tss, TimeSpanSeq)

    for TimeSpan in tss_iter_spans(tss):
        show_ts(TimeSpan)
        print(' ')


def tss_sort_spans(tss):
    ensure_type(tss, TimeSpanSeq)

    copy_tss = tss_timespans(tss).copy()

    new_tss = []

    for i in range(len(copy_tss)):
        ts = copy_tss.pop()

        if new_tss == []:
            new_tss.append(ts)

        elif (hour_number(time_hour(ts_start(ts))) <= hour_number(time_hour(ts_start(new_tss[i-1])))):
            new_tss.insert(i, ts)

        else:
            new_tss.append(ts)


    return TimeSpanSeq(new_tss)
    


# Keep only time spans that satisfy pred.
# You do not need to modify this function.
def tss_keep_spans(tss, pred):
    result = new_time_span_seq()
    for span in tss_iter_spans(tss):
        if pred(span):
            result = tss_plus_span(result, span)

    return result




"""
t_start = new_time(new_hour(12),new_minute(0))
t_end = new_time(new_hour(13),new_minute(0))
ts_1 = new_time_span(t_start, t_end)

t_start = new_time(new_hour(11),new_minute(0))
t_end = new_time(new_hour(17),new_minute(0))
ts_2 = new_time_span(t_start, t_end)

t_start = new_time(new_hour(13),new_minute(0))
t_end = new_time(new_hour(16),new_minute(0))
ts_3 = new_time_span(t_start, t_end)

first_tss = new_time_span_seq([ts_3,ts_1])

first_tss = tss_plus_span(first_tss,ts_2)

tss_iter_spans(first_tss)

show_time_spans(first_tss)

empty_tss = new_time_span_seq()
print(tss_is_empty(empty_tss))
"""