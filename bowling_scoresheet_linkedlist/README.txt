# Bowling Scoresheet (Linked List)

This is a command-line based **TEN-PIN BOWLING SCOREHSEET** implemented using a **doubly-linked-list**.
The exercise began as a 4kyu challenge from Codewars. I adapted the program to use a linked list to use it as an outlet for my study of datastructures.

Each frame is modeled as a node in the list, allowing for:
- **Retrospective scoring**: the use of `prev` pointers seemed a natural fit to mirror the real-life flow of scoring in a game where previous frames points are adjusted retrospectively after a strike or spare has been scored by being awarded points from the current frame.
- **Sequential traversal**: Iterating through the list simplifies score calculation and debugging.

The linked list approach was chosen deliberately to explore data structure implementation and practice reasoning about dynamic relationships between nodes.

While educational, this structure is **not optimized for real-world usability** or maintainability. In practical applications, a simpler list or object-based approach would likely be more appropriate.

## Getting Started

Install dependencies:

pip3 install -r requirements.txt

Running program: python3 main.py

Running Tests
To run all unit and functional tests from the project root use: PYTHONPATH=. pytest

## Usage Example

To simulate a perfect game:
Note, a full game's score of 10 frames must be entered as a string with all 10 frames scores. Frame scores use digits 0-9, '/' for spare (appearing as the 2nd character in the frame) and 'X' for strike (second digit in frame score is omitted). 

1. Using the python interpreter:
python3 -i bowling_linkedlist.py

game = Game()
game.load_scores('X X X X X X X X X XXX')
game.calculate_score()
print(game.print_frames())

This will output a formatted frame-by-frame score breakdown, correctly applying bonus rules for strikes and spares.


2. Using the cli:
first uncomment the if __name__ == "__main__" and other code at the bottom of bowling_linkedlist.py to allow command line version to run.

python3 bowling_linkedlist.py "X X X X X X X X X XXX"


