// Design an OO parking lot. What classes and functions will it have. It should say full, empty, and also be able to find spot for Valet parking
// Three different types of parking: regular, handicapped and compact

// ** Clarifying questions ** //
// Does it have multiple levels?
// Is there a restriction on the kind of vehicles that can park here?
// Does Valet have their own designated spots? If so, do those spots factor in to the publics perception of full/empty?

public enum SpotType
{
    Regular,
    Handicapped,
    Compact
}

public class ParkingLot
{

}

public class ParkingSpot
{
    public SpotType Type { get; set; }
    private bool _isEmpty { get; set; }

    public bool IsEmpty()
    {
        return this._isEmpty;
    }

    public void ParkCar(SpotType spotType = SpotType.Regular) {
        if (this._isEmpty) {
            throw new Exception("Unable to park in spot that is already occupied");
        }
        if (this.Type != SpotType.Regular || this.Type != spotType) {
            throw new Exception("Cannot park in designated spot");
        }

        this._isEmpty = false;
    }

    public void 
}