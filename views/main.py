def dec_with_args(multiplier):
    def decorator(func):

        def wrapper(*args, **kwargs):
            print('До выполнеия функции')
            result = func(*args, **kwargs)
            print('После выполнения функции')
            return result * multiplier

        return wrapper
    return decorator


@dec_with_args(3)
def func_one(arg1, arg2):
    return arg1 + arg2

print(func_one(1, 2))

