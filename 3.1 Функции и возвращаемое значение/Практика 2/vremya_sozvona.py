def print_perm_time_call(msc_time):
    hours = int(msc_time[:2]) + 2
    minutes = msc_time[3:]

    if hours < 10:
        print(f'Созвон будет в 0{hours}:{minutes}.')
    else:
        print(f'Созвон будет в {hours}:{minutes}.')
