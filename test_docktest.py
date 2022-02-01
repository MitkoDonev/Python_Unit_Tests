import doctest


def factorial_success(number):
    """
    This function calculates recursively and
    returns the factorial of a positive number.
    Define input and expected output:

    :param number: int

    >>> factorial_success(3)
    6
    >>> factorial_success(5)
    120
    """

    if number <= 1:
        return 1
    return number * factorial_success(number - 1)


def factorial_fail(number):
    """
    This function calculates recursively and
    returns the factorial of a positive number.
    Define input and expected output:

    :param number: int

    >>> factorial_fail(3)
    6
    >>> factorial_fail(5)
    120
    """

    if number <= 1:
        return 1
    return factorial_fail(number - 1)


def count_vowels(word):
    """
    Given a single word, return the total number of vowels in that single word.

    :param word: str
    :return: int

    >>> count_vowels('Cusco')
    2
    >>> count_vowels('Manila')
    3
    >>> count_vowels('Istanbul')
    3
    """

    total_vowels = 0
    for letter in word.lower():
        if letter in "aeiou":
            total_vowels += 1

    return total_vowels


if __name__ == "__main__":
    doctest.testmod(verbose=True)
