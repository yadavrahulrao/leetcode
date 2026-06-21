#729. My Calendar I


class MyCalendar(object):

    def __init__(self):
      self.mycalender = []

        

    def book(self, startTime, endTime):
      for i , j in self.mycalender :
        if startTime < j and endTime > i :
          return False
      
      self.mycalender.append((startTime,endTime))
      return True
        


# Your MyCalendar object will be instantiated and called as such:
obj = MyCalendar()
param_1 = obj.book(10,20)
print(param_1)
param_2 = obj.book(15,25)
print(param_2)


