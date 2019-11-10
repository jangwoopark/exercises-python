#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the crosswordPuzzle function below.
def crosswordPuzzle(crossword, words):
    solution = []
    crosswordPuzzleHelper(crossword, words, solution)
    return solution.pop()

def crosswordPuzzleHelper(crossword, words, solution):
    for i in range(10):
        for j in range(10):
            fillWord(crossword, words, i, j, 'down', solution)
            fillWord(crossword, words, i, j, 'right', solution)

def fillWord(crossword, words, i, j, direction, solution):
    if len(words) == 0:
        return solution.append(crossword)
    # fill in word function succeeded
    if words[0] == ';': 
        return crosswordPuzzleHelper(crossword, words[1:], solution)
    # backtrack if i or j is out of bounds
    if (i < 0 or i >= 10 or j < 0 or j >= 10):
        return
    if crossword[i][j] == "+" :
        return
    # backtrack if first char in word != crossword char at i,j
    if crossword[i][j] != '-' and crossword[i][j] != words[0]:
        return
    # create new board and set i,j to be first char in word
    new_crossword = [list(s) for s in crossword]
    new_crossword[i][j] = words[0]
    new_crossword = ["".join(s) for s in new_crossword]
    if direction == 'down':
        fillWord(new_crossword, words[1:], i+1, j, 'down', solution)
    if direction == 'right':
        fillWord(new_crossword, words[1:], i, j+1, 'right', solution)
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    crossword = []

    for _ in range(10):
        crossword_item = input()
        crossword.append(crossword_item)

    words = input()

    result = crosswordPuzzle(crossword, words)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
