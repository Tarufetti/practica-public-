def time_calculator(start, duration, day='none'):


    day=['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    n_days_later = 0

    starting_colon = start.find(':')
    starting_hour= int(start[:starting_colon])
    minutes=int(start[starting_colon+1:starting_colon+3])
    am_pm= start[starting_colon+4:]

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
    
    return n_days_later
print (time_calculator('1:00 PM', '24:00'))
        
