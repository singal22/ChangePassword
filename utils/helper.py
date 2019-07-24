import collections


# match percentage between two strings
def match_percentage(a, b):
    """
    It return match percentage between two strings
    :param a: string
    :param b: string
    :return: match percentage
    """
    count = 0
    if len(a) > len(b):
        for i in range(0, len(b)):
            if a[i] == b[i]:
                count += 1
        match = (count*100)/len(a)
    else:
        for i in range(0, len(a)):
            if a[i] == b[i]:
                count += 1
        match = (count*100)/len(b)

    return match


# count number of special characters
def count_special_characters(password, special_chars):

    """
    This function return the count of allowed special chharacter
    :param password: Password
    :param special_chars: Allowed Special Characters
    :return: count of total special characters
    """

    count = 0
    for i in range(0, len(password)):
        ch = password[i]
        if ch in special_chars:
            count = count + 1

    return count


# count digits
def count_digits(password):
    """
    This function return the count of digits in string
    :param password: pwdrequirements
    :return: count of digits
    """

    count = 0
    for i in range(0, len(password)):
        ch = password[i]
        if ch.isdigit():
            count = count + 1

    return count


# count number of repeating characters
def count_duplicate(password, num):
    """
    This function return true if exceeds allowed duplicate count
    :param password: pwdrequirements
    :param num: Number of duplicate repeating characters allowed
    :return: True if more than allowed number
    """

    dic = collections.defaultdict(int)
    duplicate = False
    for c in password:
        dic[c] += 1

    for c in dic:
        if dic[c] > num:
            duplicate = True
    return duplicate
