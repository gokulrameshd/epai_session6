import pytest
import numpy as np 
from session6 import *

suit =['spades', 'hearts', 'diamonds','clubs']
num = ['ace',2,3,4,5,6,7,8,9,10,'jack','queen','king']
test_cases = {'royal_flush':[[('ace', 'hearts'),('jack', 'hearts'),('queen', 'hearts'),('king', 'hearts'),(10, 'hearts')],
                            [('ace', 'spades'),('jack', 'spades'),('queen', 'spades'),('king', 'spades'),(10, 'spades')],
                            [('ace', 'diamonds'),('jack', 'diamonds'),('queen', 'diamonds'),('king', 'diamonds'),(10, 'diamonds')],
                            [('ace', 'clubs'),('jack', 'clubs'),('queen', 'clubs'),('king', 'clubs'),(10, 'clubs')],
                            [('ace', 'hearts'),('jack', 'hearts'),('queen', 'hearts'),('king', 'hearts')],
                            [('ace', 'spades'),('jack', 'spades'),('queen', 'spades'),('king', 'spades')],
                            [('ace', 'diamonds'),('jack', 'diamonds'),('queen', 'diamonds'),('king', 'diamonds')],
                            [('ace', 'clubs'),('jack', 'clubs'),('queen', 'clubs'),('king', 'clubs')],
                            [('ace', 'hearts'),('jack', 'hearts'),('queen', 'hearts')],
                            [('ace', 'spades'),('jack', 'spades'),('queen', 'spades')],
                            [('ace', 'diamonds'),('jack', 'diamonds'),('queen', 'diamonds')],
                            [('ace', 'clubs'),('jack', 'clubs'),('queen', 'clubs')]],
             'straight_flush':[[(10, 'hearts'),(9, 'hearts'),(8, 'hearts'),(7, 'hearts'),(6, 'hearts')],
                              [(1, 'spades'),(2, 'spades'),(3, 'spades'),(4, 'spades'),(5, 'spades')],
                            [(2, 'diamonds'),(3, 'diamonds'),(4, 'diamonds'),(5, 'diamonds'),(6, 'diamonds')],
                            [(3, 'clubs'),(4, 'clubs'),(5, 'clubs'),(6, 'clubs'),(7, 'clubs')],
                            [(4, 'hearts'),(5, 'hearts'),(6, 'hearts'),(7, 'hearts')],
                            [(5, 'spades'),(6, 'spades'),(7, 'spades'),(8, 'spades')],
                            [(8, 'diamonds'),(9, 'diamonds'),(10, 'diamonds'),('jack', 'diamonds')],
                            [(9, 'clubs'),(10, 'clubs'),(11, 'clubs'),(8, 'clubs')],
                            [(10, 'hearts'),('jack', 'hearts'),(9, 'hearts')],
                            [('jack', 'spades'),(10, 'spades'),(9, 'spades')],
                            [(6, 'diamonds'),(4, 'diamonds'),(5, 'diamonds')],
                            [(3, 'clubs'),(1, 'clubs'),(2, 'clubs')]],
             'four_kind':[[('queen','hearts'),('queen','clubs'),('queen','spades'),('queen','diamonds'),('king','hearts')],
                         [('king','hearts'),('king','clubs'),('king','spades'),('king','diamonds'),('queen','hearts')],
                         [('jack','hearts'),('jack','clubs'),('jack','spades'),('jack','diamonds'),('king','hearts')],
                         [('ace','hearts'),('ace','clubs'),('ace','spades'),('ace','diamonds'),('queen','hearts')],
                         [(2,'hearts'),(2,'clubs'),(2,'spades'),(2,'diamonds'),('king','hearts')],
                         [(5,'hearts'),(5,'clubs'),(5,'spades'),(5,'diamonds')],
                         [(8,'hearts'),(8,'clubs'),(8,'spades'),(8,'diamonds')],
                         [(3,'hearts'),(3,'clubs'),(3,'spades'),(3,'diamonds')],
                         [(10,'hearts'),(10,'clubs'),(10,'spades'),(10,'diamonds')],
                         [(2,'hearts'),(2,'clubs'),(2,'spades'),(2,'diamonds')]],
             'full_house':[[('queen','hearts'),('queen','clubs'),('queen','spades'),('king','diamonds'),('king','hearts')],
                         [('king','hearts'),('king','clubs'),('king','spades'),('queen','diamonds'),('queen','hearts')],
                         [('jack','hearts'),('jack','clubs'),('jack','spades'),('king','diamonds'),('king','hearts')],
                         [('queen','hearts'),('queen','clubs'),('ace','spades'),('ace','diamonds'),('ace','hearts')]],
             'flush':[[('king','hearts'),(1,'hearts'),(5,'hearts'),(8,'hearts'),(9,'hearts')],
                     [('king','clubs'),(1,'clubs'),(5,'clubs'),(8,'clubs'),(9,'clubs')],
                     [(10,'clubs'),(1,'clubs'),(5,'clubs'),(8,'clubs'),(9,'clubs')],
                     [(2,'spades'),(1,'spades'),(5,'spades'),(8,'spades'),(9,'spades')],
                     [(2,'spades'),(1,'spades'),(5,'spades'),(8,'spades')],
                     [(2,'spades'),(1,'spades'),(5,'spades')]],
             'straight': [[(8,'hearts'),(7,'spades'),(6,'clubs'),(5,'diamonds'),(4,'hearts')],
                         [(1,'hearts'),(2,'spades'),(3,'clubs'),(4,'diamonds'),(5,'hearts')],
                         [(6,'hearts'),(7,'spades'),(8,'clubs'),(9,'diamonds'),(10,'diamonds')],
                         [(6,'hearts'),(7,'spades'),(8,'clubs'),(9,'diamonds'),(10,'clubs')],
                         [(6,'hearts'),(7,'spades'),(8,'clubs'),(9,'diamonds'),(10,'spades')],
                         [(11,'hearts'),(7,'spades'),(8,'clubs'),(9,'diamonds'),(10,'hearts')]],
             'three_kind':[[('queen','hearts'),('queen','spades'),('queen','clubs'),(5,'diamonds'),(4,'hearts')],
                          [('ace','hearts'),(4,'spades'),(4,'clubs'),(5,'diamonds'),(4,'hearts')],
                          [('queen','hearts'),(5,'spades'),(5,'clubs'),(5,'diamonds'),(4,'hearts')],
                          [('queen','hearts'),('queen','spades'),('queen','clubs'),(5,'diamonds')],
                          [('ace','hearts'),(4,'spades'),(4,'clubs'),(4,'diamonds')],
                          [('queen','hearts'),(5,'spades'),(5,'clubs'),(5,'diamonds')]],
             'two_pair':[[('queen','hearts'),('queen','spades'),('ace','clubs'),(4,'diamonds'),(4,'hearts')],
                        [('queen','hearts'),('queen','spades'),('ace','clubs'),('ace','diamonds'),(4,'hearts')],
                        [('queen','hearts'),('ace','spades'),('ace','clubs'),(4,'diamonds'),(4,'hearts')]],
             'one_pair':[[('queen','hearts'),('queen','spades'),('ace','clubs'),(3,'diamonds'),(4,'hearts')],
                        [('king','hearts'),('queen','spades'),('ace','clubs'),('ace','diamonds'),(4,'hearts')],
                        [('queen','hearts'),('ace','spades'),('ace','clubs'),(2,'diamonds'),(4,'hearts')]],
             'high_card':[[('queen','hearts'),('jack','spades'),('ace','clubs'),(2,'diamonds'),(4,'hearts')],
                         [('queen','hearts'),(6,'spades'),('ace','clubs'),(2,'diamonds'),(4,'hearts')],
                         [('king','hearts'),(8,'spades'),('ace','clubs'),(2,'diamonds'),(4,'hearts')],
                         [(5,'hearts'),('jack','spades'),('ace','clubs'),(2,'diamonds'),(4,'hearts')],
                         [('queen','hearts'),('jack','spades'),('ace','clubs'),(2,'diamonds')],
                         [('queen','hearts'),(6,'spades'),('ace','clubs'),(2,'diamonds')],
                         [('king','hearts'),(3,'spades'),('ace','clubs'),(2,'diamonds')],
                         [(5,'hearts'),('jack','spades'),('ace','clubs'),(2,'diamonds')],
                         [('queen','hearts'),('jack','spades'),('ace','clubs')],
                         [('queen','hearts'),(6,'spades'),('ace','clubs')],
                         [('king','hearts'),(2,'spades'),('ace','clubs')],
                         [(5,'hearts'),('jack','spades'),('ace','clubs')]]}


