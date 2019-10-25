# function : +2 sum
# param : int (max num)
# return : int
def sum(max):
    result = 0
    for i in range(0, max, 2):
        result += i
    return result


# main
num = int(input("2씩 더할 최대 숫자를 입력하세요 : "))
print("결과 : %d" % sum(num))