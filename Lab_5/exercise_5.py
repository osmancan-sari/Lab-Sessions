def sum_binaries(str1:str, str2:str):
    max_len = max(len(str1), len(str2))

    str1 = str1.zfill(max_len)
    str2 = str2.zfill(max_len)

    result = ""
    carry = 0

    i = max_len - 1

    while i >= 0:
        s = int(str1[i]) + int(str2[i]) + carry
        if s == 0:
            result += '0'
        elif s == 1:
            result += '1'
            carry = 0
        elif s == 2:
            result += '0'
            carry = 1
        elif s == 3:
            result += '1'
            carry = 1
        i = i-1

    if carry == 1:
        result += '1'

    final_result = result[::-1]
    return final_result

str1, str2 = input().split(" ")

print(sum_binaries(str1, str2))
            
