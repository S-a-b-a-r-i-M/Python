class Distance:
  def __init__(self, value):
    self._km = value

  @property
  def kilometers(self):
    return self._km
  
  @kilometers.setter
  def kilometers(self, value):
    if value < 0:
      raise ValueError("Negative values not allowed")
    self._km = value

  @property
  def meters(self):
    return self._km * 1000
  
  @meters.setter
  def meters(self, value):
    if value < 0:
      raise ValueError("Negative values not allowed")
    self._km = value//1000


distance = Distance(10)
print(distance.kilometers) # Accessing a method like a attribute of the class
print(f"{distance.kilometers} is equal to {distance.meters} meters")
distance.meters = 2000
print(distance.kilometers)

# below statement raise an exception
# distance.kilometers = -100 

