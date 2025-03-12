# ############################### EXAMPLE ###############################

# Decorator function
import time


def my_decorator(func):

  def my_wrapper():
    print("Method started working")
    func()
    print("Method work completed")

  return my_wrapper


# Apply decorator on the function
@my_decorator
def greetings():
  print("Anaivarukkum Vanakkam")


# greetings()


# ############################### LOG DECORATOR ###############################

def log_decorator(func):

  def wrapper(*args, **kwargs):
    print(f"{func.__name__} is called with args: {args} , kwargs: {kwargs}")
    result = func(*args, **kwargs)
    print(f"{func.__name__} returned result : {result}")

    return result
  
  return wrapper

@log_decorator
def calculate_product(*nums):
  product = 1
  for num in nums:
    product *= num
  
  return product


# print(f"result of product(2, 3, 4, 5) : {calculate_product(2, 3, 4, 5)}")


# ############################### MEASURE TIME DECORATOR ###############################

def measure_performance_time(func):

  def wrapper(*args, **kwargs):
    start = time.time()
    result = func(*args, **kwargs)
    end = time.time()
    duration = end - start

    print(f"Function {func.__name__} takes {duration:.3f} seconds")
    return result
  
  return wrapper


@measure_performance_time
def caluculate_sum(nums):
  sum = 0
  for num in nums:
    sum += num

  return sum


# print(f"result of sum(2, 3, 4, 5) : {caluculate_sum([i for i in range(0,1_00_000)])}")


# ############################### CONVERT DATA TYPE DECORATOR ###############################

def convert_to_data_type(target_type):
    def type_converter_decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return target_type(result)
        return wrapper
    return type_converter_decorator

@convert_to_data_type(int)
def add_values(a, b):
    return a + b

int_result = add_values(10, 20)
print("Result:", int_result, type(int_result))

@convert_to_data_type(str)
def concatenate_strings(str1, str2):
    return str1 + str2

str_result = concatenate_strings("Python", " Decorator")
print("Result:", str_result, type(str_result))
  