# classes = {'royal_flush':1 , 'straight_flush':2 , 'four_kind':3,
#             'full_house':4 , 'flush' : 5 , 'straight':6 ,
#             'three_kind': 7 , 'two_pair' : 8 , 'one_pair' : 9,
#             'high_card': 10 ,'' : 11}
# five
test_case_1 = {'a' : test_cases['royal_flush'][0] , "b" : test_cases['straight_flush'][0]}
test_case_2 = {'a' : test_cases['royal_flush'][0] , "b" : test_cases['four_kind'][0]}
test_case_3 = {'a' : test_cases['royal_flush'][0] , "b" : test_cases['full_house'][0]}
test_case_4 = {'a' : test_cases['royal_flush'][0] , "b" : test_cases['flush'][0]}
test_case_5 = {'a' : test_cases['royal_flush'][0] , "b" : test_cases['straight'][0]}
test_case_6 = {'a' : test_cases['royal_flush'][0] , "b" : test_cases['three_kind'][0]}
test_case_7 = {'a' : test_cases['royal_flush'][0] , "b" : test_cases['two_pair'][0]}
test_case_8 = {'a' : test_cases['royal_flush'][0] , "b" : test_cases['one_pair'][0]}
test_case_9 = {'a' : test_cases['royal_flush'][0] , "b" : test_cases['high_card'][0]}

