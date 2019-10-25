# 1. 10 points
from calculator.calculator import *
import logging

# 9. 15points
logging.basicConfig(filename='cal.log',format='%(asctime)s %(message)s')
request = input("계산합시다 : ")
logging.warning("계산식 : {}".format(request))

# 2. 5 points
while request!="exit":
    # 8. 15 points
    if request=="txt":
        file = open("cal.txt", "r")
        logging.warning("파일 열기 : cal.txt")
        for lines in file:
            print(lines)
        lists = lines.split(' ')
    else:
        lists = request.split(' ')

    for list in lists:
        # 3. 10 points
        if list.isalpha():
            print("잘못된 입력")
            logging.warning("잘못된 입력")
            continue

    # 4. 10 points, 5. 10 points
    for i in range(len(lists)):
        if i % 2:
            if lists[i] == '+':
                lists[i+1] = plus(float(lists[i-1]), float(lists[i+1]))
                # 7. 10 points
                if lists[i + 1].is_integer():
                    print("결과 : {}".format(int(lists[i+1])))
                    logging.warning("결과 : {}".format(int(lists[i + 1])))
                else:
                    print("결과 : {}".format(lists[i + 1]))
                    logging.warning("결과 : {}".format(lists[i + 1]))
            elif lists[i] == '-':
                lists[i + 1] = minus(float(lists[i - 1]), float(lists[i + 1]))
                # 7. 10 points
                if lists[i + 1].is_integer():
                    print("결과 : {}".format(int(lists[i + 1])))
                    logging.warning("결과 : {}".format(int(lists[i + 1])))
                else:
                    print("결과 : {}".format(lists[i + 1]))
                    logging.warning("결과 : {}".format(lists[i + 1]))
            elif lists[i] == '*':
                lists[i + 1] = multiply(float(lists[i - 1]), float(lists[i + 1]))
                # 7. 10 points
                if lists[i + 1].is_integer():
                    print("결과 : {}".format(int(lists[i + 1])))
                    logging.warning("결과 : {}".format(int(lists[i + 1])))
                else:
                    print("결과 : {}".format(lists[i + 1]))
                    logging.warning("결과 : {}".format(lists[i + 1]))
            else:
                lists[i + 1] = divide(float(lists[i - 1]), float(lists[i + 1]))
                # 7. 10 points
                if lists[i + 1].is_integer():
                    print("결과 : {}".format(int(lists[i + 1])))
                    logging.warning("결과 : {}".format(int(lists[i + 1])))
                else:
                    print("결과 : {}".format(lists[i + 1]))
                    logging.warning("결과 : {}".format(lists[i + 1]))


    request = input("계산합시다 : ")


logging.warning("프로그램 종료")



