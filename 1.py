# -----------------------masala-1-------------------------

def majority_element(nums: list) -> int:
    natija=-1
    son=0

    for i in nums:
        if nums.count(i) > son:
            son=nums.count(i)
            natija=i

    return natija


nums=[2, 2, 1, 1, 1, 2, 2]
print(majority_element(nums))

# -----------------------masala-1-------------------------