#!/usr/bin/python3
def safe_function(fct, *args):
    import sys

    try:
        result = fct(args[0], args[1])
        return result
    except (TypeError, ValueError):
        print("Exception: wrong type", file=sys.stderr)
    except IndexError:
        print("Exception: list index out of range", file=sys.stderr)
    except ZeroDivisionError:
        print("Exception: division by zero", file=sys.stderr)
    return None
