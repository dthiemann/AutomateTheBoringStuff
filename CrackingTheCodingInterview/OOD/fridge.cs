/*
    Using OOP design patterns to design a refridgerator

    Actors
    - User
    - Food item
    - Container
    - Fridge
    - Freezer
    - Crispers
    - Ice/Water machine
 */

public interface HasWaterIceDispenser
{
    void getWater();
    void getIce();
}

public class Refridgerator
{

}

public class FoodItem
{
    public string name;
    public string description;
}

public class RefridgeratorWithWaterIce : Refridgerator, HasWaterIceDispenser
{
    public void getWater()
    {
        Console.WriteLine("get water");
    }
    public void getIce()
    {
        Console.WriteLine("get ice")
    }
}