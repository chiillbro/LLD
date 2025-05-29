# Builder Pattern : Main goal is to separate the object's construction from its representation

class House():
  def __init__(self, builder):
    self._stories = builder.stories
    self._roof_type = builder.roof_type
    self._door_type = builder.door_type
    self._rooms = builder.rooms

  @property
  def stories(self):
    return self._stories

  @property
  def roof_type(self):
    return self._roof_type
  
  @property
  def door_type(self):
    return self._door_type
  
  @property
  def rooms(self):
    return self._rooms
  
  def get_attributes(self):
    room_str = ', '.join(str(room) for room in self.rooms)
    return f"{self.stories} {self.roof_type} {self.door_type} | {room_str}"
  

class Room:
  def __init__(self, name, size):
    self.name = name
    self.size = size
  
  def __str__(self):
    return f"{self.name} ({self.size} sqft)"


class Builder:
  def __init__(self):
    self.stories = None
    self.roof_type = None
    self.door_type = None
    self.rooms = []

  
  def set_stories(self, stories : int):
    self.stories = stories
    return self
  
  def set_roof_type(self, roof_type : str):
    self.roof_type = roof_type
    return self
  
  def set_door_type(self, door_type : str) :
    self.door_type = door_type
    return self
  
  def set_room(self, name : str, size : int):
    self.rooms.append(Room(name, size))
    return self

  def build(self):
    if not self.stories or not self.door_type or not self.roof_type:
      raise ValueError("Missing required attributes!")
    return House(self)
  


# Imagine a one_storey_house will always be having one storey, single door type and pointy roof and a two-storey_house will always be having two storey, double door type and flat roof

# Then instead of building the house with the requirements from the scratch, we can create a class called Director which will do all the fixed requirements of a particular house and returns the instance to us

#  Our Director class which takes builder as parameter and returns different types of houses depending on the client's requirement
class Director:
    def __init__(self, builder):
      self.builder = builder

    
    def build_house(self, type : str) -> Builder:
      if type == "Modern":
        return self.builder.set_stories(2).set_door_type("Sliding").set_roof_type("Flat").build()
      elif type == "Classic":
        return self.builder.set_stories(1).set_door_type("Single").set_roof_type("pointy").build()
      elif type == "Family":
        return self.builder.set_stories(2).set_door_type("Double").set_roof_type("Gabled").set_room("Living Room", 250).set_room("Kitchen", 150).build()
      else:
        return self.builder.set_stories(1).set_door_type("Single").set_roof_type("Flat").build()
    
    # def build_1_storey_house(self):
    #   return self.builder.set_stories(1).set_door_type("Single").set_roof_type("pointy").build()

    # def build_2_storey_house(self):
    #   return self.builder.set_stories(2).set_door_type("Double").set_roof_type("Flat").build()


house_builder = Builder()
# one_storey_house_step_1 = house_builder.set_stories(1)
# one_storey_house_step_2 = one_storey_house_step_1.set_roof_type("Pointy").set_door_type("Double")
# one_storey_house = one_storey_house_step_2.build()

director = Director(house_builder)

modern_house = director.build_house("Modern")

classic_house = director.build_house("Classic")
family_house = director.build_house("Family")

print("modern_house", modern_house.get_attributes())
print("classic_house", classic_house.get_attributes())
print("family_house", family_house.get_attributes())


# one_storey_house = director.build_1_storey_house()
# two_storey_house = director.build_2_storey_house()

# print("one_storey_house", one_storey_house.get_attributes())

# print("two_storey_house", two_storey_house.get_attributes())


