class LinkedList():
  def __init__(self):
    self.head = None

  class Box():
    cat = None
    nextcat = None
    def __init__(self, cat, nextcat = None):
      self.cat = cat
      self.nextcat = nextcat

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
    newbox = self.Box(newcat)
    if self.head is None:
      self.head = newbox
      return
    lastbox = self.head
    while (lastbox.nextcat):
      lastbox = lastbox.nextcat
    lastbox.nextcat = newbox

  def addToPosition(self, cat, index):
    i = 0
    node = self.head
    prev_node = self.head
    while i < index:
      prev_node = node
      node = node.nextcat
      i += 1
    prev_node.nextcat = self.Box(cat, nextcat = node)
    return cat

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
print(List.length())
print(List.contains('5'))
List.addToEnd('10')
print(List.get(3))
List.removeBox(3)

List.addToPosition('11', 4)
print(List.length())
final = []
for i in range(List.length()):
  final.append(List.get(i))
print(final)