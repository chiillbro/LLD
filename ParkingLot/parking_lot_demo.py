from parking_lot import ParkingLot
from level import Level
from vehicle import Vehicle
from vehicle_type import VehicleType
from car import Car
from motorcycle import MotorCycle
from truck import Truck

class ParkingLotDemo:
  def run():
    parking_lot = ParkingLot.get_instance()

    parking_lot.add_level(Level(1, 5))
    parking_lot.add_level(Level(2, 4))

    # parking_lot.display_availability()

    car1 = Car("ABCH34324")
    motorcycle1 = MotorCycle("doijid333")
    truck1 = Truck("FEOO343")


    print(parking_lot.park_vehicle(car1))

    print(parking_lot.park_vehicle(motorcycle1))

    print(parking_lot.park_vehicle(truck1))

    parking_lot.display_availability()

if __name__ == "__main__":
  ParkingLotDemo.run()