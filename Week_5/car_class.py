class Car:
  color = ""
  speed = 0

  def up_speed(self, value):
    self.speed += value

  def down_speed(self, value):
    self.speed -= value


myCar1 = Car()
myCar1.color = "red"
myCar1.speed = 0

myCar2 = Car()
myCar2.color = "blue"
myCar2.speed = 0

myCar3 = Car()
myCar3.color = "yellow"
myCar3.speed = 0

myCar1.up_speed(30)
print("CAR_1's color is %s. speed is %dkm" % (myCar1.color, myCar1.speed))

myCar2.up_speed(60)
print("CAR_2's color is %s. speed is %dkm" % (myCar2.color, myCar2.speed))

myCar3.up_speed(30)
print("CAR_3's color is %s. speed is %dkm" % (myCar3.color, myCar3.speed))