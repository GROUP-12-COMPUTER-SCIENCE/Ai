// Function to initialize an empty board
function initializeBoard() {
    return [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ];
}

// Function to print the board
function printBoard(board) {
    board.forEach(row => console.log(row.join(' | ')));
    console.log();
}

// Function to check if a player has won
function checkWin(board, player) {
    // Check rows
    for (let row of board) {
        if (row.every(cell => cell === player)) return true;
    }

    // Check columns
    for (let col = 0; col < 3; col++) {
        if (board.every(row => row[col] === player)) return true;
    }

    // Check diagonals
    if (board[0][0] === player && board[1][1] === player && board[2][2] === player) return true;
    if (board[0][2] === player && board[1][1] === player && board[2][0] === player) return true;

    return false;
}

// Function to generate all possible next states for a player
function generateNextStates(board, player) {
    let nextStates = [];
    for (let i = 0; i < 3; i++) {
        for (let j = 0; j < 3; j++) {
            if (board[i][j] === ' ') {
                let newBoard = board.map(row => row.slice());
                newBoard[i][j] = player;
                nextStates.push(newBoard);
            }
        }
    }
    return nextStates;
}

// BFS function to explore all possible game states
function bfsTicTacToe() {
    let initialBoard = initializeBoard();
    let queue = [{ board: initialBoard, currentPlayer: 'X' }];

    while (queue.length > 0) {
        let { board, currentPlayer } = queue.shift();
        printBoard(board);

        if (checkWin(board, 'X')) {
            console.log("X wins!");
            return;
        }
        if (checkWin(board, 'O')) {
            console.log("O wins!");
            return;
        }

        let nextPlayer = currentPlayer === 'X' ? 'O' : 'X';
        let nextStates = generateNextStates(board, currentPlayer);
        nextStates.forEach(state => {
            queue.push({ board: state, currentPlayer: nextPlayer });
        });
    }

    console.log("It's a draw!");
}

// Run the BFS Tic-Tac-Toe game
bfsTicTacToe();
