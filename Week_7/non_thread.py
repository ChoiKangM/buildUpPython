def working(worker_no):
  for i in range(10):
    print("[%d] working - [%d] times" % (worker_no, i))

num = int(input("input number : "))

for k in range(num):
  working(k)