#!/usr/bin/env python3
# -*- coding: utf-8 -*

import sys

from grammar import Grammar

default_file = ""


def greibach(grammar: Grammar):
    return grammar


def main(argv):
    filename = './data/input/example.txt'
    lines = [line.rstrip('\n') for line in open(filename, 'r')]
    print(lines)
    res = []
    for counter, line in enumerate(lines):
        if line.isdigit():
            res.append(counter)
            res.append(int(line))
    print(res)
    if len(res) != 6:
        raise Exception("Неверное число номеров в файле")
    non_terminals = lines[res[0] + 1: res[1] + 1]
    terminals = lines[res[2] + 1: res[2] + res[3] + 1]
    rules = lines[res[4] + 1: res[4] + res[5] + 1]
    start_symbol = lines[-1:][0]
    grammar = Grammar(non_terminals, terminals, rules, start_symbol)
    gr_grammar = greibach(grammar)
    gr_grammar.save('./data/output/example.txt')


if __name__ == '__main__':
    main(sys.argv)
