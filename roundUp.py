'''
The construction of the code is as follows.
版权声明：本文为CSDN博主「我心依依旧」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/a200822146085/article/details/89181439
'''
def round_up(number,power=0):
    """
    exactly extract num of float
    param number: float
    param power: support 0-∞
    return: 4 out 5 in
    """
    digit = 10 ** power
    num2 = float(int(number * digit))
    # positive number，power is not 0
    if number>=0 and power !=0:
        tag = number * digit - num2 + 1 / (digit * 10)
        if tag>=0.5:
            return (num2+1)/digit
        else:
            return num2/digit
    # positive number，power is 0
    elif  number>=0 and power==0 :
        tag = number * digit - int(number)
        if tag >= 0.5:
            return (num2 + 1) / digit
        else:
            return num2 / digit
    # negative number，power is 0
    elif power==0 and number<0:
        tag = number * digit - int(number)
        if tag <= -0.5:
            return (num2 - 1) / digit
        else:
            return num2 / digit
    # negative number，power is not 0
    else:
        tag = number * digit - num2 - 1 / (digit * 10)
        if tag <= -0.5:
            return (num2-1)/digit
        else:
            return num2/digit
