def containsDuplicate(nums) -> bool:
    comparison_list=set(nums)
    if len(nums)>len(comparison_list):
        return True
    else:
        return False


print(containsDuplicate([1,2,3,1]))
print(containsDuplicate([1,2,3,4]))