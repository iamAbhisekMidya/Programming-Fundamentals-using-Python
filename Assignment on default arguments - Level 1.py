'''Consider sample data as follows: sample_data=range(1,11)

Create two functions: odd() and even()
The function even() returns a list of all the even numbers from sample_data
The function odd() returns a list of all the odd numbers from sample_data

Create a function sum_of_numbers() which will accept the sample data and/or a function.
If a function is not passed, the sum_of_numbers() should return the sum of all the numbers from sample_data
If a function is passed, the sum_of_numbers() should return the sum of numbers returned from the function passed.
'''

def sum_of_numbers(list_of_num,filter_func=None):
    if filter_func is not None:
       list_of_num=filter_func(list_of_num)
    s=sum(list_of_num)
    return s

def even(data):
    lst= list(filter(lambda x: x%2==0,data))
    return lst

def odd(data):
    lst= list(filter(lambda x: x%2!=0,data))
    return lst

sample_data = range(1,11)
print(sum_of_numbers(sample_data,None))
