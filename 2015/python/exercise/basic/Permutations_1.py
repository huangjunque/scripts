#!/usr/loca/env python
__author__ = 'junqueh'

import random
import itertools

def new_deck():
    return list(itertools.product(
            itertools.chain(xrange(2, 11), ('J', 'Q', 'K', 'A')),
            ('H', 'D', 'C', 'S'),
            ))

def show_deck(deck):
    p_deck = deck[:]
    while p_deck:
        row = p_deck[:13]
        p_deck = p_deck[13:]
        for j in row:
            print '%2s%s' %j,
        print

# GET a new deck, with the cards in order
deck = new_deck()
print 'Initial deck:'
show_deck(deck)

#Shuffle the deck to randomize the order
random.shuffle(deck)
print '\nShuffled deck:'
show_deck(deck)

# Deal 4 hanfs of 5 cards each
hands = [ [], [], [], [] ]

for i in xrange(5):
    for h in hands:
        h.append(deck.pop())

# Show the hands
print '\nHands:'
for n, h in enumerate(hands):
    print '%d: ' % (n+1),
    for c in h:
        print '%2s%s' % c,
    print

# Show the remainning deck
print '\nRemainning deck:'
show_deck(deck)

