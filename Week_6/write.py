out_file = None
out_str = ""

# 1. open file
out_file = open("output.txt", "w")

while True:
  out_str = input("input string : ")
  
  if out_str == "exit": break

  # 2. write string
  out_file.write(out_str)
  out_file.write('\n')

# 3. close flle
out_file.close()