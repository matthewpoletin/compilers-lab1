#!/usr/bin/env python3
# -*- coding: utf-8 -*


class Grammar:
    """
	Класс для работы с граматикой
    """

    # Нетерминалы N
    nonTerminals = []
    # Терминалы E
    terminals = []
    # Правила P
    rules = []
    # Начальный символ S
    startSymbol = None

    def __init__(self, non_terminals: list, terminals: list, rules: list, start_symbol: str):
        """
        :param non_terminals:
        :param terminals:
        :param rules:
        :param start_symbol:
        """
        self.nonTerminals = non_terminals
        self.terminals = terminals
        self.rules = rules
        self.startSymbol = ''

    def save(self, filename: str):
        """
        :param filename:
        :return:
        """
        file = open(filename, 'w')
        file.write("{}\n".format(len(self.nonTerminals)))
        for non_terminal in self.nonTerminals:
            file.write(non_terminal + "\n")
        file.write("{}\n".format(len(self.terminals)))
        for terminal in self.terminals:
            file.write(terminal + "\n")
        file.write("{}\n".format(len(self.rules)))
        for rule in self.rules:
            file.write("{}\n".format(rule))
        file.write("{}\n".format(self.startSymbol))
        file.close()
        return filename
