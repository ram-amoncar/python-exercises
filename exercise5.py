# Snake, Water, & Gun

from enum import IntEnum
from random import choice

class RESULTS(IntEnum):
    WIN = 1
    DRAW = 0
    LOSE = -1


class OPTIONS(IntEnum):
    SNAKE = 0
    WATER = 1
    GUN = 2


"""
              CPU
            S   W   G
        S   0   1  -1
Player  W  -1   0   1
        G   1  -1   0
"""
condition_matrix = [[0, 1, -1], [-1, 0, 1], [1, -1, 0]]
wins = losses = draws = 0

print("Snake, Water, & Gun")

while True:
    for i, opt in enumerate(OPTIONS):
        print(f"{i+1}.", opt.name.title())

    player = int(input("Pick your move: ")) - 1
    cpu = choice(list(OPTIONS))

    match (condition_matrix[player][cpu]):
        case RESULTS.WIN:
            wins += 1
        case RESULTS.LOSE:
            losses += 1
        case RESULTS.DRAW:
            draws += 1

    print("You chose:", OPTIONS(player).name.title())
    print("CPU chose:", OPTIONS(cpu).name.title())
    print(f"Results: {RESULTS(condition_matrix[player][cpu]).name.title()}")

    if input("Do you want to play one more round? (y/n)\n").lower() != "y":
        break

print("\nFINAL RESULTS")
print(
    f"""Wins: {wins}
Draws: {draws} 
Losses: {losses}"""
)
