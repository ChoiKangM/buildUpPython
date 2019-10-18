class Car:
  color = ""
  speed = 0

  def __init__(self):
    self.color = "red"
    self.speed = 0

  def up_speed(self, value):
    self.speed += value

  def down_speed(self, value):
    self.speed -= value

myCar1 = Car()