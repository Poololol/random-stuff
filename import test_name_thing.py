import test_name_thing
import inspect
black = test_name_thing.black
def retrieve_name(var):
    callers_local_vars = inspect.currentframe().f_back.f_locals.items()
    print(inspect.currentframe())
    return [var_name for var_name, var_val in callers_local_vars if var_val is var]
print(f'{retrieve_name(black)[0]}: {black}')