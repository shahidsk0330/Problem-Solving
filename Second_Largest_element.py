"""
Second Largest Element in an Array
"""
l = [10,8,5,7,6,4,100,4,89,90,5]

"""
Description:
is array sorted? No
Assumed largest and second largest number with index 0 value.
Compared each every element.
Time complexity: O(N)
"""

def second_largest_element(l):
    largest = l[0]
    second_lar = l[0]
    for i in range(1,len(l)):
        if(l[i] > largest):
            second_lar = largest
            largest = l[i]
        elif(l[i] > second_lar):
            second_lar = l[i]
    return second_lar

print("The second largest element in an array {}".format(second_largest_element(l)))
        


