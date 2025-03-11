from vehicle import Vehicle
from vehicle_type import VehicleType

class MotorCycle(Vehicle):
  def __init__(self, license_plate):
    super().__init__(license_plate, VehicleType.MOTORCYCLE)