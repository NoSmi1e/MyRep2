def add_query_string(url, query):
    if not query:
        return url
    parameters = '&'.join(f'{key}={value}' for key, value in query.items())
    return f'{url}?{parameters}'
