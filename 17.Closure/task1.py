def function_1 (num):
    def function_2(num1):
        return num*num1
    return function_2

multiple_width_5=function_1(5)
multiple_width_4=function_1(4)

res_1=multiple_width_5(5)
res_2=multiple_width_4(8)

print(res_1,res_2)


