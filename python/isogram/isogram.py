def is_isogram(string):
    dict = {}
    for char in string:
        if char.lower() in dict:
            return False
        if char != " " and char != "-":
            dict[char.lower()] = True

    return True
