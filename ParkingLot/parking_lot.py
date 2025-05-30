from typing import List
from level import Level
from vehicle import Vehicle

class ParkingLotException(Exception):
  pass

class ParkingLot:
  _instance = None
  def __init__(self):
    if ParkingLot._instance:
      raise ParkingLotException("ParkingLot already initialized")
    else:
      ParkingLot._instance = self
      self.levels : List[Level] = []
  
  @staticmethod
  def get_instance():
    if not ParkingLot._instance:
      ParkingLot()
    
    return ParkingLot._instance


  def add_level(self, level : Level) -> None:
    self.levels.append(level)

  def park_vehicle(self, vehicle: Vehicle) -> bool:
    for level in self.levels:
      if level.park_vehicle(vehicle):
        return True
    
    return False

  def unpark_vehicle(self, vehicle : Vehicle) -> bool:
    for level in self.levels:
      if level.unpark_vehicle(vehicle):
        return True
    
    return False

  def display_availability(self) -> None:
    print("Level Wise Availability Display")
    for level in self.levels:
      print(f"Availability for Level: {level.floor}")
      level.display_availability()