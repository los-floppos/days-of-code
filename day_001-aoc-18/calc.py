#!/usr/bin/env python3
"""
Calculator to solve the puzzle of https://adventofcode.com/2020/day/18
"""
    # 2 * 3 + (4 * 5) becomes 26.
    # 5 + (8 * 3 + 9 + 3 * 4 * 3) becomes 437.
    # 5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4)) becomes 12240.
    # ((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2 becomes 13632.

with open('/Users/weber/Downloads/input-puzzle-aoc-18', encoding = 'utf-8') as file:
    line = file.readline()
    print(line)
    print(type(line))
    str(line)