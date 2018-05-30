#!/usr/bin/env python3
# -*- coding: utf-8 -*


class Grammar:
	"""

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
		self.startSymbol = str

	def save(self, filename: str):
		"""
		:param filename:
		:return:
		"""
		file = open(filename, 'w')
		for rule in self.rules:
			file.write(rule)
		file.close()
		return filename
