# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 18:51:24 2017

@author: Rodion
"""
import logging

logging.basicConfig(level=logging.ERROR)

def cross(A, B):
    "Cross product of elements in A and elements in B."
    return [a+b for a in A for b in B]

assignments = []
rows = 'ABCDEFGHI'
cols = '123456789'
boxes = cross(rows, cols)
row_units = [cross(r, cols) for r in rows]
column_units = [cross(rows, c) for c in cols]
square_units = [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')]
diagonal_units = [[rows[i]+cols[i] for i in range(len(rows))],[rows[i]+cols[len(rows)-i-1] for i in range(len(rows))]]
unitlist = row_units + column_units + square_units + diagonal_units
units = dict((s, [u for u in unitlist if s in u]) for s in boxes)
peers = dict((s, set(sum(units[s],[]))-set([s])) for s in boxes)   