class CSStudent:
   stream="CSE"
   def __init__(self,name,roll):
       self.name=name
       self.roll=roll
if __name__=="__main__":
   a=CSStudent("Geek",1)
   b=CSStudent("Geek2",2)
   print(a.stream)
   print(b.stream)
   print(a.name)
   print(b.name)
   print(a.roll)
   print(b.roll)
   print(CSStudent.stream)