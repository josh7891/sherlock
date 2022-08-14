"""Sherlock Randomizer Module

This module returns an array of randomized usernames built on the original 
provided. Adds random numbers and characters.
"""

class Randomizer:
    def __init__(self, username, range_lim):
        return

    def randomizer(username, range_lim):
        special_character_list = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '?', '~']
        username_list = []
        for num in range(range_lim):
            username_list.append("{0}{1}".format(username, str(num)))
            for char in special_character_list:
                username_list.append("{0}{1}{2}".format(username, str(num), char))

        return (username_list)
