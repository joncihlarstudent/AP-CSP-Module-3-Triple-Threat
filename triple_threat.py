"""
Triple threat simulation game for AP Computer Science Principles.
Monarch High School - Boulder Valley School District
J. Cihlar - November 2024
"""

import random

def main() -> None:
        # set variables for the simulation
    cost_to_play: int = 5
    base_prize: int = 10
    mega_number: int = 6 # this is the special roll number
    mega_multiplier: int = 10

        # roll three dice
    roll_1: int = random.randint(1, 6)
    roll_2: int = random.randint(1, 6)
    roll_3: int = random.randint(1, 6)
    
    payout: int = 0
        # check if they are equal   
    if roll_1 == roll_2 and roll_2 == roll_3:
            # if they are, calculate the prize
        if roll_1 == mega_number:
            payout = base_prize * mega_multiplier
        else:
            payout = base_prize * roll_1

    profit: int = cost_to_play - payout
    
    # output results
    print(f"Casino collects: ${cost_to_play}")
    print(f"Player rolls: {roll_1}-{roll_2}-{roll_3}")
    print(f"Casino pays out: ${payout}")
    print(f"Profit: ${profit}")

if __name__ == "__main__":
    main()
