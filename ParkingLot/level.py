from parking_spot import ParkingSpot
from typing import List
from vehicle import Vehicle

class Level:
  def __init__(self, floor_number: int, spots_count : int):
    self.floor = floor_number
    self.spots : List[ParkingSpot] = [ParkingSpot(i) for i in range(1, spots_count + 1)]
  

  def park_vehicle(self, vehicle : Vehicle) -> bool:
    for spot in self.spots:
      if spot.is_available():
        spot.park_vehicle(vehicle)
        return True
    return False

  def unpark_vehicle(self, vehicle: Vehicle) -> bool:
    for spot in self.spots:
      if not spot.is_available() and spot.parked_vehicle == vehicle:
        spot.unpark_vehicle()
        return True
    return False

  def display_availability(self):
    for spot in self.spots:
      print(f"Spot {spot.get_spot_number()}: {'Available' if spot.is_available() else 'Occupied'}")