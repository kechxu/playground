# Compute the sum of a vector

def vector_sum(nums):
    """
    @brief: compute the sum of a vector, (or list in python)
    @param num: the vector
    @return the sum of elements nums
    """
    # Add code here
    return sum(nums)


if __name__ == "__main__":

    nums1 = [1, 2, 3]
    if (vector_sum(nums1) == 6):
        print("Test Success!")
    else:
        print("Test Failed!")

