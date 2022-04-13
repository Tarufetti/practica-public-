def time_calculator(start, duration, day='none'):


    days={'monday':1,'tuesday':2,'wednesday':3,'thursday':4,'friday':5,'saturday':6,'sunday':7}
    days_backwards={1:'monday',2:'tuesday',3:'wednesday',4:'thursday',5:'friday',6:'saturday',7:'sunday'}
    n_days_later = 0
    final_day = ''

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
            minutes = (minutes + duration_minutes)-60
            duration_minutes=0
        else:
            minutes = minutes + duration_minutes
            duration_minutes=0
        starting_hour += duration_hour
        duration_hour=0
        if starting_hour >= 12:
                am_pm = 'PM'
        if starting_hour >= 13:
            starting_hour = starting_hour-12

    if am_pm == 'PM':
        if minutes + duration_minutes >= 60:
            starting_hour += 1
            minutes = (minutes + duration_minutes)-60
            duration_minutes=0
        else:
            minutes = minutes + duration_minutes
            duration_minutes=0
        starting_hour += duration_hour
        duration_hour=0  
        if starting_hour >= 12:
            am_pm = 'AM' 
            n_days_later +=1  
        if starting_hour >= 13:
            starting_hour = starting_hour-12
    if am_pm == 'AM':
        if starting_hour > 12:
                am_pm = 'PM'
        if starting_hour >= 13:
            starting_hour = starting_hour-12







    if day in days:
        if days[day] + n_days_later > 7:
            final_day = days_backwards[((days[day]+n_days_later)-7)]
        else:
            final_day = days_backwards[(days[day]+n_days_later)]


    return starting_hour, minutes, am_pm, final_day, n_days_later
print (time_calculator('11:21 AM', '00:40', 'monday'))
