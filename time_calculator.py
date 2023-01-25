def add_time(start, duration, day='none'):


    days={'Monday':1,'Tuesday':2,'Wednesday':3,'Thursday':4,'Friday':5,'Saturday':6,'Sunday':7}
    days_index={1:'Monday',2:'Tuesday',3:'Wednesday',4:'Thursday',5:'Friday',6:'Saturday',7:'Sunday'}
    n_days_later = 0
    final_day = ''

    #Get the data from starting hour and separate values from the colon.
    starting_colon = start.find(':')
    starting_hour= int(start[:starting_colon])
    minutes=int(start[starting_colon+1:starting_colon+3])
    am_pm= start[starting_colon+4:]

    #Get data from the duration parameter.
    duration_colon = duration.find(':')
    duration_hour = int(duration[:duration_colon])
    duration_minutes = int(duration[duration_colon+1:])

    # Turn minutes into hours and add minutes to final minutes.
    if duration_minutes + minutes >= 60:
        duration_hour += 1
        minutes = duration_minutes + minutes - 60
    else:
        minutes += duration_minutes
    #Calculate how many days have passed and get final hour.
    total_hour = starting_hour + duration_hour
    if total_hour >= 24:
        n_days_later += int(duration_hour/24)
        total_hour = total_hour % 24
    if am_pm == 'PM' and total_hour >= 12:
        n_days_later += 1
        am_pm = 'AM'
        if total_hour > 12:
            total_hour = total_hour % 12
    elif am_pm == 'AM' and total_hour >= 12:
        am_pm = 'PM'
        if total_hour > 12:
            total_hour = total_hour % 12
            
    #Get minutes to ocupy 2 spaces 
    if len(str(minutes)) == 1:
        minutes= str(minutes).zfill(2)
    
    final_hour= f'{total_hour}:{minutes} {am_pm}'    

    #Returns with and without the optional day parameter.
    day = day.capitalize()
    if day in days:
        if days[day] + n_days_later > 7:
            final_day = days_index[((days[day]+n_days_later)-7)]
        else:
            final_day = days_index[(days[day]+n_days_later)]
        if n_days_later == 0:
            return f'{final_hour}, {final_day}'
        elif n_days_later == 1:
            return f'{final_hour}, {final_day} (next day)'
        elif n_days_later > 1:
            return f'{final_hour}, {final_day} ({n_days_later} days later)'
    else:
        if n_days_later == 0:
            return f'{final_hour}'
        elif n_days_later == 1:
            return f'{final_hour} (next day)'
        elif n_days_later > 1:
            return f'{final_hour} ({n_days_later} days later)'
