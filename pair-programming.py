# TASK PROMPT: Offsets the mean of a given array to match a given value
def offsetMean(arr, target_mean):

    # calculate the current mean of the given array
    current_mean = np.mean(arr)

    # calculate the offset needed to match the target mean
    offset_value = target_mean - current_mean
    
    # offset each element in the array using vectorized operations
    offset_arr = arr + offset_value

    return offset_arr

'''
Feedback:
- The function is well-documented with clear explanations of its purpose, parameters, and return value.

Possible Improvements:
- Consider adding an example in the documentation to demonstrate usage.
- Include "import numpy as np" atop the function to ensure its functionality for users.  
'''

# This is the code I added to successfully utilize your code: 

## Example array and target mean
my_array = np.array([1, 2, 3, 4, 5])
target_mean = 5

## Call the function with my_array and target_mean
adjusted_array = offsetMean(my_array, target_mean)

print("Original array:", my_array)
print("Adjusted array:", adjusted_array)
print("New mean of the array:", np.mean(adjusted_array))