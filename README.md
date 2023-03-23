# Change One Letter Solver
This project is a Python implementation of a Change One Letter game solver, which is a puzzle game where the objective is to convert one word into another word by changing one letter at a time. For example, converting the word 'POOL' to 'SAGE' can be done in the following steps: POOL, POLL, POLE, PALE, SALE, SAGE.

Strategy and Algorithms Used
The main strategy used in this implementation is to build an n-ary tree of all possible words that can be formed from the starting word by changing one letter at a time. The tree is built until the ending word is found, and then the solution path is traced back from the ending word to the starting word using the parent indices.

To build the tree, the solver starts with the starting word and find all the words that can be formed by changing one letter. The solver add these words as children of the starting word and repeat the process for each child word until the ending word is found or all possible words are explored. The solver uses a set to store all the four-letter words, and a list to store the n-ary tree of words.

To find the children of a word, the solver use regular expressions to match words that differ by only one letter. We define four regular expressions to match words that differ by the first, second, third, and fourth letters. The solver then matches each word in the set of all possible words against these regular expressions to find the children of the current word.

To trace back the solution path, the solver starts with the ending word and use the parent indices to move back to the starting word. The solver inserts each word in the solution path at the beginning of a list and print the list in reverse order to get the correct sequence of words.

How to Use
To use this implementation, you need to have Python 3 installed on your machine. You also need to download the words.txt file in the same directory as the Python script. This file should contain a list of most four-letter words (15,650 words), with each word on a separate line.

To run the script, simply execute the following command in a terminal:

```
python3 col-solver.py
```
You will be prompted to enter the starting and ending words. Enter the words and press enter. The script will then show the generation process of words and print the solution path.

'===IMPOSSIBLE===' if no path exists between two words
