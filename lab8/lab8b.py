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

    return tss_sort_spans(TimeSpanSeq(TimeSpans))


def tss_is_empty(tss):
    if tss == []:
        return False

    else:
        return True


def tss_plus_span(tss, ts):
    ensure_type(tss, TimeSpanSeq)
    ensure_type(ts, TimeSpan)

    tss.TimeSpans.append(ts)

    return tss_sort_spans(tss)


def tss_iter_spans(tss):

    ensure_type(tss, TimeSpanSeq)

    for TimeSpan in tss.TimeSpans:
        yield TimeSpan


def show_time_spans(tss):
    ensure_type(tss, TimeSpanSeq)

    for TimeSpan in tss.TimeSpans:
        show_ts(TimeSpan)


def tss_sort_spans(tss):
    """TODO fundamentally wrong, currently duplicates TimeSpan if only one is given"""
    ensure_type(tss, TimeSpanSeq)

    new_tss = []

    for TimeSpan in tss.TimeSpans:
        if new_tss == []:
            new_tss.append(TimeSpan)
        for i in range(len(new_tss)):
            if hour_number(time_hour(ts_start(TimeSpan))) <= hour_number(time_hour(ts_start(new_tss[i]))):
                new_tss.insert(i, TimeSpan)
                break

            else:
                new_tss.append(TimeSpan)
                break


    return TimeSpanSeq(new_tss)
    


# Keep only time spans that satisfy pred.
# You do not need to modify this function.
def tss_keep_spans(tss, pred):
    result = new_time_span_seq()
    for span in tss_iter_spans(tss):
        if pred(span):
            result = tss_plus_span(result, span)

    return result





t_start = new_time(new_hour(12),new_minute(0))
t_end = new_time(new_hour(13),new_minute(0))
ts_1 = new_time_span(t_start, t_end)

t_start_2 = new_time(new_hour(11),new_minute(0))
t_end_2 = new_time(new_hour(17),new_minute(0))
ts_2 = new_time_span(t_start_2, t_end_2)

first_tss = new_time_span_seq([ts_2])

print(first_tss)
tss_plus_span(first_tss,ts_1)

tss_iter_spans(first_tss)

tss_sort_spans(first_tss)

#show_time_spans(first_tss)