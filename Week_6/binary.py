copy_file = open("copy.jpg", "wb")

# open binary file
bin_file = open("cafe.jpg", "rb")
print(bin_file.read())

# read and write binary file
copy_file.write(bin_file.read())

# close file
bin_file.close()
copy_file.close()