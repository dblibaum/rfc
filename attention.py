"""Defines type relations present in structure to use in computation.

   Use: Initialize with the max depth, max object, and number of types. Pass structure to filter(), which returns a
        vector containing the types observed. To update attention, pass an integer vector of size
        max_depth*max_objects*2 to set().
"""

import random


class Attention:

    def __init__(self, max_depth, max_objects, n_types):
        """
        :param max_depth: The maximum depth in the structure which to attend to.
        :param max_objects: The maximum number of type pairs to attend to in each layer of structure.
        :param n_types: The number of types in the structure.
        """
        self.attention = [[{random.randint(1, n_types), random.randint(1, n_types)} for x in range(max_objects)]
                          for x in range(max_depth)]
        self.max_objects = max_objects
        self.max_depth = max_depth

    def set(self, new_attention):
        """Sets a new attention for the attender.

        :param new_attention: :type iterable (int): An integer vector of size max_depth*max_objects*2.
        """
        for i in range(self.max_depth):
            new_layer_copy = []
            n_obj = self.max_objects*2
            new_layer = new_attention[i*n_obj:(i+1)*n_obj]
            for j in range(len(new_layer) - 1):
                pair = {new_layer[j], new_layer[j + 1]}
                new_layer_copy.append(pair)
            self.attention[i] = new_layer_copy

    def filter(self, structure):
        """Filters the structure by the current attention.

        :param structure: :type list: A list of lists generated by Structure.
        :return: :type list: A list of the type relations found in the structure.
        """
        types = []
        i = 0
        for layer in structure:
            if i < self.max_depth:
                attention_l = self.attention[i]
                for j in range(len(layer) - 1):
                    pair = {layer[j], layer[j + 1]}
                    if pair in attention_l:
                        for symbol in pair:
                            types.append(symbol)
            i += 1
        return types
