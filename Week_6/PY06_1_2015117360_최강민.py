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

nameList = ["가가가","나나나","다다다","라라라","마마마",
            "바바바","사사사","아아아","자자자","차차차"]
majorList = ["전기공학부","컴퓨터공학부","전자공학부"]
departList = ["개발연구팀", "전략기획팀", "인사관리팀"]
person_List = []

for i in range(10) :
  if(random.randint(0,1)):
    person_List.append(Student(
        random.choice(nameList),
        "010-" + "{:04n}".format(random.randint(0000, 1000)) + "-" + "{:04n}".format(random.randint(0000, 1000)),
        random.choice(majorList),
        "201"+ "{:06n}".format(random.randint(1000000,9999999))
        )
    )

  else :
    person_List.append(Worker(
      random.choice(nameList),
      "010-" + "{:04n}".format(random.randint(0000, 1000)) + "-" + "{:04n}".format(random.randint(0000, 1000)),
      random.choice(departList),
      "2019"+ "{:03n}".format(random.randint(000,999))
      )
    )
print(person_List)
# 1. open file
out_file = open("address.txt", "w", encoding="utf-8")

# 2. write string
for i in range(len(person_List)):
  # person = person_List[i]
  if type(person_List[i]) is Student :
    out_file.writelines("[학생] 이름 : "+person_List[i].name+"\t전화번호: "+ person_List[i].phone +"\t학과 :"+ person_List[i].major+"\t학번: "+person_List[i].schoolNum)

  elif type(person_List[i]) is Worker :
    out_file.writelines("[사원] 이름 : " +person_List[i].name + "\t전화번호: " +person_List[i].phone+ "\t부서 :" +person_List[i].depart+ "\t사번: " +person_List[i].companyNum)
  out_file.write("\n")
# 3. close flle
out_file.flush()
out_file.close()

for i in range(len(person_List)):
  # person = person_List[i]
  if type(person_List[i]) is Student :
    print("[학생] 이름 : "+person_List[i].name+"\t전화번호: "+ person_List[i].phone +"\t학과 :"+ person_List[i].major+"\t학번: "+person_List[i].schoolNum)

  elif type(person_List[i]) is Worker :
    print("[사원] 이름 : " +person_List[i].name + "\t전화번호: " +person_List[i].phone+ "\t부서 :" +person_List[i].depart+ "\t사번: " +person_List[i].companyNum)

person_name = input("찾을 사람 이름은 ? ")
while(person_name != "끝"):
  for i in range(len(person_List)):
    if person_name == str(person_List[i].name):
      match = person_List[i]
  if type(match) is Student :
    print("[학생] 이름 : "+match.name+"\t전화번호: "+ match.phone +"\t학과 :"+ match.major+"\t학번: "+match.schoolNum)

  elif type(match) is Worker :
    print("[사원] 이름 : " +match.name + "\t전화번호: " +match.phone+ "\t부서 :" +match.depart+ "\t사번: " +match.companyNum)
  else :
    print("찾는 사람이 없습니다")
  person_name = input("찾을 사람 이름은 ? ")
