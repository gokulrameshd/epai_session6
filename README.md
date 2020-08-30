# Functions:

## create_deck() :
- This function creates deck of cards using list coprehension


## create_deck_spec(suit,num) :
- This function creates deck of cards using map , lambda , zip functions


## get_class(a) :
- This function gets the class of the cards in hand or collection

## get_winner(a,b) :
- This function given the winner  between two persons


# Rules of the game:

- The game has two main rules ,
- - The winner should have one of the following ten classes and the top in the heirarchy,
- - If both the players have the same class , then the card count will decide who is the winner . 
- - If both the players have similar class and count it is draw.

## Royal flush 
- - The combination should contain Ace , king , queen , jack and 10  of single  suit.

## Straight flush
- - The combination should contain sequence of numbers in same suit.

## Four kind  
- - The combination should contain a number in four different suits.

## Full house
- - The  combination should contain ace / queen / king / jack  and it should be a format of one pair and three of a kind .

## Flush 
- - Combination of cards in same suit.

## Straight 
- - The combination of cards in a sequence but different suits.

## Three of kind
- - The combination should contain a set oh three cards of same number but different suits.

## Two pair
- - The combination should contain two pairs of cards , in which the numbers should be same  but the suits should be different.

## One pair
- - The combination should contain only one pair of cards ,  in which the numbers should be same  but the suits should be different.

## High card 
- - In this combination the numbers are all different  and contains all four suits.

    -------------------------------------------------------------------------------------
    classes                                 |    combinations (examples)
    -----------------------------------------------------------------------------------
    * Royal flush                            | ('ace', 'hearts'),('jack', 'hearts'),('queen', 'hearts'),('king', 'hearts'),(10, 'hearts')
    * Straight flush                         | (10, 'hearts'),(9, 'hearts'),(8, 'hearts'),(7, 'hearts'),(6, 'hearts')
    * Four kind                            | ('queen','hearts'),('queen','clubs'),('queen','spades'),('queen','diamonds'),('king','hearts')
    * Full house                            | ('queen','hearts'),('queen','clubs'),('ace','spades'),('ace','diamonds'),('ace','hearts')  
    * flush                             |('king','hearts'),(1,'hearts'),(5,'hearts'),(8,'hearts'),(9,'hearts') 
    * Straight                           | (8,'hearts'),(7,'spades'),(6,'clubs'),(5,'diamonds'),(4,'hearts')
    * Three kind                        |  ('queen','hearts'),('queen','spades'),('queen','clubs'),(5,'diamonds'),(4,'hearts')
    * Two pair                           | ('queen','hearts'),('queen','spades'),('ace','clubs'),(4,'diamonds'),(4,'hearts')
    * One pair                          | ('queen','hearts'),('queen','spades'),('ace','clubs'),(3,'diamonds'),(4,'hearts')
    * High card                          | ('queen','hearts'),('jack','spades'),('ace','clubs'),(2,'diamonds'),(4,'hearts')


