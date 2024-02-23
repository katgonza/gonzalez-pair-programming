# TASK PROMPT: Offsets the mean of a given array to match a given value
def offsetMean(arr, target_mean):

    # calculate the current mean of the given array
    current_mean = np.mean(arr)

    # calculate the offset needed to match the target mean
    offset_value = target_mean - current_mean
    
    # offset each element in the array using vectorized operations
    offset_arr = arr + offset_value

    return offset_arr