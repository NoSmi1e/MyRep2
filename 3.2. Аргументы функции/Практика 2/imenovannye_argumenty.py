def info_kwargs(**kwargs):
    for name in sorted(kwargs):
        print(f'{name}: {kwargs[name]}')
