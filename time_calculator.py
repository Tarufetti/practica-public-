def time_calculator(start, duration, day='none'):


    days={'Monday':1,'Tuesday':2,'Wednesday':3,'Thursday':4,'Friday':5,'Saturday':6,'Sunday':7}
    days_index={1:'Monday',2:'Tuesday',3:'Wednesday',4:'Thursday',5:'Friday',6:'Saturday',7:'Sunday'}
    n_days_later = 0
    final_day = ''

    starting_colon = start.find(':')
    starting_hour= int(start[:starting_colon])
    minutes=int(start[starting_colon+1:starting_colon+3])
    am_pm= start[starting_colon+4:]
    final_ampm=''

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

        if starting_hour == 24:
            starting_hour -=12
            n_days_later +=1
            final_ampm = 'AM'
        elif starting_hour > 24:
            starting_hour -=24
            n_days_later +=1
            final_ampm = 'AM'
        elif starting_hour >= 12:
                final_ampm = 'PM'
        elif starting_hour >= 13:
            starting_hour = starting_hour-12
  #EL ERROR SEGURAMENTE ESTA ACA, PERO NO LO VEO. SOLO PASA EN PM CON MAS DE 24 HORAS DE DURACION HASTA 47. SI FUNCIONA EN 36, PERO NO EN EL RESTO.
  #A PARTIR DE LOS 49 VUELVE A FUNCIONAR. 
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
        if starting_hour >=12 and starting_hour <24:
            n_days_later +=1
            final_ampm = 'AM'
            if starting_hour >= 13 and starting_hour <24:
                starting_hour = starting_hour-12
        if starting_hour == 24:
            starting_hour -=12
            final_ampm = 'PM'
        elif starting_hour >= 25:
            starting_hour -=24
            n_days_later +=1
            final_ampm = 'PM'

            
        
    
    if len(str(minutes)) == 1:
        minutes= f'0{minutes}'
    final_hour= f'{starting_hour}{start[starting_colon]}{minutes} {final_ampm}'
    print(final_hour)
    

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
        elif n_days_later > 2:
            return f'{final_hour}, {final_day} ({n_days_later} days later)'
    else:
        if n_days_later == 0:
            return f'{final_hour}'
        elif n_days_later == 1:
            return f'{final_hour} (next day)'
        elif n_days_later > 2:
            return f'{final_hour}, {final_day} ({n_days_later} days later)'

print(time_calculator('11:21 PM', '47:40', 'monday'))