test_case_10 = {'a' : test_cases['high_card'][0] , "b" : test_cases['straight_flush'][0]}
test_case_11 = {'a' : test_cases['high_card'][0] , "b" : test_cases['four_kind'][0]}
test_case_12 = {'a' : test_cases['high_card'][0] , "b" : test_cases['full_house'][0]}
test_case_12 = {'a' : test_cases['high_card'][0] , "b" : test_cases['flush'][0]}
test_case_13 = {'a' : test_cases['high_card'][0] , "b" : test_cases['straight'][0]}
test_case_14= {'a' : test_cases['high_card'][0] , "b" : test_cases['three_kind'][0]}
test_case_15 = {'a' : test_cases['high_card'][0] , "b" : test_cases['two_pair'][0]}
test_case_16 = {'a' : test_cases['high_card'][0] , "b" : test_cases['one_pair'][0]}
test_case_17 = {'a' : test_cases['high_card'][0] , "b" : test_cases['royal_flush'][0]}

test_case_18 = {'a' : test_cases['flush'][1] , "b" : test_cases['straight_flush'][0]}#b,b,b,Draw,a,a,b,a,b
test_case_19 = {'a' : test_cases['flush'][1] , "b" : test_cases['four_kind'][0]}#b
test_case_20 = {'a' : test_cases['flush'][1] , "b" : test_cases['full_house'][0]}#b
test_case_21 = {'a' : test_cases['flush'][1] , "b" : test_cases['flush'][0]}#Draw
test_case_22 = {'a' : test_cases['flush'][1] , "b" : test_cases['straight'][0]}#a
test_case_23= {'a' : test_cases['flush'][1] , "b" : test_cases['three_kind'][0]}#a
test_case_24 = {'a' : test_cases['flush'][1] , "b" : test_cases['two_pair'][0]}#a
test_case_25 = {'a' : test_cases['flush'][1] , "b" : test_cases['one_pair'][0]}#a
test_case_26 = {'a' : test_cases['flush'][1] , "b" : test_cases['royal_flush'][0]}#b

# classes = {'royal_flush':1 , 'straight_flush':2 , 'four_kind':3,
#             'full_house':4 , 'flush' : 5 , 'straight':6 ,
#             'three_kind': 7 , 'two_pair' : 8 , 'one_pair' : 9,
#             'high_card': 10 ,'' : 11}

test_case_27 = {'a' : test_cases['three_kind'][1] , "b" : test_cases['straight_flush'][0]}#b,b,b,a,a,a,a,b
test_case_28 = {'a' : test_cases['straight'][1] , "b" : test_cases['four_kind'][0]}#b
test_case_29 = {'a' : test_cases['one_pair'][1] , "b" : test_cases['full_house'][0]}#b
test_case_30 = {'a' : test_cases['two_pair'][1] , "b" : test_cases['flush'][0]}#b
test_case_31 = {'a' : test_cases['four_kind'][1] , "b" : test_cases['straight'][0]}#a
test_case_32= {'a' : test_cases['straight_flush'][1] , "b" : test_cases['three_kind'][0]}#a
test_case_33 = {'a' : test_cases['royal_flush'][1] , "b" : test_cases['two_pair'][0]}#a
test_case_34 = {'a' : test_cases['full_house'][1] , "b" : test_cases['one_pair'][0]}#a
test_case_35 = {'a' : test_cases['one_pair'][1] , "b" : test_cases['royal_flush'][0]}#b





def test_royal_flush():
    for i in range(len(test_cases['royal_flush'])):
        a_res ,a_sum_sort,a_sum_num = get_class(test_cases['royal_flush'][i])
        print(a_res)
        assert np.unique(a_res)[0] == 'royal_flush' ,"worked!!"

