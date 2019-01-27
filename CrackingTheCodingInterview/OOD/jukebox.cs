using System.Linq;
using System.Collections.Generic;
/*
    Design a jukebox using OO principles

    Some clarifying information
    - jukebox, CD, song, artist, playlist, display

    Actions
    - playlist creation, Cd seelction, song selection, queue for next song, get next song
 */

public abstract class BaseEntity
{
    public string id;
    public string name;
}

public class Song : BaseEntity
{
    public string artistId; // COuld also replace (or add) a string (or object) reference to the actual artist
    public string albumId;
}

public class Artist : BaseEntity
{
    List<string> Albums; // you could swap out the list of ids for the list of actual albums if you don't mind passing around large objects
}

public class Album : BaseEntity
{
    List<string> Songs; // same logic applies from above
}

public class Playlist : BaseEntity
{
    Queue<Song> Songs;

    public Song getNextSong()
    {
        return Songs.Dequeue();
    }

    public void addSong(Song s)
    {
        return Songs.Append(s);
    }

    public Song viewNextSong()
    {
        return Songs.Peek();
    }
}

public class Jukebox
{
    protected Display display;
    protected Jukebox jukebox;
    protected Song CurrentSong;
    protected Playlist playlist;


    private Jukebox() { }
    public Jukebox GetJukebox()
    {
        if (jukebox == null)
        {
            jukebox = new Jukebox();
        }

        return jukebox;
    }


}

public class Display
{

}