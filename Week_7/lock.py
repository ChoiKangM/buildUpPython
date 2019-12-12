import threading

class my_thread(threading.Thread):
  def __init__(self, no):
    threading.Thread.__init__(self)
    self.worker_no = no
  
  def run(self):
    t_lock.acquire()
    for i in range(10):
      print("[%d] working - [%d] times" % (self.worker_no, i))
    t_lock.release()
t_lock = threading.Lock()
ths = []

num = int(input("input number : "))

for k in range(num):
  t = my_thread(k)
  t.start()
  ths.append(t)

for t in ths:
  t.join()

print("-----finish all threads-----")