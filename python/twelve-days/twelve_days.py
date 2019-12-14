def recite(start_verse = 1, end_verse = 12):
    lyrics = {
        1: ["first", "a Partridge in a Pear Tree."],
        2: ["second", "two Turtle Doves"],
        3: ["third", "three French Hens"],
        4: ["fourth", "four Calling Birds"],
        5: ["fifth", "five Gold Rings"],
        6: ["sixth", "six Geese-a-Laying"],
        7: ["seventh", "seven Swans-a-Swimming"],
        8: ["eighth", "eight Maids-a-Milking"],
        9: ["ninth", "nine Ladies Dancing"],
        10: ["tenth", "ten Lords-a-Leaping"],
        11: ["eleventh", "eleven Pipers Piping"],
        12: ["twelfth", "twelve Drummers Drumming"] 
    }
    
    str = []
    
    for i in range(start_verse, (end_verse + 1)):
        line = "On the %s day of Christmas my true love gave to me: " % lyrics[i][0]
        if i == 1:
            line += "%s" % lyrics[i][1]
        if i != 1:
            for j in range(i, 0, -1):
                if j == 1:
                    line += "and %s" % lyrics[j][1]
                if j != 1:
                    line += "%s, " % lyrics[j][1]
        str.append(line)

    return str