f = open("./files/AoC/2022_3.txt", "r")

prioritySum = 0
groupCounter = 0
group = []
for line in f:
    group.append(line.strip())
    groupCounter += 1

    if groupCounter == 3:
        prioritySet = set(group[0])

        for team in group:
            prioritySet = prioritySet.intersection(team)

        badge = list(prioritySet)[0]
        prioritySum += (
            ord(badge) - ord("a") + 1 if badge.islower() else ord(badge) - ord("A") + 27
        )
        groupCounter = 0
        group = []


f.close()

print(prioritySum)

