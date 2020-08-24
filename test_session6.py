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
