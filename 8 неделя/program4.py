class Box():
  def __init__ (self,cat = None):
    self.cat = cat
    self.nextcat = None

class LinkedList():
  def __init__(self):
    self.head = None
  def length(self):
    len = 0
    lastbox = self.head
    while (lastbox):
      len += 1
      lastbox = lastbox.nextcat
    return len

  def contains(self, cat):
    lastbox = self.head
    while (lastbox):
      if cat == lastbox.cat:
        return True
      else:
        lastbox = lastbox.nextcat
    return False

  def addToEnd(self, newcat):
    newbox = Box(newcat)
    if self.head is None:
      self.head = newbox
      return
    lastbox = self.head
    while (lastbox.nextcat):
      lastbox = lastbox.nextcat
    lastbox.nextcat = newbox

  def get(self, catIndex):
    lastbox = self.head
    boxIndex = 0
    if catIndex >= List.length():
      return None
    else:
      while boxIndex <= catIndex:
        if boxIndex == catIndex:
          return lastbox.cat
        boxIndex = boxIndex + 1
        lastbox = lastbox.nextcat


  def removeBox(self, rmcat):
    headcat = self.head
    rmIndex = 0
    if headcat is not None:
      if rmIndex == rmcat:
        self.head = headcat.nextcat
        rmIndex += 1
        headcat = None
        return
    while headcat is not None:
        if rmIndex == rmcat:
          break
        lastcat = headcat
        headcat = headcat.nextcat
        rmIndex += 1
    lastcat.nextcat = headcat.nextcat
    if headcat == None:
      return
    headcat = None

List = LinkedList()
P_list = list(map(str, input().split()))
for i in range (len(P_list)):
  List.addToEnd(P_list[i])

print(List.get(6))