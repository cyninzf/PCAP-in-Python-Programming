# PE2
# 4.5.1.3 The datetime module

from datetime import date
import time

timestamp = time.time()
print ("Timestamp:", timestamp)
"""The timestamp is actually the difference between a particular date
(including time) and January 1, 1970, 00:00:00 (UTC), expressed in seconds."""

d = date.fromtimestamp(timestamp)
print("Date:", d)
print()

# replace

d = date(1991, 2, 5)
print(d)

d = d.replace(year=1992, month=1, day=16)
print(d)
