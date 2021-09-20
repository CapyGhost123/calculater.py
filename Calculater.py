print("Whats would you like To Do type as given to do opreation")
lol = input("(1 = add / 2 = subtract / 3 = multiply / 4 = divide):")
if lol == '1':
    add_num1 = input("num one:")
    add_num2 = input("num two:")
    add = int(add_num1) + int(add_num2)
    print(add)
else:
    pass 
if lol =='2':
    sub_1 = input("Num one:")
    sub_2 = input("Num two:")
    sub = int(sub_1) - int(sub_2)
    print(sub)
else:
    pass
if lol == '3':
    multi1 = input('Num one:')
    multi2 = input('Num two:')
    mult = int(multi1) * int(multi2)
    print(mult)
else:
    pass
if lol == '4':
       divi1 = input("Num one:")
       div2 = input("Num2 two:")
       div = int(divi1) / int(div2)
       print(div)