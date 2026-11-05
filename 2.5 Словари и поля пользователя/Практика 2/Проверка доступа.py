def is_access_allowed(ip_address, mode, ip_access_lists):
    if mode == 1:
        allowed = ip_address not in ip_access_lists['black list']
    else:
        allowed = ip_address in ip_access_lists['white list']
    return 'ДА' if allowed else 'НЕТ'
