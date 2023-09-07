def isPalindrome(x: int)-> bool:
    list_of_numbers= list(str(x))
    reversed_list=[]
    for num in reversed(list_of_numbers):
        reversed_list.append(num)
    if ("".join(list_of_numbers))==("".join(reversed_list)):
        return True
    else:
        return False
    

print(isPalindrome(121))
print(isPalindrome(10))