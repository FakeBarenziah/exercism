
def latest(scores):
    return scores[-1]


def personal_best(scores):
    greatest = 0
    for each in scores:
        if each > greatest:
            greatest = each
    return greatest

def personal_top_three(scores):
    newList = []
    newList.extend(scores)
    newList.sort()

    returnList = []
    i = 1
    while len(returnList) < 3 & i <= len(newList):
        returnList.append(newList[-i])
        i = i + 1
    print(returnList)
    return returnList
