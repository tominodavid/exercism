"""
Functions used in preparing Guido's gorgeous lasagna.
Learn about Guido, the creator of the Python language: https://en.wikipedia.org/wiki/Guido_van_Rossum
"""

EXPECTED_BAKE_TIME = 40
PREPERATION_TIME = 2


def bake_time_remaining(elapsed_bake_time):
    """
    Return calculate remaining bake time in minutes. This function takes the actual minutes the lasagna has been in the oven as an argument and returns how many minutes the lasagna still needs to bake based on the EXPECTED_BAKE_TIME
    """
    remaining = EXPECTED_BAKE_TIME - elapsed_bake_time
    return remaining


def preparation_time_in_minutes(number_of_layers):
    """
    Return preparation time in minutes. This function takes the number of layers you want to add to the lasagna as an argument and returns how many minutes you would spend making them. Assume each layer takes 2 minutes to prepare.
    """
    spend_prep_time = PREPERATION_TIME * number_of_layers
    return spend_prep_time


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """
    Return elapsed cooking time. This function takes two numbers representing the number of layers & the time already spent baking and calculates the total elapsed minutes spent cooking the lasagna.
    """
    spend_prep_time = PREPERATION_TIME * number_of_layers
    return spend_prep_time + elapsed_bake_time
