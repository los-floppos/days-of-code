#!/usr/bin/env python3
from typing import List
"""
Calculator to solve the puzzle of https://adventofcode.com/2020/day/18
"""
    # 2 * 3 + (4 * 5) becomes 26.
    # 5 + (8 * 3 + 9 + 3 * 4 * 3) becomes 437.
    # 5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4)) becomes 12240.
    # ((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2 becomes 13632.

def nested_precedence(line: List[str]) -> List[str]:
    """follows precedence ordering and returns a nested list"""
    nesting_lvl = 0
    nested = {nesting_lvl: []}       
    for char in line:
        print(f'{char}', end='')
        if char == "(":
            # print('shift right')
            nesting_lvl += 1
            nested[nesting_lvl] = [char]
            continue

        nested[nesting_lvl].append(char)
        if char == ")":
            # print('shift left')
            nesting_lvl -= 1

    return nested



with open('/Users/weber/Downloads/input-puzzle-aoc-18', encoding = 'utf-8') as file:
    line = file.readline()
    print(f'line: {line}')
    print(nested_precedence(line.replace(' ', '')))