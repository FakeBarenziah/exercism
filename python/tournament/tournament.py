def tally(rows):
    teams = {}

    for outcome in rows:
        outcome = outcome.split(";")

        if not outcome[0] in teams:
            teams[outcome[0]] = {"mp":0, "w":0, "d":0, "l":0, "p":0}

        if not outcome[1] in teams:
            teams[outcome[1]] = {"mp":0, "w":0, "d":0, "l":0, "p":0}

        teams[outcome[0]]["mp"]+=1
        teams[outcome[1]]["mp"]+=1

        if outcome[2] == "win":
            teams[outcome[0]]["w"]+=1
            teams[outcome[0]]["p"]+=3

            teams[outcome[1]]["l"]+=1

        if outcome[2] == "loss":
            teams[outcome[1]]["w"]+=1
            teams[outcome[1]]["p"]+=3

            teams[outcome[0]]["l"]+=1

        if outcome[2] == "draw":
            teams[outcome[0]]["d"]+=1
            teams[outcome[0]]["p"]+=1

            teams[outcome[1]]["d"]+=1
            teams[outcome[1]]["p"]+=1

    table = ["Team                           | MP |  W |  D |  L |  P"]

    team_list = []
    
    for team in teams.keys():
        team_list.append(team)

    team_list = sorted(team_list)
    team_list = sorted(team_list, key=lambda team : teams[team]["p"], reverse=True)

    for team in team_list:
        delimiter = " | "
        line = ""
        line += team.ljust(30) + delimiter
        line += str(teams[team]["mp"]).rjust(2) + delimiter
        line += str(teams[team]["w"]).rjust(2) + delimiter
        line += str(teams[team]["d"]).rjust(2) + delimiter
        line += str(teams[team]["l"]).rjust(2) + delimiter
        line += str(teams[team]["p"]).rjust(2)

        table.append(line)

    return table
