in_file = None # txt file
in_str = ""    # read string

# 1. open file
in_file = open("data.txt", "r")

# 2. read
in_list = in_file.readlines()
for in_str in in_list:
  print(in_str)

# 3. close file
in_file.close()