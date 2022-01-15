"""
class Box:
  def __init__(self, weight):
    self.__weight = weight
 
  def getWeight(self)
    return self.__weight
 
  def setWeight(self, weight):
    if weight >= 0:
      self.__weight = weight
 
  def delWeight(self):
    del self.__weight
 
  weight = property(getWeight, setWeight, delWeight, "Docstring for the 'weight' property")
"""

class Box:
 def __init__(self, weight):
   self.__weight = weight
 
 @property
 def weight(self):
   """Docstring for the 'weight' property"""
   return self.__weight
 
 
 @weight.setter
 def weight(self, weight):
   if weight >= 0:
     self.__weight = weight
 
 @weight.deleter
 def weight(self):
   del self.__weight


box = Box(10)
#print(box.weight)

box.weight = 5
#print(box.weight)

del box.weight
#print(box.weight)