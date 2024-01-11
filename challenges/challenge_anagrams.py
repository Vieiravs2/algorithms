def is_anagram(first_string, second_string):
    first_string = first_string.lower()
    second_string = second_string.lower()

    if not first_string and not second_string:
        return first_string, second_string, False

    return (
        order_string(first_string),
        order_string(second_string),
        order_string(first_string) == order_string(second_string)
    )


def order_string(string):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    return (
        ''.join(letter * string.count(letter)
                for letter in alphabet if letter in string)
    )