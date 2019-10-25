import random
import time

class Person:
  def __init__(self, name, phone):
    self.name = name
    self.phone = phone
  
  def get_name(self):
    return self.name

  def get_phone(self):
    return self.phone

class Student(Person):
  def __init__(self, name, phone, major, schoolNum):
    Person.__init__(self, name, phone)
    self.major = major
    self.schoolNum = schoolNum

  def get_major(self):
    return self.major
  def get_schoolNum(self):
    return self.schoolNum

class Worker(Person):
  def __init__(self, name, phone, depart, companyNum):
    Person.__init__(self, name, phone)
    self.depart = depart
    self.companyNum = companyNum

  def get_depart(self):
    return self.depart

  def get_companyNum(self):
    return self. companyNum

in_file = None # txt file
in_str = ""    # read string
person_List = []

# log file
out_file = open("address.log", "w", encoding="utf-8")

# 1. open file

in_file = open("address.txt", "r")
out_file.write("["+time.asctime()+"]"+" open file address.txt\n")

# 2. read
while True:
  in_str = in_file.readline()
  if in_str[1:3]=="학생":
    name = in_str[10:13]
    phone = str(in_str[23:36])
    major = in_str[41:47]
    schoolNum = in_str[57:68]

    person_List.append(Student(name, phone, major, schoolNum))
  
  elif in_str[1:3]=="사원":
    name = in_str[10:13]
    phone = str(in_str[23:36])
    depart = in_str[41:47]
    companyNum = in_str[57:68]

    person_List.append(Worker(name, phone, depart, companyNum))

  else:
    print("invalid input")

  if in_str == "": break
  print(in_str, end="")

print(person_List)
out_file.write("["+time.asctime()+"]"+" total "+str(len(person_List))+" persons\n")

person_name = input("찾을 사람 이름은 ? ")
while(person_name != "끝"):
  for i in range(len(person_List)):
    if person_name == str(person_List[i].name):
      out_file.write("["+time.asctime()+"]"+" search "+person_name+ "\n")
      match = person_List[i]
  if type(match) is Student :
    print("[학생] 이름 : "+match.name+"\t전화번호: "+ match.phone +"\t학과 :"+ match.major+"\t학번: "+match.schoolNum)

  elif type(match) is Worker :
    print("[사원] 이름 : " +match.name + "\t전화번호: " +match.phone+ "\t부서 :" +match.depart+ "\t사번: " +match.companyNum)
  else :
    print("찾는 사람이 없습니다")
  person_name = input("찾을 사람 이름은 ? ")

out_file.write("["+time.asctime()+"]"+" exit\n")
# 3. close file
in_file.close()
# 3. close flle
out_file.flush()
out_file.close()
