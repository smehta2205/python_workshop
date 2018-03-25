class Person(object):
  def __init__(self, name):
      self.name = name

  def hello(self):
      print("Hello, %s" %self.name)
      #print("Hello, {}" .format(self.name))

p=Person("Stuti")
p.hello()
#Person(p).hello()
