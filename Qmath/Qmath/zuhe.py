#! /usr/bin/env python

import decimal

def zuhe(n, e):
	up = 1
	for i in range(e):
		up *= n - i
	return up

def birth(n, e):
	up = zuhe(n, e)
	down = n ** e
	decimal.getcontext().prec = 80
	up = decimal.Decimal(up)
	down = decimal.Decimal(down)
	return 1 - up / down
