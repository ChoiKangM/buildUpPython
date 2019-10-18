import os  # os module for searching file path

file_name = "" # file name
in_file = None # txt file
in_str = ""    # read string

while True:
  file_name = input("\ninput file name : ")

  # check file path
  if os.path.exists(file_name):
    # 1. open file
    in_file = open(file_name, "r")

    # 2. read
    in_list = in_file.readlines()
    for in_str in in_list:
      print(in_str.strip('\n'))

    # 3. close file
    in_file.close()
  else:
    print("error - '%s' file no exist..." % file_name)
    