import threading

class my_thread(threading.Thread):
  def __init__(self, no):
    threading.Thread.__init__(self)
    self.worker_no = no
  
  def run(self):
    for i in range(10):
      print("[%d] working - [%d] times" % (self.worker_no, i))

num = int(input("input number : "))

for k in range(num):
  t = my_thread(k)
  t.start()