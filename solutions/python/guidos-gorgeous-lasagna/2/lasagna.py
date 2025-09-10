"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language: https://en.wikipedia.org/wiki/Guido_van_Rossum
"""

EXPECTED_BAKE_TIME = 40
PREPERATION_TIME = 2

"""
Calculate the bake time remaining.

:param elapsed_bake_time: int - baking time already elapsed.
:return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

Function that takes the actual minutes the lasagna has been in the oven as
an argument and returns how many minutes the lasagna still needs to bake
based on the `EXPECTED_BAKE_TIME`.
"""

def bake_time_remaining(elapsed_bake_time):

    """
    Return calculate remaining bake time in minutes

    This function takes the actual minutes the lasagna has been in the oven as an argument and returns how many 
    minutes the lasagna still needs to bake based on the EXPECTED_BAKE_TIME
    """

    elapsed_bake_time = EXPECTED_BAKE_TIME - elapsed_bake_time

    return elapsed_bake_time
    pass

def preparation_time_in_minutes(spend_prep_time):

    """
    Return preparation time in minutes.

    This function takes the number of layers you want to add to the lasagna as an argument and returns how 
    many minutes you would spend making them. Assume each layer takes 2 minutes to prepare.  
    """

    spend_prep_time =  PREPERATION_TIME * spend_prep_time

    return spend_prep_time
    pass

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):

    """
    Return elapsed cooking time.

    This function takes two numbers representing the number of layers & the time already spent 
    baking and calculates the total elapsed minutes spent cooking the lasagna.
    """
    
    number_of_layers = PREPERATION_TIME * number_of_layers

    return number_of_layers + elapsed_bake_time
    pass
