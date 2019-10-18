in_file = None # txt file
in_str = ""    # read string

# 1. open file
in_file = open("data.txt", "r")

# 2. read
in_list = in_file.readlines()
print(in_list)

# 3. close file
in_file.close()