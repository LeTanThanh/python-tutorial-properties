class Person:
  def __init__(self, name, age) -> None:
    self.name = name
    self.set_age(age)

  def set_age(self, age):
    if age <= 0:
      raise ValueError("The age must be positive")
    else:
      self._age = age

  def get_age(self):
    return self._age
