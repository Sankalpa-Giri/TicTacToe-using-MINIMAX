# Tic-Tac-Toe Using Minimax (Alpha-Beta Pruning)

## **Overview**

This project implements a **Tic-Tac-Toe game** where a human player competes against an AI agent powered by the **Minimax algorithm with Alpha-Beta pruning**. The human plays as `'X'` (maximizer), while the AI plays as `'O'` (minimizer). The game runs entirely in the console with colored output for enhanced readability.

---

## **1. Features**

### ✔ Fully interactive console-based Tic-Tac-Toe

### ✔ AI agent using Minimax + Alpha-Beta pruning

### ✔ Valid move checking and error handling

### ✔ Highlights wins, losses, and draws using color-coded text

### ✔ Human can choose who plays first

---

## **2. Board Representation**

The board is represented as a **list of 9 characters**, each representing a cell:

* `' '` → empty cell
* `'X'` → human
* `'O'` → AI

Index layout:

```
0 | 1 | 2
3 | 4 | 5
6 | 7 | 8
```

Players input a number (0–8) to place their symbol.

---

## **3. Color System**

A small `Colors` class defines ANSI escape codes:

* `RED` → errors
* `GREEN` → human win
* `YELLOW` → agent win
* `BLUE` → information (new game, draws)
* `RESET` → resets console

Used throughout the script to improve readability.

---

## **4. Key Functions**

### ### **4.1 `print_board(board)`**

Displays the board in the console in a 3×3 grid.

---

### **4.2 `check_winner(board, player)`**

Checks whether the given `player` (`'X'` or `'O'`) has a winning combination.

* Returns **True** if any of the 8 possible win patterns match.
* Otherwise returns **False**.

---

### **4.3 `check_draw(board)`**

Returns **True** when no empty cells remain.
Used after each turn to detect draw conditions.

---

## **5. Minimax Algorithm**

### **5.1 Goal of Minimax**

* Human (`X`) tries to **maximize** the score.
* Agent (`O`) tries to **minimize** the score.

The scoring system:

* `+1` → Human wins
* `-1` → Agent wins
* `0` → Draw

---

### **5.2 `minimax(board, is_maximizing, alpha, beta)`**

This is the core AI function.

#### **Parameters:**

* `is_maximizing`: whether it's `'X'`'s turn.
* `alpha`: best score the maximizer has found so far.
* `beta`: best score the minimizer has found so far.

#### **Returns:**

An integer score { -1, 0, 1 } for the board.

#### **Logic Flow:**

1. Check terminal states (win/loss/draw).
2. If maximizing:

   * Try all possible `'X'` moves.
   * Update `alpha`.
   * Stop exploring if `alpha >= beta` (pruning).
3. If minimizing:

   * Try all possible `'O'` moves.
   * Update `beta`.
   * Prune when `alpha >= beta`.

Alpha-Beta pruning helps reduce the number of recursive calls, making the AI faster.

---

## **6. Agent Move Selection**

### **6.1 `best_move(board)`**

* Loops over all possible moves.
* Simulates the move.
* Calls minimax to evaluate resulting board.
* Chooses the move with the **lowest score** (best for `'O'`).

Returns the index of the optimal move.

---

## **7. Game Loop**

### **7.1 `game_loop(board)`**

This function runs the core gameplay.

#### Responsibilities:

* Display board
* Accept and validate human moves
* Detect invalid inputs (non-numeric or out of range)
* Check win/draw conditions after each move
* Compute AI move using `best_move()`
* Announce results with colored messages

The loop continues until:

* Human wins
* AI wins
* Draw occurs

---

## **8. Program Entry Point**

The script starts by asking:

```
1 for Human first
2 for Agent first
```

If the agent starts, it makes a move immediately using `best_move()`.
Then the main game loop begins.

---

## **9. Example Run**

```
New Game.
1 for Human. 2 for Agent
Enter your choice: 1
| | | |
| | | |
| | | |
Make a move between 0-8: 4
...
```

Gameplay continues with alternating turns.

---

## **10. Possible Improvements**

### ⭐ Make AI Human-like

* Introduce randomness
* Limit depth of minimax
* Mix minimax with heuristics

### ⭐ Add Better UI

* Pygame GUI
* Tkinter UI
* Web-based UI with Flask or React

### ⭐ Add Logging and Analytics

* Track win rates
* Track move patterns
* Evaluate human performance vs perfect AI

---

## **11. Conclusion**

This script demonstrates a fully functional Minimax-based AI for Tic-Tac-Toe with alpha-beta pruning, displayed in a console-friendly interface with colored text. It provides a strong foundation for learning game AI and can be expanded with UI, difficulty settings, or alternate heuristics.
