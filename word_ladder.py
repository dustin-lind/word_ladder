#!/bin/python3
from collections import deque
import copy


def word_ladder(start_word, end_word, dictionary_file='words5.dict'):
    '''
    Returns a list satisfying the following properties:

    1. the first element is `start_word`
    2. the last element is `end_word`
    3. elements at index i and i+1 are `_adjacent`
    4. all elements are entries in the `dictionary_file` file

    For example, running the command
    ```
    word_ladder('stone','money')
    ```
    may give the output
    ```
    ['stone', 'shone', 'phone', 'phony', 'peony', 'penny', 'benny',
    'bonny', 'boney', 'money']
    ```
    but the possible outputs are not unique,
    so you may also get the output
    ```
    ['stone', 'shone', 'shote', 'shots', 'soots', 'hoots', 'hooty',
    'hooey', 'honey', 'money']
    ```
    (We cannot use doctests here because the outputs are not unique.)

    Whenever it is impossible to generate a word ladder between the two words,
    the function returns `None`.
    '''

    with open(dictionary_file) as f:
        newline_dictionary = f.readlines()

    stripped_dictionary = []
    for element in newline_dictionary:
        stripped_dictionary.append(element.strip())

    if start_word == end_word:
        return list([start_word])

    stack = []
    stack.append(start_word)
    queue = deque([])
    queue.append(stack)

    while queue:
        temp_stack = queue.popleft()
        for word in list(stripped_dictionary):
            if _adjacent(temp_stack[-1], word):
                if word == end_word:
                    temp_stack.append(word)
                    return temp_stack
                temp_stack_copy = copy.copy(temp_stack)
                temp_stack_copy.append(word)
                queue.append(temp_stack_copy)
                stripped_dictionary.remove(word)
    return None


def verify_word_ladder(ladder):
    '''
    Returns True if each entry of the input list is adjacent to its neighbors;
    otherwise returns False.

    >>> verify_word_ladder(['stone', 'shone', 'phone', 'phony'])
    True
    >>> verify_word_ladder(['stone', 'shone', 'phony'])
    False
    '''
    if len(ladder) == 1:
        return True
    elif len(ladder) == 0:
        return False
    else:
        for i in range(1, len(ladder)):
            if not _adjacent(ladder[i - 1], ladder[i]):
                 return False
        return True


def _adjacent(word1, word2):
    '''
    Returns True if the input words differ by only a single character;
    returns False otherwise.

    >>> _adjacent('phone','phony')
    True
    >>> _adjacent('stone','money')
    False
    '''

    if len(word1) != len(word2):
        return False
    else:
        diff = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                diff += 1
        return (diff == 1)
