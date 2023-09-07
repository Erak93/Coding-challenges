def countBits(n):
    bit_dic={}
    for num in range(0,n+1):
        bit_dic[num]=int(str(bin(num)).replace("b",""))
    binary_count_list=[]

    for value in bit_dic:
        binary_count_list.append(bit_dic[value])
    
    for i in range(len(binary_count_list)):
        binary_count_list[i]=list(str(binary_count_list[i])).count("1")
    
    return binary_count_list


print(countBits(2))
print(countBits(5))
