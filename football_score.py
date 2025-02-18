def main():
    teams = {}
    n = int(input())
    for _ in range(n):
        match = input().split(";")
        team1, goals1, team2, goals2 = [int(i) if i.isdigit() else i for i in match]
        if team1 not in teams:
            teams[team1] = {"games": 0, "wins": 0, "draws": 0, "losses": 0, "points": 0}
        if team2 not in teams:
            teams[team2] = {"games": 0, "wins": 0, "draws": 0, "losses": 0, "points": 0}
        teams[team1]["games"] += 1
        teams[team2]["games"] += 1
        if goals1 > goals2:
            teams[team1]["wins"] += 1
            teams[team1]["points"] += 3
            teams[team2]["losses"] += 1
        elif goals1 < goals2:
            teams[team2]["wins"] += 1
            teams[team2]["points"] += 3
            teams[team1]["losses"] += 1
        else:
            teams[team1]["draws"] += 1
            teams[team1]["points"] += 1
            teams[team2]["draws"] += 1
            teams[team2]["points"] += 1
    for team, stats in teams.items():
        print(
            f"{team}:{stats['games']} {stats['wins']} {stats['draws']} {stats['losses']} {stats['points']}"
        )


main()