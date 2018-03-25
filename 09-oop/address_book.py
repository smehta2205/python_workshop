class AddressBook(object):
  def __init__(self, name, id_no, mobile, email):
    self.name= name
    self.id_no = id_no
    self.mobile = mobile
    self.email = email

  def __str__(self):
    return("{} has id {}. (s)he can be contacted via {} or {}".format
    (self.name,
    self.id_no,
    self.mobile,
    self.email))
