/* 
Some guidelines for this specfic design
1: What if there are different modes of payments(cash, card, digital wallets).
2: What if there are different types of users paid/premium, freemium, enterprise customer(a company).
3: What if there are different types of hotels(luxury resort, 5 star, 3 start, economy), What if there are different services provided by a specific hotel(decorator pattern could be used).
4: What if there are expansions in different countries or integrating with different aggregator sites

Actors
1. User
2. Payment system
3. Hotel
4. Room
5. Employee

 */

public interface HasRate
{
    float getRate();

}

public abstract class Room : HasRate
{
    protected bool isOccupied;

    public List<BedType> beds;

    public bool IsOccupied()
    {
        return isOccupied;
    }

    public bool setOccupation(bool isOccupied)
    {
        this.isOccupied = isOccupied;
    }

    public abstract float getRate();
}

public class SingleRoomQueen : Room
{
    public SingleRoomQueen()
    {
        this.beds = new List<BedType> { BedType.Queen };
    }

    public float getRate()
    {
        return 100.0;
    }
}

public class DoiubleRoomTwin : Room
{
    public DoiubleRoomTwin()
    {
        this.beds = new List<BedType> { BedType.Twin, BedType.Twin };
    }

    public float getRate()
    {
        return 80.0;
    }
}

public abstract class RoomAmenityDecorator : Room
{
    protected Room room;

    public abstract float getRate();
}

public class HotTubAmenityDecorator : RoomAmenityDecorator
{
    public HotTubAmenityDecorator(Room room)
    {
        this.room = room;
    }

    public float getRate()
    {
        return this.room.getRate() + 10.0;
    }
}

public enum BedType
{
    Twin,
    Double,
    Full,
    Queen,
    King
}

public enum RoomType
{
    Single,
    Double,
    Executive
}

public abstract class Payment
{
    private float _amount;
    public float getAmount()
    {
        return _amount;
    }
    private void withdraw(float amount)
    {
        this._amount -= amount;
    }
    private void deposit(float amount)
    {
        this._amount += amount;
    }
    public abstract void Pay(int amount);
}

public class CashPayment : Payment
{
    public void pay(float amount)
    {
        if (amount > this.getAmount())
        {
            throw new PaymentExcpetion();
        }
        this.withdraw(amount);
    }
}

public class CreditPayment : Payment
{
    public void pay(float amount)
    {
        if (amount > this.getAmount())
        {
            throw new PaymentExcpetion();
        }
        this.withdraw(amount);
    }
}

public abstract class Customer
{
    protected string name;
    protected Date dateOfBirth;
    protected Payment paymentMethod;
    protected int percentDiscount;

    protected Customer(string name, Date dateOfBirth, Payment paymentMethod)
    {
        this.name = name;
        this.dateOfBirth = dob;
        this.paymentMethod = paymentMethod;
    }

    public void PayForRoom(float amount)
    {
        this.PaymentMethod.Pay(amount / this.percentDiscount);
    }
}

public class SilverMember : Customer
{
    public SilverMember(string name, Date dob, PaymentMethod pMethod) : base(name, dob, pMethod)
    {
        this.percentDiscount = 10;
    }
}

public class GoldMember : Customer
{
    public GoldMember(string name, Date dob, PaymentMethod pMethod) : base(name, dob, pMethod)
    {
        this.percentDiscount = 25;
    }
}
