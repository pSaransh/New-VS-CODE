def countWays(steps):
    ways = [0] * (steps + 2)
    ways[0] = 1
    ways[1] = 1
    ways[2] = 2
 
    for i in range(3, steps+1):
        ways[i] = ways[i - 1] + ways[i - 2] + ways[i - 3]
 
    return ways[steps]

steps = int(input())
print(countWays(steps))