#Find the nearest value to the given one.

#You are given a list of values as set form and a value for which you need to find the nearest one.

#For example, we have the following set of numbers: 4, 7, 10, 11, 12, 17, and we need to find the nearest value to the number 9. 
#If we sort this set in the ascending order, then to the left of number 9 will be number 7 and to the right - will be number 10. But 10 is closer than 7, which means that the correct answer is 10.


def nearest_value(values: set, one: int) -> int:
#find if one is in the value
    if one in values:
        return one

    else:
        #abs absolute value to find the distance from one: int
        #create a list of tuples (abs(x+one),x)
        #min returns the tuple with the lowest 
        #index [1] returns the num in values
        return min((abs(x-one), x) for x in values)[1]
