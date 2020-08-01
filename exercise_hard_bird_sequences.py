#
# Description: Find the collisions between birds
#
# Author: Ninad Dipal Zambare
#

level_one_birds = ["A", "B", "C", "D", "E"]
level_two_birds = ["B", "A", "E", "D", "C"]
collisions = {}

i=0
for bird1 in level_one_birds:
    for bird2 in level_one_birds:
        if bird1 != bird2 and not level_one_birds.index(bird2)< level_one_birds.index(bird1):
            if level_one_birds.index(bird1) < level_one_birds.index(bird2):
                if level_two_birds.index(bird1) > level_two_birds.index(bird2):
                    collisions[i] = bird1 + " " + bird2
                    i+=1
            elif level_one_birds.index(bird1) > level_one_birds.index(bird2):
                if level_two_birds.index(bird1) < level_two_birds.index(bird2):
                    collisions[i] = bird1 + " " + bird2
                    i += 1
for i in list(collisions.keys()):
    print(collisions[i].split(" ")[0] + " collided with " + collisions[i].split(" ")[1])
print(collisions)