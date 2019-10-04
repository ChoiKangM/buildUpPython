# 무한반복하지만 99999 입력시 탈출
scores = []
while True:
  # 교과목들의 점수를 한꺼번에 입력하세요
  scores = input("교과목들의 점수를 한꺼번에 입력하세요")
  if scores == "99999":
    break
  lists = [float(x) for x in scores.split(',')]
  # print(lists)
  # 최저 점수, 최고 점수, 평균점수 출력
  min = min(lists)
  max = max(lists)
  average = sum(lists) / len(lists)
  result = f'최저점수 : %.2f, 최대점수 : %.2f, 평균점수: %.2f' % (min, max, average)
  print(result)  


