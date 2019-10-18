class Car:
  color = ""
  speed = 0

  def __init__(self, val_col, val_spd):
    self.color = "red"
    self.speed = 0

  def up_speed(self, value):
    self.speed += value

  def down_speed(self, value):
    self.speed -= value

myCar1 = Car("red", 0)
myCar2 = Car("blue", 0)
myCar3 = Car("yellow", 0)