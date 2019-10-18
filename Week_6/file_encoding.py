in_file = None # txt file
in_list = []   # list or string
in_str = ""    # read string

# 1. open file
in_file = open("data_utf8.txt", "r", encoding='utf-8')

# 2. read
in_list = in_file.readlines()
for in_str in in_list:
  print(in_str.strip('\n'))

# 3. close file
in_file.close()