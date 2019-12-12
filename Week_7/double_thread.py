from threading import Thread
import time

def do_work(start_no, end_no, result):
  sum = 0
  for i in range(start_no, end_no):
    sum += i
  result.append(sum)

while True:
  num = int(input("input number: "))
  start = 0
  end = num
  result = []

  t1 = time.time()

  th1 = Thread(target=do_work, args=(start, int(end/2), result))
  #th2 = Thread(target=do_work, args=(int(end/2), end, result))

  th1.start()
  #th2.start()

  th1.join()
  #th2.join()

  print("Result : %d" % sum(result))

  t2 = time.time()
  print("================ [%.3f sec]" % (t2 - t1))
  t1, t2 = 0.0, 0.0