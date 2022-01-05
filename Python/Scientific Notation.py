# Note : To the number larger than 1 and is a float one , information of the numbers of digit
# come atfer the LIMIT length would be lost
# (9222227.256 -> 9.22223 * 10^7)
LIMIT = 5  # Limit to show decimal digits atfer decimal point


# ---------------------------------------------------------
def cutDigit(num, isDecimal=False):
    res = num
    if isDecimal:
        zero = res.count('0')
        exp_num = 1
        for w in res:
            if w == '0':
                exp_num += 1
            else:
                break
        degit_num = res.replace('0', '', len(res))
        degit_num = degit_num[0] + '.' + degit_num[1:]
    else:
        index = res.find('.')
        if index >= 0:
            lim = index - 1
            res = res.replace('.', '')
        else:
            lim = len(res) - 1
        exp_num = lim
        degit_num = res[0] + '.' + res[1:]
    return degit_num, exp_num


# ----------------------------------------------------------
word = input('Number: ').strip()
number = word
sign = 1  # Positive number signal
exp_sign = 1  # larger than 1 signal
isDec = False  # smaller than 1
if number[0] == '-':
    sign = -1
    number = number[1:]
found = number.find('0.')
if found >= 0:  # small than 1
    isDec = True
    number = number[2:]
    exp_sign = -1
degit, exp = cutDigit(number, isDec)
print('{0} => {1} * 10^{2} '.format(word, round(float(degit) * sign, LIMIT), exp * exp_sign))
