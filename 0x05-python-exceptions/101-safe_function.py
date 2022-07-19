#!/usr/bin/python3
def safe_function(fct, *args):
    try:
        return fct(*args)
    except Exception as err:
        import sys
        sys.stderr.write(f"Exception: {err}\n")
        return None
