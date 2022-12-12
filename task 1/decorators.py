def my_decorator(func):
    def wrapper(arg1, arg2):
        print('Название {} => {}'.format(arg1, arg2)) if func(arg1, arg2) \
            else print('Название {} < {}'.format(arg2, arg1))
    return wrapper


