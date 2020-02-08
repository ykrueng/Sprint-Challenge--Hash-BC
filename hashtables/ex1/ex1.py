#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)

def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    for index in range(length):
        key = limit - weights[index]
        pair_index = hash_table_retrieve(ht, key)

        if pair_index is None:
            hash_table_insert(ht, weights[index], index)
        else:
            return(index, pair_index)
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
