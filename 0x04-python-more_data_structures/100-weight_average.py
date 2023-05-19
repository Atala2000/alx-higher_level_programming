#!/usr/bin/python3
def weight_average(my_list=[]):
    average = 0
    tWeight = 0
    tScore = 0
    if (len(my_list) <= 0):
        return (0)
    for item in my_list:
        score, weight = item
        tWeight += weight
        tScore += score * weight
    return tScore / tWeight
