# import sys

try:
    open("database.sqlite")
except OSError:
    # raise RuntimeError("unable to handle error")
    print("Fitxer no existeix")
    raise