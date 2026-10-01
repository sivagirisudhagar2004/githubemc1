from datetime import datetime

t = int(input("Number of test cases: "))
for _ in range(t):
    t1_str = input("Enter first timestamp(Day dd MMM YYYY HH:MM:SS +/-XXXX): ") # timezone offset in hours and minutes _+0530 or -0700
    t2_str = input("Enter second timestamp(Day dd MMM YYYY HH:MM:SS +/-XXXX): ")  # timezone offset in hours and minutes +0530 or -0700

    fmt = "%a %d %b %Y %H:%M:%S"
    
    t1_part = t1_str.rsplit(' ',1)
    t2_part = t2_str.rsplit(' ',1)

    t1 = datetime.strptime(t1_part[0],fmt)
    t2 = datetime.strptime(t2_part[0],fmt)

    def parse_timezone(tz_str):
        sign = 1 if tz_str[0] == '+' else -1
        tz_str= tz_str[1:]
        if ':'in tz_str:
            hours,minutes = map(int,tz_str.split(':'))
        else:
            hours = int(tz_str[:2])
            minutes = int(tz_str[2:])
        return sign * (hours*3600 + minutes*60)
    
    tz1_offset = parse_timezone(t1_part[1])
    tz2_offset = parse_timezone(t2_part[1])
    
    t1_seconds = t1.timestamp()- tz1_offset
    t2_seconds = t2.timestamp() - tz2_offset
     
    diff = abs(t1_seconds - t2_seconds)
    
    print(int(diff))
        