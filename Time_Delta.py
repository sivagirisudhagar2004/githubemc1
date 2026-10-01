from datetime import datetime

t = int(input("Number of test cases: "))
for _ in range(t):
    t1_str = input("Enter first timestamp(Day dd MMM YYYY HH:MM:SS +/-XXXX): ") # timezone offset in hours and minutes _+0530 or -0700
    t2_str = input("Enter second timestamp(Day dd MMM YYYY HH:MM:SS +/-XXXX): ")  # timezone offset in hours and minutes +0530 or -0700

    fmt = "%a %d %b %Y %H:%M:%S"
    
    t1_part = t1_str.rsplit(' ',1)
    t2_part = t2_str.rsplit(' ',1)