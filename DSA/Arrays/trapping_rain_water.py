# Find the maximum amount of water that can be trapped within a given set of blocks
# where each blocks's width and height is 1 unit. 

# Imagine a 2D field where the blocks are constructed in container like shapes to 
# trap water. 
# Height of blocks: [2, 1, 3, 1, 4]. Constructed as so, the max amount
# of water trapped is 3 blocks worth.

# Base cases: if len of array < 3, no water trapped. First and last bars 
# cannot trap water
# Solution: Track the max height on the left and right of the targeSt block. Then find
# the min between those 2. The number of blocks of water trapped is 
# min(max_left, max_right) - height_of_target_block
# max left/right value: Iterate through the array and record the max left/right values

# height_of_target = [1, 0, 2, 1, 3, 1, 2, 0, 3]
# max_left = [0, 1, 1, 2, 2, 3, 3, 3, 3]
# max_right = [3, 3, 3, 3, 3, 3, 3, 3, 0]
# trapped water = min(max_left, max_right) - height_of_target_block
# = [0, 1, 0, 1, 0, 2, 1, 3]

# O(n) as there are no nested forloops
def trapping_water_problem(heights): 
    # Base case
    if len(heights) < 3:
        return 0

    # Initialising lists
    left_max = [0 for _ in range(len(heights))]
    right_max = [0 for _ in range(len(heights))]

    # Starting from 0 as the first index of left_max is always 0
    for i in range(1, len(heights)):
        # Take the max of previous left_max and previous height
        left_max[i] = max(left_max[i-1], heights[i-1])
    
    # Starting from the 2nd last index as the last index for right_max is always 0
    # From len(heights)-2 to -1 as the index is exclusive of the end value.
    for i in range(len(heights)-2, -1, -1):
        right_max[i] = max(right_max[i+1], heights[i+1])

    trapped_water = 0

    # Iterating through the array of heights adding the water trapped if the min of
    # left_max and right_max is more than the height of the target block
    for i in range(1, len(heights)-1):
        if min(left_max[i], right_max[i]) > heights[i]:
            trapped_water += min(left_max[i], right_max[i]) - heights[i]

    return trapped_water

if __name__=="__main__":
    heights = [3, 2, 3]
    print(trapping_water_problem(heights))
