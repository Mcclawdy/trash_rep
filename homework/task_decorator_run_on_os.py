import platform


os = False
 
 
def run_on_linux(func):
    def wrapper(*args, **kwargs):
        global os
        if not os:
            if platform.system() == 'Linux':
                os = True
                return func(*args, **kwargs)
            else:
                return None
        else:
            return func(*args, **kwargs)
    return wrapper


def run_on_macos(func):
    def wrapper(*args, **kwargs):
        global os
        if not os:
            if platform.system() == 'Darwin':
                os = True
                return func(*args, **kwargs)
            else:
                return None
        else:
            return func(*args, **kwargs)
    return wrapper
    

def run_on_windows(func):
    def wrapper(*args, **kwargs):
        global os
        if not os:
            if platform.system() == 'Windows':
                os = True
                return func(*args, **kwargs)
            else:
                return None
        else:
            return func(*args, **kwargs)
    return wrapper