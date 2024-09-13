def func_trans(a, b, c):
    numbers = str(a) + str(b) + str(c)    
    return numbers


outPut = int(func_trans(2, 1, 3))

print(f"{outPut}", type(outPut), '\n')


def digits2number(hundreds, tens, units):
    number = 100*hundreds + 10*tens + units
    return number


num1 = digits2number(hundreds=1, tens=2, units=3)
num2 = digits2number(tens=2, units=3, hundreds=1)
num3 = digits2number(units=3, hundreds=1, tens=2)
print(f"{num1 = }, {num2 = }, {num3 = }\n")


def func_mean(scores, base_score):
    mean = sum(score + base_score for score in scores) / len(scores)
    return mean


scores = [10, 20, 30]

mean1 = func_mean(scores, base_score=0)
mean2 = func_mean(scores, base_score=10)
mean3 = func_mean(scores, base_score=20)
print(f"{mean1 = }, {mean2 = }, {mean3 = }")