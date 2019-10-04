def spam(eggs):
  # eggs로 전달된 주소값에 [1]추가
  eggs.append(1)
  # 전달된 eggs 주소 확인
  print(id(eggs))

  eggs = [2,3]
  print(id(eggs))
  print("in spam : ", eggs)

# main
ham = [0]
spam(ham)

print("result: ", ham)
print(id(ham))