#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    average = 0
    divisor = 0
    for number in my_list:
        average += number[0] * number[1]
        divisor += number[1]
    return float(average / divisor)
