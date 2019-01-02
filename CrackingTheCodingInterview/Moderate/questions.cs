// 17.1
// Write a function to swap a number in place - without a temprary variable
public void ModerateOne()
{
    int[] myArray = new int[5] { 1, 2, 3, 4, 5 };

    // swap
    myArray[2] = myArray[2] - myArray[1];
    myArray[1] = myArray[2] + myArray[1];
    myArray[2] = myArray[1] - myArray[2];

    foreach (var element in myArray)
    {
        Console.WriteLine(element);
    }
}

// 17.2
// Design an algorith to figure out if someone has won a game of tic-tac-toe (3x3 board)

// [[x, x, x]
//  [x, x ,x]
//  [x, x, x]]
public char TicTacToeWinner(IList<IList<char>> board)
{
    for (int i = 0; i < board.Length(); i++)
    {
        // Check rows
        if (board[i][0] != null &&
            board[i][0] == board[i][1] &&
            board[i][1] == board[i][2])
        {
            return board[i][0];
        }

        // Check columns
        if (board[0][i] != null &&
            board[0][i] == board[1][i] &&
            board[1][i] == board[2][i])
        {
            return board[0][i];
        }

        // Check diagnonal (top to bottom)
        if (board[0][0] != null &&
            board[1][1] == board[0][0] &&
            board[1][1] == board[2][2])
        {
            return board[0][0];
        }

        // Check other diagonal
        if (board[2][0] != null &&
            board[2][0] == board[1][1] &&
            board[1][1] == board[0][2])
        {
            return board[2][0];
        }

        return null;
    }
}