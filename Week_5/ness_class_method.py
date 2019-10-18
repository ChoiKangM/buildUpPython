class Date:
  word = "date : "

  def __init__(self, date):
    self.date = self.word + date

    # @staticmethod
    # def now():
    #   return Date("today")

    # def show(self):
    #   print(self.date)

    @classmethod
    def now(cls):
      return cls("today")

    def show(self):
      print(self.date)

class KoreanDate(Date):
  word = "날짜 : "

my_day = Date("2019-10-04")
my_day.show()

your_day = Date.now()
your_day.show()

his_day = KoreanDate.now()
his_day = show()