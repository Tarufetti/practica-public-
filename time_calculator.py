
STRINGS DO NOT CHANGE!!!



def time_calculator(start, duration, day='none'):

    start = '12:00 PM'
    duration = '5:00'
    day=['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    n_days_later = 0

    starting_hour= int(start[0:2])
    minutes=int(start[3:5])
    am_pm= start[6:]

    duration_colon = duration.find(':')
    duration_hour = int(duration[:duration_colon])
    duration_minutes = int(duration[duration_colon+1:])

    if duration_hour >=24:
        n_days_later += int(duration_hour/24)
        duration_hour = duration_hour%24
            

    if am_pm == 'AM':
        if minutes + duration_minutes >= 60:
            starting_hour += 1
            minutes = (minutes + duration_minutes) -60
            if starting_hour == 13:
                starting_hour = 1
                am_pm = 'PM'
        else:
            minutes = minutes + duration_minutes
    
    return duration_hour
print (time_calculator('12:00 AM', '24:00'))
        
