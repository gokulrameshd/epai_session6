import numpy as np 

suit =['spades', 'hearts', 'diamonds','clubs']
val = ['ace',2,3,4,5,6,7,8,9,10,'jack','queen','king']
deck = []

def create_deck():
    '''This function creates deck of cards using list coprehension'''
    suit =['Spades', 'Hearts', 'Diamonds','Clubs']
    num = ['ace',2,3,4,5,6,7,8,9,10,'jack','queen','king']
    # list(map(lambda a,b,c,d : for i in suit )
    l = [(s,n) for s in suit for n in num]
    return l


def create_deck_spec(suit,num):
    '''This function creates deck of cards using map , lambda , zip functions'''
    c = []
    r =list(map(lambda a : [(a[0],a[1][0]),(a[0],a[1][1]),(a[0],a[1][2]),(a[0],a[1][3])] , zip(num,[suit for i in range(len(num))])))
    for i in r:
        c += i
    return c


#  POKER

suit =['spades', 'hearts', 'diamonds','clubs']
num = ['ace',2,3,4,5,6,7,8,9,10,'jack','queen','king']



def get_class(a): 
    """This function get the class of the cards in hand or collection"""
    num = []
    count = []
    suit = []
    sort =[]
    res =[]
    for i in a:
        if type(i[0]) == str:
            count.append(10)
            if i[0] == 'ace':
                sort.append(1)
            elif i[0] == 'jack':
                sort.append(11)
            elif i[0] == 'queen':
                sort.append(12)
            elif i[0] == 'king':
                sort.append(13)
        else:
            count.append(i[0])
            sort.append(i[0])
        num.append(i[0])
        suit.append(i[1])

    if (len(np.unique(suit)) == 1)& (sum(count) == 10 *len(a)) :
        res.append('royal_flush')


    elif ((len(np.unique(suit)) == 1) & (sum(count) != 10 * len(a)) & (len(np.unique(sort)) == len(a))
          & (list(np.sort(sort)) == [x for x in range(min(sort),max(sort)+1)])):
        res.append('straight_flush')
        
    elif ((len(np.unique(suit)) == 4) 
          & ((len(np.unique(num)) <= 2 )
             & ((sort.count(np.unique(sort)[0]) ==4) or (sort.count(np.unique(sort)[1]) ==4)  ))):
        res.append('four_kind')

    elif (sum(count) == 10 * len(a)) & (len(np.unique(suit)) < len(a)):
        res.append("full_house")

    elif ((len(np.unique(suit)) == 1) & (sum(count) < 10 * len(a)) 
          & (len(np.unique(num)) == len(a)) 
          & (list(np.sort(sort)) != [x for x in range(min(sort),max(sort)+1)])):
        res.append('flush')


    elif (len(np.unique(suit))  > (len(a)/2)) & (list(np.sort(sort)) == [x for x in range(min(sort),max(sort)+1)]):
        res.append('straight')

    elif (((len(np.unique(suit)) >= 3) & (len(np.unique(num)) <= 3))
         & ((sort.count(np.unique(sort)[0])==3 )or(sort.count(np.unique(sort)[1])==3) or(sort.count(np.unique(sort)[-1])==3) )):
       res.append('three_kind')

    elif (((sort.count(np.unique(sort)[0])==2 )
              +(sort.count(np.unique(sort)[1])==2)
              +(sort.count(np.unique(sort)[-1])==2))==2 ):
        res.append('two_pair')


    elif ((((len(a) ==5 ) &((sort.count(np.unique(sort)[0])==2 )
           +(sort.count(np.unique(sort)[1])==2)
           +(sort.count(np.unique(sort)[-1])==2)+(sort.count(np.unique(sort)[-2])==2)==1))
         or ((len(a) == 4) &((sort.count(np.unique(sort)[0])==2 )
           +(sort.count(np.unique(sort)[1])+(sort.count(np.unique(sort)[-1])==2)==2)))  
         or ((len(a) < 4) &((sort.count(np.unique(sort)[0])==2 )
           +(sort.count(np.unique(sort)[1])==2))))):
        res.append('one_pair')

    elif (len(np.unique(sort)) == len(a)) & (len(np.unique(suit)) >= (len(a)-1)):
        res.append('high_card')
    else:
        res.append('')



    return res ,sum(sort),sum(count)


def get_winner(a,b):
    
    classes = {'royal_flush':1 , 'straight_flush':2 , 'four_kind':3,
                'full_house':4 , 'flush' : 5 , 'straight':6 ,
                'three_kind': 7 , 'two_pair' : 8 , 'one_pair' : 9,
                'high_card': 10 ,'' : 11}
    a_res ,a_sum_sort,a_sum_num = get_class(a)
    b_res ,a_sum_sort,b_sum_num = get_class(b)

    if classes[a_res[0]] < classes[b_res[0]]:
        winnner = 'a'
    elif classes[a_res[0]] > classes[b_res[0]]:
        winner = 'b'
    else :
        if a_sum_num > b_sum_num :
            winnner = 'a'
        elif a_sum_num < b_sum_num :
            winnner = 'b'
        else:
            winnner = 'Nobody'





    
    