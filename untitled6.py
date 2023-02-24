# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 21:35:44 2023

@author: Elizabeth

Game
"""
""" Items
"""
gold = {'value':1,'weight':0,'description':'shiny'}
sword = {'value':5,'weight':6,'description':'rusty'}


invintory = []

""" ADD item to invintory
"""

invintory = ["guts","tails","tails","tails","gold"]
guts_needed = 2
tails_needed = 3
gold_needed = 5
guts_num = invintory.count('guts')
tails_num = invintory.count('tails')
gold_num =invintory.count('gold')

if guts_needed != guts_num and tails_needed == tails_num and gold_num != gold_needed:
    print(f"You don't have enough guts. You need {guts_needed} guts, you have {guts_num}.")
    print(f"You don't have enough gold. You need {gold_needed} gold, you have {gold_num}.")
elif guts_needed != guts_num and tails_needed != tails_num and gold_num != gold_needed:
    print(f"You don't have enough guts. You need {guts_needed} guts, you have {guts_num}.")
    print(f"You don't have enough gold. You need {gold_needed} gold, you have {gold_num}.")
    print(f"You don't have enough tails. You need {tails_needed} tails, you have {tails_num}.")
elif guts_needed == guts_num and tails_needed != tails_num and gold_num != gold_needed:
    print(f"You don't have enough gold. You need {gold_needed} gold, you have {gold_num}.")
    print(f"You don't have enough tails. You need {tails_needed} tails, you have {tails_num}.")
elif guts_needed == guts_num and tails_needed == tails_num and gold_num != gold_needed:
    print(f"You don't have enough gold. You need {gold_needed} gold, you have {gold_num}.")
elif guts_needed != guts_num and tails_needed != tails_num and gold_num == gold_needed:
    print(f"You don't have enough guts. You need {guts_needed} guts, you have {guts_num}.")
    print(f"You don't have enough tails. You need {tails_needed} tails, you have {tails_num}.")
elif guts_needed == guts_num and tails_needed != tails_num and gold_num == gold_needed:
    print(f"You don't have enough tails. You need {tails_needed} tails, you have {tails_num}.")
elif guts_needed == guts_num and tails_needed == tails_num and gold_num == gold_needed:
    print("You make the item.")
    
