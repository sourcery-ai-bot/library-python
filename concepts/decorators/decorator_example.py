#  Source: https://www.youtube.com/watch?v=FsAPt_9Bf3U

def decorator_function(original_function):
    def wrapper_function():
        return original_function()
    return wrapper_function


def display():
    print('Display function ran')

decorated_display = decorator_function(display)

decorated_display()
