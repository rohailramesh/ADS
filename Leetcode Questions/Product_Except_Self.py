# This is brute force approach with time complexity of n^2.
def productExceptSelf(nums):
    res = []
    for i in range(len(nums)):
        temp_product = 1
        for j in range(len(nums)):
            if(i != j):
                temp_product *= nums[j]
                print(temp_product)
                # print(nums[i],nums[j])
        res.append(temp_product)
    return res
                
# print(productExceptSelf([4,2,3,7]))


# Using idea of prefix and suffix for optimal time and space complexity
def productExceptSelfOptimal(nums):
    res = [1] * (len(nums))
    # print(res)
    prefix = suffix = 1
    for i in range(len(nums)):
        res[i] = prefix
        prefix *= nums[i]
    # print(nums)
    # print(res)
    for i in range(len(nums)-1, -1, -1):
        # print(nums[i])
        res[i] *= suffix
        suffix *= nums[i]
        print(res)
    # print(res)
    return res

print(productExceptSelfOptimal([4,2,3,7]))