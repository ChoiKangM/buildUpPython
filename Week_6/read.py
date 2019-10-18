in_file = None # txt file
in_str = ""    # read string

# 1. open file
in_file = open("data.txt", "r")

# 2. read
in_str = in_file.read()
print(in_str, end="")

# 3. close file
in_file.close()