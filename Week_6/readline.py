in_file = None # txt file
in_str = ""    # read string

# 1. open file
in_file = open("data.txt", "r")

# 2. read
while True:
  in_str = in_file.readline()
  if in_str == "": break
  print(in_str, end="")

# 3. close file
in_file.close()