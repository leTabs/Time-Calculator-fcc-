def add_time(start, duration, day = ''):
    day = day.strip().lower().title()
    week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    start = start.split()
    z = start[1]
    num_of_days = 0
    arival_day = ''

    s_time = start[0].split(':')
    s_hours = s_time[0]
    s_minutes = s_time[1]

    duration = duration.split(':')
    d_hours = duration[0]
    d_minutes = duration[1]

    r_hour = int(s_hours) + int(d_hours)
    r_mins = int(s_minutes) + int(d_minutes)

    if r_mins >= 60:
        r_hour += r_mins // 60
        r_mins -= (r_mins // 60) *60


    if r_hour > 12:
        if start[1] == "PM":
            z = "AM"
            num_of_days = r_hour // 24 + 1
        else: z = "PM"
        r_hour -= 12 * (r_hour // 12)
        if r_hour == 0: r_hour = 12

    #if num_of_days == 1: num_of_days = 0
    if day != '':

        d =week_days.index(day)
        arival_day_i = d+num_of_days
        if arival_day_i > 6:
            arival_day_i -= 6 * (arival_day_i // 6)

        arival_day = week_days[arival_day_i]


    print(f'{r_hour}:{r_mins} {z} {arival_day}({num_of_days} days later)')

add_time("6:30 PM", "205:12")
