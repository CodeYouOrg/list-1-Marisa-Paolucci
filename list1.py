# Basic list exercises
# Fill in the code for the functions below. main() is already set up
# to call the functions with a few different inputs,
# printing 'OK' when each function is correct.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code.
# It's ok if you do not complete all the functions, and there
# are some additional functions to try in list2.py.

# A. match_ends
# Given a list of strings, return the count of the number of
# strings where the string length is 2 or more and the first
# and last chars of the string are the same.
# Note: python does not have a ++ operator, but += works.

def match_ends(words):
    counter = 0 # I originally did not have this and kept getting an error. This is necessary to start the count at zero.
    for word in words:  # this for loop will go through each word in the list.
        if len(word) >= 2 and word[0] == word[-1]:  # this if statement is checking two conditions. First, it makes sure that the word is at least 2 or more characters, and it checks if the first character (index [0]) and last character (index [-1]) are the same.
            counter += 1 # if the above conditions in the if statement are correct, then the counter goes up one increment.
    return counter 


# B. front_x
# Given a list of strings, return a list with the strings
# in sorted order, except group all the strings that begin with 'x' first.
# e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
# ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
# Hint: this can be done by making 2 lists and sorting each of them
# before combining them.

def front_x(words):
    x_word_list = []  # This list will store all the words starting with 'x'.
    other_word_list = []  # This list will store all other words.

    for word in words:  # This for loop will go through each word in the list. 
        if word.startswith('x'):  # In this if statement, the .startswith function will check for every word that starts with x. 
            x_word_list.append(word)  # If the condition is met in the if statement, then the .append function will add the word to x_word_list.
        else:
            other_word_list.append(word)  # If the condition in the if statement is not met, then the word will be added to the word to other_word_list.

    x_word_list.sort()  # The .sort function is necessary to sort the words in each list.
    other_word_list.sort() 
    new_word_list = x_word_list + other_word_list # this will merge the two lists. Putting x_word_list puts all of the x words in the list before the other words. 

    return new_word_list



# C. sort_last
# Given a list of non-empty tuples, return a list sorted in increasing
# order by the last element in each tuple.
# e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields
# [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
# Hint: use a custom key= function to extract the last element form each tuple.

def sort_last(tuples):
    new_list = sorted(tuples, key=lambda x: x[-1]) # in the new_last variable, I'm using the sorted function to sort the list of tuples. The lambda function is a small anonymous function that can have any number of arguments but can only have one expression. They are restricted to a single line of code. Here the key parameter is used to call on each list element prior to making a comparison. The lambda function takes a tuple 'x' and returns its last element x[-1].
    return new_list



# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.

def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


# Calls the above functions with interesting inputs.
def main():
    print('match_ends')
    test(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']), 3)
    test(match_ends(['', 'x', 'xy', 'xyx', 'xx']), 2)
    test(match_ends(['aaa', 'be', 'abc', 'hello']), 1)

    print()
    print('front_x')
    test(front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']),
         ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
    test(front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']),
         ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
    test(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']),
         ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])

    print()
    print('sort_last')
    test(sort_last([(1, 3), (3, 2), (2, 1)]),
         [(2, 1), (3, 2), (1, 3)])
    test(sort_last([(2, 3), (1, 2), (3, 1)]),
         [(3, 1), (1, 2), (2, 3)])
    test(sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)]),
         [(2, 2), (1, 3), (3, 4, 5), (1, 7)])


if __name__ == '__main__':
    main()
