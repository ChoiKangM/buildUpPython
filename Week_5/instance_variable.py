class Car:
  color = ""
  speed = 0

  def __init__(self, name, speed):
    self.name = name
    self.speed = speed

  def get_name(self):
    return self.name

  def get_speed(self):
    return self.speed

## variables
car1, car2 = None, None

car1 = Car("BENZ", 30)
print("%s's speed is %dkm" % (car1.get_name(), car1.get_speed()))

car2 = Car("AUDI", 10)
print("%s's speed is %dkm" % (car2.get_name(), car2.get_speed()))