def test_straight_flush():
    for i in range(len(test_cases['straight_flush'])):
        a_res ,a_sum_sort,a_sum_num = get_class(test_cases['straight_flush'][i])
        assert np.unique(a_res)[0] == 'straight_flush' ,"worked!!"
#four_kind
def test_four_kind():
    for i in range(len(test_cases['four_kind'])):
        a_res ,a_sum_sort,a_sum_num = get_class(test_cases['four_kind'][i])
        assert np.unique(a_res)[0] == 'four_kind' ,"worked!!"

def test_full_house():
    for i in range(len(test_cases['full_house'])):
        a_res ,a_sum_sort,a_sum_num = get_class(test_cases['full_house'][i])
        assert np.unique(a_res)[0] == 'full_house' ,"worked!!"
    #full_
def test_flush():
    for i in range(len(test_cases['flush'])):
        a_res ,a_sum_sort,a_sum_num = get_class(test_cases['flush'][i])
        assert np.unique(a_res)[0] == 'flush' ,"worked!!"

def test_straight():
    for i in range(len(test_cases['straight'])):
        a_res ,a_sum_sort,a_sum_num = get_class(test_cases['straight'][i])
        assert np.unique(a_res)[0] == 'straight' ,"worked!!"


def test_three_kind():
    for i in range(len(test_cases['three_kind'])):
        a_res ,a_sum_sort,a_sum_num = get_class(test_cases['three_kind'][i])
        assert np.unique(a_res)[0] == 'three_kind' ,"worked!!"

def test_two_pair():
    for i in range(len(test_cases['two_pair'])):
        a_res ,a_sum_sort,a_sum_num = get_class(test_cases['two_pair'][i])
        assert np.unique(a_res)[0] == 'two_pair' ,"worked!!"

def test_one_pair():
    for i in range(len(test_cases['one_pair'])):
        a_res ,a_sum_sort,a_sum_num = get_class(test_cases['one_pair'][i])
        assert np.unique(a_res)[0] == 'one_pair' ,"worked!!"

def test_high_card():
    for i in range(len(test_cases['high_card'])):
        a_res ,a_sum_sort,a_sum_num = get_class(test_cases['high_card'][i])
        print(np.unique(a_res)[0] )
        assert np.unique(a_res)[0] == 'high_card' ,"worked!!"


def test_create_deck():
    deck = []
    for i in num:
        for j in suit:
            a = (i,j)
            deck.append(a)
    d1 = create_deck()
    assert d1 == deck , "worked!!!!!"

def test_create_deck_spec():
    deck = []
    for i in num :
        for j in suit:
            a = (i,j)
            deck.append(a)
    d1 = create_deck_spec()
    assert d1 == deck , "worked!!!!!"




def test_get_winner_1():
    a = test_case_1['a']
    b = test_case_1['b']
    winner = get_winner(a,b)
    assert winner == 'a' , "worked!!!!!"

def test_get_winner_2():
    a = test_case_2['a']
    b = test_case_2['b']
    winner = get_winner(a,b)
    assert winner == 'a' , "worked!!!!!"

def test_get_winner_3():
    a = test_case_3['a']
    b = test_case_3['b']
    winner = get_winner(a,b)
    assert winner == 'a' , "worked!!!!!"

def test_get_winner_4():
    a = test_case_4['a']
    b = test_case_4['b']
    winner = get_winner(a,b)
    assert winner == 'a' , "worked!!!!!"

def test_get_winner_5():
    a = test_case_5['a']
    b = test_case_5['b']
    winner = get_winner(a,b)
    winner == 'a' , "worked!!!!!"

def test_get_winner_6():
    a = test_case_6['a']
    b = test_case_6['b']
    winner = get_winner(a,b)
    assert winner == 'a' , "worked!!!!!"

def test_get_winner_7():
    a = test_case_7['a']
    b = test_case_7['b']
    winner = get_winner(a,b)
    assert winner == 'a' , "worked!!!!!"

def test_get_winner_8():
    a = test_case_8['a']
    b = test_case_8['b']
    winner = get_winner(a,b)
    assert winner == 'a' , "worked!!!!!"

def test_get_winner_9():
    a = test_case_9['a']
    b = test_case_9['b']
    winner = get_winner(a,b)
    assert winner == 'a' , "worked!!!!!"

def test_get_winner_10():
    a = test_case_10['a']
    b = test_case_10['b']
    winner = get_winner(a,b)
    assert winner == 'b' , "worked!!!!!"

