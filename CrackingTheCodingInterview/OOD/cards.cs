// Design the OOD model for a deck of cards that can be subclassed into a game of blackjack


public enum SuitType
{
    Diamonds,
    Hearts,
    Spades,
    Clubs
}

public class Suit
{
    private int _value { get; internal set; }
    private SuitType Suit { get; internal set; }
    public int GetValue() { return this._value; }
    public static SuitType getSuitFromValue(int value) { return SuitType.Clubs; } // Implement later
}

public class Deck
{
    private IList<Card> _cards { get; internal set; }
    private int _dealtIndex = 0;

    public Deck(IList<Card> cards)
    {
        this._cards = cards;
    }

    public void Shuffle()
    {
        // Do shuffling
    }
    public IList<Card> DealHand()
    {
        // Deal hand
    }
    public Card Deal()
    {
        // Deal single card
    }
}

public class Hand
{
    protected IList<Card> cards = new IList<Card>();
    public int score()
    {
        var score = 0;
        foreach (var card in cards)
        {
            value += card.GetValue();
        }
        return score;
    }

    public void AddCard(Card card)
    {
        cards.Add(card);
    }
}

public class Card
{
    protected int Value { get; internal set; } // 1 through 13
    protected Suit Suit { get; internal set; }

    public Card(int value, Suit suit)
    {
        this.Value = value;
        this.Suit = suit;
    }

    public abstract int GetValue() { return this.Value; }
    public Suit GetSuit() { return this.Suit; }
}

public class BlackJackCard : Card
{

    public BlackJackCard(int value, Suit suit)
    {
        super(value, suit);
    }

    public int GetValue()
    {
        if (this.IsFaceCard())
        {
            return 10;
        }
    }

    public int GetMinAmmount()
    {
        return this.Value();
    }

    public int GetMaxAmount()
    {
        if (this.IsAce()) { return 11; }
        return this.Value;
    }

    public bool IsFaceCard()
    {
        return this.Value >= 11 && this.Value <= 13;
    }

    public bool IsAce()
    {
        return this.Value == 1;
    }
}