import random
class Person:
  def __init__(self, name, phone):
    self.name = name
    self.phone = phone
  
  def get_name(self):
    return self.name

  def get_phone(self):
    return self.phone

class Student(Person):
  def __init__(self, major, schoolNum):
    self.major = major
    self.schoolNum = schoolNum

  def get_major(self):
    return self.major
  def get_schoolNum(self):
    return self.schoolNum

class Worker(Person):
  def __init__(self, depart, companyNum):
    self.depart = depart
    self.companyNum = companyNum
  
  def get_depart(self):
    return self.depart

  def get_companyNum(self):
    return self. companyNum

nameList = ["가가가","나나나","다다다","라라라","마마마",
            "바바바","사사사","아아아","자자자","차차차"]
majorList = ["전기공학부","컴퓨터공학부","전자공학부"]
departList = ["개발연구팀", "전략기획팀", "인사관리팀"]
person_List = []

for i in range(10):
  if(random.randint(0,1)):
    person = Student(random.choice(majorList), "201"+str(random.randint(1000000,9999999)))
    super(person).__init__(random.choice(nameList),"010-"+str(random.randint(0000,1000))+"-"+str(random.randint(0000,1000)))
  else:
    person = Worker(random.choice(departList), "2019"+str(random.randint(000,999)))
    super(person).__init__(random.choice(nameList),"010-"+str(random.randint(0000,1000))+"-"+str(random.randint(0000,1000)))
name = input("찾는 사람의 이름은?")

print(person)
# while(name != "끝"):
