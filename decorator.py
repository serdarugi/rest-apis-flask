from functools import wraps 

def prefix_decorator(prefix):
    def decorator_function(original_function):
        @wraps(original_function)
        def wrapper(*args,**kwargs):
            print(f"{prefix}, Executed before, {original_function.__name__}")
            result = original_function(*args,**kwargs)
            print(f'{prefix}, Executed after, {original_function.__name__}')
            return result
        return wrapper
    return decorator_function


@prefix_decorator('LOG:')
def display_info(name,age):
    print(f'{name} and {age}')

display_info('Serdar', 31)