// Design an OO parking lot. What classes and functions will it have. It should say full, empty, and also be able to find spot for Valet parking
// Three different types of parking: regular, handicapped and compact

// ** Clarifying questions ** //
// Does it have multiple levels?
// Is there a restriction on the kind of vehicles that can park here?
// Does Valet have their own designated spots? If so, do those spots factor in to the publics perception of full/empty?

public class ParkingLot
{

}


public enum SpotType
{
    Regular,
    Handicapped,
    Compact
}
public class ParkingSpot
{
    public SpotType Type { get; set; }
    private bool _isEmpty { get; set; }

    public bool IsEmpty()
    {
        return this._isEmpty;
    }
}