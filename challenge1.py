def converting_to_24hr_time(hour,min,period):
    if 1<=hour<=12 and 0<=min<=59 and period =="AM":
        hour_in_24hr_system =0

    elif 1<=hour<=12 and 0<=min<=59 and period=="PM":
            hour_in_24hr_system = hour+12

    else:return "key in the time correctly so that it can be converted to 24hr clock system"    

    return f"{hour_in_24hr_system:02d}{min:02d}hours"

print(converting_to_24hr_time(1,40,"AM"))