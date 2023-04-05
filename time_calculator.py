def add_time(starter, duration, day = None):

    # first given time
    starter= starter.split()
    starter_hour, starter_min = starter[0].split(':')[0], starter[0].split(':')[1]
    half = starter[1]
    if half == 'PM' and starter_hour != 12:
        starter_hour = int(starter_hour) + 12

    # second given time
    duration = duration.split(':')
    duration_hour, duration_min = duration[0], duration[1]


    # calculate the final minutes
    final_min = (int(starter_min) + int(duration_min)) % 60
    if len(str(final_min)) == 1:
        final_min = '0' + str(final_min)
    box = (int(starter_min) + int(duration_min)) // 60

    # calculate the final hours
    final_hour = (int(starter_hour) + int (duration_hour) + box) % 24

    # configure the final time with the AMs & PMs
    if final_hour == 0:
        final_hour = 12
        half = 'AM'

    elif final_hour == 12:
        half = 'PM'

    elif final_hour < 12:
        half = 'AM'
    else:
        final_hour -= 12
        half = 'PM'

    # counting the duration of the overall time on days
    final_day_count = (int(starter_hour) + int(duration_hour) + box) // 24

    # config the sufix
    if final_day_count == 0:
        day_declaration = ''
    elif final_day_count == 1:
        day_declaration = ' (next day)'
    else:
        day_declaration = f' ({final_day_count} days later)'

    # pinpoint the day on wich the resulting hour will take place
    if day != None:
        day = day.capitalize().strip()
        week_days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
        day_indx = week_days.index(day)
        final_day_indx = (day_indx + final_day_count) % 7
        final_day = f', {week_days[final_day_indx]}'

    else:
        final_day = ''

    # return the result
    return f'{final_hour}:{final_min} {half}{final_day}{day_declaration}'
