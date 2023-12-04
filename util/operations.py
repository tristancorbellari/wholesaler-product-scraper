def end_of_url(url):
    '''Used to get the last part of a url, i.e. everything after the last "/"'''
    return url[(url.rfind("/") + 1) :]
