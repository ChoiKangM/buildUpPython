out_file = None
str_list = ["안녕하세요.\n", "하위하위\n", "파이썬\n", "잼잼\n"]


# 1. open file
out_file = open("output2.txt", "w", encoding="utf-8")

# 2. write string
out_file.writelines(str_list)

# 3. close flle
out_file.close()