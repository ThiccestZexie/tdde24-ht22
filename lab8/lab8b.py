from cal_abstraction import *

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


def tss_is_empty(tss):
    pass


def tss_plus_span(tss, ts):
    pass


def tss_iter_spans(tss):
    pass


def show_time_spans(tss):
    pass


# Keep only time spans that satisfy pred.
# You do not need to modify this function.
def tss_keep_spans(tss, pred):
    result = new_time_span_seq()
    for span in tss_iter_spans(tss):
        if pred(span):
            result = tss_plus_span(result, span)

    return result
