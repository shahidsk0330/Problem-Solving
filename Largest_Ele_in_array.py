"""
Largest Element in an array!
"""
l = [10,5,20,30,4,-1,80,3,2,10]
"""
question-1: Is data is sorted: no
As data is not sorted then we have to 
compare each and every element with the max element.
I will assume first element is the max element:
Time Complexity: O(N)
"""

def largest_element_in_an_array(l):
    # I have to traverse tha array
    maxelement = l[0]
    for i in range(1,len(l)):
        if(l[i] > maxelement):
            maxelement = l[i] # update element with max number.
    return maxelement
output = largest_element_in_an_array(l)
print("The max element in an array is {}".format(output))

