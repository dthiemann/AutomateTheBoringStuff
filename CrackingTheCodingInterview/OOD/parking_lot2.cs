/* 
    A (hopefully) better implementation of the parking lot OOD design
*/

public enum SpotSize
{
    Motorcylce,
    Compact,
    Large
}

public enum VehicleType
{
    Motorcycle,
    Car,
    Bus
}

public static class SpotVehicleFitCalculator
{
    public static bool CanFit(ParkingSpot spot, VehicleType vehicleType)
    {
        var spotSize = spot.GetSpotSize();
        switch (vehicleType)
        {
            case (VehicleType.Motorcycle):
                return !spot.IsOccupied();
            case (VehicleType.Car):
                return !spot.IsOccupied() && (spotSize == SpotSize.Compact || spotSize == SpotSize.Large);
            case (VehicleType.Large):
                return !spot.IsOccupied() && (spotSize == spotSize.Large);
        }
    }
}

public abstract class Vehicle
{
    protected string plateNumber { get; set; }
    protected int spotsNeeded { get; set; }

    protected VehicleType type { get; set; }

    protected List<ParkingSpot> parkingSpots;
    private Vehicle(int plateNumber)
    {
        this.plateNumber = plateNumber;
    }

    public bool CanFitInSpot(ParkingSpot spot)
    {
        return SpotVehicleFitCalculator.CanFit(spot, this);
    }

    // Returns true if it parked, false otherwise
    public bool ParkVehicleInSpot(ParkingSpot spot)
    {
        this.parkingSpots.Add(spot);
    }

    public string GetPlateNumber() { return this.plateNumber; }
    public int GetSpotsNeeded() { return this.spotsNeeded; }
    public VehicleType GetVehicleType() { return this.type; }

    public void ClearParkingSpots()
    {
        this.parkingSpots.Clear();
    }
}

public class Motorcycle : Vehicle
{
    public Motorcycle(string plateNumber)
    {
        super(plateNumber);
        this.type = VehicleType.Motorcycle;
        this.spotsNeeded = 1;
    }
}

public class Car : Vehicle
{
    public Car(string plateNumber)
    {
        super(plateNumber);
        this.type = VehicleType.Car;
        this.spotsNeeded = 1;
    }
}

public class Bus : Vehicle
{
    public Bus(string plateNumber)
    {
        super(plateNumber);
        this.type = VehicleType.Bus;
        this.spotsNeeded = 5;
    }
}

public class ParkingSpot
{
    protected Vehicle parkedVehicle { get; set; }
    protected int floor { get; set; }
    protected int row { get; set; }
    protected int spotNumber { get; set; } // Index in the floor array

    protected SpotSize size { get; set; }

    public bool IsOccupied()
    {
        return parkedVehicle != null;
    }

    public ParkingSpot(int floor, int row, int spotNumber, SpotSize size)
    {
        this.floor = floor;
        this.row = row;
        this.spotNumber = spotNumber;
        this.size = size;
    }

    // only checks size (not if more than one is needed)
    public bool CanFitVehicle(Vehicle v)
    {
        return SpotVehicleFitCalculator.CanFit(this, v);
    }

    public SpotSize GetSpotSize()
    {
        return this.size;
    }
}