class Test:
  num = 10

  def ins_plus(self, a, b):
    return a + b + self.num

  @staticmethod
  def plus(a,b):
    return a + b

print("class direct: ", Test.plus(1,2))