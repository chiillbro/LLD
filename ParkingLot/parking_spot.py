from vehicle_type import VehicleType
from vehicle import Vehicle
from typing import Literal

class ParkingSpot:
  def __init__(self, spot_number : int):
    self.spot_number = spot_number
    self.vehicle_type = VehicleType.CAR
    self.parked_vehicle = None
  
  def is_available(self):
    return self.parked_vehicle is None
  
  def park_vehicle(self, vehicle : Vehicle) -> None:
    if self.is_available():
      self.parked_vehicle = vehicle
      self.vehicle_type = vehicle.get_type()
    else:
      raise ValueError("Invalid Vehicle Type or Spot was already occupied!")


  def unpark_vehicle(self) -> None:
    self.parked_vehicle = None

  def get_spot_number(self) -> int:
    return self.spot_number
  
  def get_vehicle_type(self) -> VehicleType:
    return self.vehicle_type

  def get_parked_vehicle(self) -> None | Vehicle:
    return self.parked_vehicle