def test_get_winner_11():
    a = test_case_11['a']
    b = test_case_11['b']
    winner = get_winner(a,b)
    assert winner == 'b' , "worked!!!!!"

def test_get_winner_12():
    a = test_case_12['a']
    b = test_case_12['b']
    winner = get_winner(a,b)
    assert winner == 'b' , "worked!!!!!"

def test_get_winner_13():
    a = test_case_13['a']
    b = test_case_13['b']
    winner = get_winner(a,b)
    assert winner == 'b' , "worked!!!!!"

def test_get_winner_14():
    a = test_case_14['a']
    b = test_case_14['b']
    winner = get_winner(a,b)
    assert winner == 'b' , "worked!!!!!"

def test_get_winner_15():
    a = test_case_15['a']
    b = test_case_15['b']
    winner = get_winner(a,b)
    assert winner == 'b' , "worked!!!!!"

def test_get_winner_16():
    a = test_case_16['a']
    b = test_case_16['b']
    winner = get_winner(a,b)
    assert winner == 'b' , "worked!!!!!"

def test_get_winner_17():
    a = test_case_17['a']
    b = test_case_17['b']
    winner = get_winner(a,b)
    assert winner == 'b' , "worked!!!!!"

#a,b,b,Draw,a,a,b,a,b
def test_get_winner_18():
    a = test_case_18['a']
    b = test_case_18['b']
    winner = get_winner(a,b)
    assert winner == 'b' , "worked!!!!!"

def test_get_winner_19():
    a = test_case_19['a']
    b = test_case_19['b']
    winner = get_winner(a,b)
    assert winner == 'b' , "worked!!!!!"

def test_get_winner_20():
    a = test_case_20['a']
    b = test_case_20['b']
    winner = get_winner(a,b)
    assert winner == 'b' , "worked!!!!!"

def test_get_winner_21():
    a = test_case_21['a']
    b = test_case_21['b']
    winner = get_winner(a,b)
    assert winner == 'Draw' , "worked!!!!!"

def test_get_winner_22():
    a = test_case_22['a']
    b = test_case_22['b']
    winner = get_winner(a,b)
    assert winner == 'a' , "worked!!!!!"

def test_get_winner_23():
    a = test_case_23['a']
    b = test_case_23['b']
    winner = get_winner(a,b)
    assert winner == 'a' , "worked!!!!!"

def test_get_winner_24():
    a = test_case_24['a']
    b = test_case_24['b']
    winner = get_winner(a,b)
    assert winner == 'a' , "worked!!!!!"

def test_get_winner_25():
    a = test_case_25['a']
    b = test_case_25['b']
    winner = get_winner(a,b)
    assert winner == 'a' , "worked!!!!!"

def test_get_winner_26():
    a = test_case_26['a']
    b = test_case_26['b']
    winner = get_winner(a,b)
    assert winner == 'b' , "worked!!!!!"

def test_get_winner_27():
    a = test_case_27['a']
    b = test_case_27['b']
    winner = get_winner(a,b)
    assert winner == 'b' , "worked!!!!!"

def test_get_winner_28():
    a = test_case_28['a']
    b = test_case_28['b']
    winner = get_winner(a,b)
    assert winner == 'b' , "worked!!!!!"

def test_get_winner_29():
    a = test_case_29['a']
    b = test_case_29['b']
    winner = get_winner(a,b)
    assert winner == 'b' , "worked!!!!!"

def test_get_winner_30():
    a = test_case_30['a']
    b = test_case_30['b']
    winner = get_winner(a,b)
    assert winner == 'b' , "worked!!!!!"

def test_get_winner_31():
    a = test_case_31['a']
    b = test_case_31['b']
    winner = get_winner(a,b)
    assert winner == 'a' , "worked!!!!!"

def test_get_winner_32():
    a = test_case_32['a']
    b = test_case_32['b']
    winner = get_winner(a,b)
    assert winner == 'a' , "worked!!!!!"

def test_get_winner_33():
    a = test_case_33['a']
    b = test_case_33['b']
    winner = get_winner(a,b)
    winner == 'a' , "worked!!!!!"

def test_get_winner_34():
    a = test_case_34['a']
    b = test_case_34['b']
    winner = get_winner(a,b)
    winner == 'a' , "worked!!!!!"

def test_get_winner_35():
    a = test_case_35['a']
    b = test_case_35['b']
    winner = get_winner(a,b)
    winner == 'b' , "worked!!!!!"


# #b,b,b,a,a,a,a,b

