out_file = None
str_list = ["안녕하세요.", "하위하위", "파이썬", "잼잼"]


# 1. open file
out_file = open("output3.txt", "w", encoding="utf-8")

# 2. write string
out_file.write('\n'.join(str_list))

# 3. close flle
out_file.flush()
out_file.close()