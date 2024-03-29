# https://www.dailyfx.com/education/candlestick-patterns/inverted-hammer.html
def candle_382(hp, lp, op, cp, date, percentage=0.382):
    hp, lp, op, cp = float(hp), float(lp), float(op), float(cp)
    # green candle
    gc_frl = hp - ((hp - lp) * percentage)
    # red candle
    rc_frl = hp + ((hp - lp) * percentage)
    if op > cp:
        if op > gc_frl:
            return f"Buying pressure on {date}."
    elif op < cp:
        if op < rc_frl:
            return f"Selling pressure on {date}."
    # no pattern
    return f"No 38.2% Candlstick Pattern on {date}."
