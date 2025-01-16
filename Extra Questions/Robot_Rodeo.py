'''
This is how a robot works:
G instructs the robot to move forward one step.
L instructs the robot to turn left in place.
R instructs the robot to turn right in place.

Once the robot has completed the list of instructions, it will repeat them in an infinite loop.

Consider the commands R and G executed infinitely. A diagram of the robot's movement looks like:

RG --> RG
^      |
|      v
RG <-- RG
The robot will never leave the circle.

Function description
Complete the function doesCircleExist
The function must return an array of n strings either 'YES' or 'NO' based on whether the robot is bound within a circle or not, in order of test results.

doesCircleExist has the following parameter(s):

commands[commands[0], ..., commands[n-1]]: An array of n commands[i] where each represents a list of commands to test.

Constraints
1 <= | commands[i] | <= 2500
1 <= n <= 10
Each command consists of G, L, and R only.

'''

def doesCircleExist(commands):
    # Validate input array size
    if not 1 <= len(commands) <= 10:
        return []
    results = []
    for cmd_sequence in commands:
        circle_found = False
        # Validate sequence length
        if not 1 <= len(cmd_sequence) <= 2500:
            continue
            
        # Validate characters
        if not all(cmd in 'GLR' for cmd in cmd_sequence):
            results.append('NO')
            continue
            
        if len(cmd_sequence) == 1:
            results.append('NO' if cmd_sequence == 'G' else 'YES')
            continue
    # base case 1: length of commands is 1
    # sub-base case 1: that 1 command is G meaning robot will move in a straight line forerver -> return 'NO'
    # sub-base case 1: that i command is L or R meaning the robot will keep turning 90 degrees and eventually a circle will be formed -> return 'YES'

 
        else: # now considering sequence of length > 1
            # Change of robot's angle depends on L or R
            # Change of robot's position depends on G
            # North: 0, East: 1, South: 2, West: 3
            # Assume robot always starts at direction 0
            current_direction = 0
            current_x_pos, current_y_pos = 0, 0
            for command in cmd_sequence:
                if command == 'G':
                    current_x_pos, current_y_pos = updatePositionCoord(current_x_pos, current_y_pos, current_direction)
                elif command == 'L':
                    current_direction = (current_direction - 1) % 4 #updating which way the robot is facing
                    # directions are clockwise
                    # turning right goes 'up' by 1
                    # turning left goes 'down' by 1
                elif command == 'R':
                    current_direction = (current_direction + 1) % 4
                
                # if at any point robot's x_pos and y_pos are 0 that means its is back at origin and a circle exists
                if (current_x_pos == 0 and current_y_pos == 0):
                    circle_found = True
            if(circle_found) == True:
                results.append("YES")
            else:
                results.append("NO")
            # results.append('YES' if (current_x_pos == 0 and current_x_pos == 0) else 'NO') quicker way of doing the same thing above
    return results
        
 

def updatePositionCoord(current_x_pos, current_y_pos, current_direction):
    # This helper function updates the current x and y coords after robot moves one unit in a given direction
    new_pos_x, new_pos_y = current_x_pos, current_y_pos
    if current_direction == 0:
        new_pos_y += 1
    elif current_direction == 1:
        new_pos_x += 1
    elif current_direction == 2:
        new_pos_y -= 1
    elif current_direction == 3:
        new_pos_x -= 1
    return new_pos_x, new_pos_y




def run_test_cases():
    # Test Case 1: Base cases with single commands
    test1 = ["G", "L", "R"]
    expected1 = ["NO", "YES", "YES"]
    result1 = doesCircleExist(test1)
    print("Test 1 - Single commands:")
    print(f"Input: {test1}")
    print(f"Expected: {expected1}")
    print(f"Got: {result1}")
    print(f"Pass: {result1 == expected1}\n")

    # Test Case 2: Simple repeating patterns
    test2 = ["GLGLGLGL", "GLLG", "GG"]
    expected2 = ["YES", "YES", "NO"]
    result2 = doesCircleExist(test2)
    print("Test 2 - Simple repeating patterns:")
    print(f"Input: {test2}")
    print(f"Expected: {expected2}")
    print(f"Got: {result2}")
    print(f"Pass: {result2 == expected2}\n")

    # Test Case 3: Complex patterns
    test3 = ["GRGRGRGR", "GGLLGG", "GLLGGRRGGLL"]
    expected3 = ["YES", "NO", "YES"]
    result3 = doesCircleExist(test3)
    print("Test 3 - Complex patterns:")
    print(f"Input: {test3}")
    print(f"Expected: {expected3}")
    print(f"Got: {result3}")
    print(f"Pass: {result3 == expected3}\n")

    # Test Case 4: Edge case with longer sequences
    test4 = ["G" * 2500, "LR" * 1250, "GGLR" * 625]
    expected4 = ["NO", "YES", "NO"]
    result4 = doesCircleExist(test4)
    print("Test 4 - Long sequences:")
    print(f"Input: ['G'*2500, 'LR'*1250, 'GGLR'*625]")  # abbreviated for readability
    print(f"Expected: {expected4}")
    print(f"Got: {result4}")
    print(f"Pass: {result4 == expected4}\n")

    # Test Case 5: Boundary conditions
    test5 = ["GLRG" * 625]  # exactly 2500 characters
    expected5 = ["NO"]
    result5 = doesCircleExist(test5)
    print("Test 5 - Boundary condition (2500 chars):")
    print(f"Input: ['GLRG' * 625]")  # abbreviated for readability
    print(f"Expected: {expected5}")
    print(f"Got: {result5}")
    print(f"Pass: {result5 == expected5}\n")

# Run all test cases
if __name__ == "__main__":
    run_test_cases()


'''
Sample Case 0
Sample Input 0
2
G
L
Sample Output 0
NO
YES
Explanation 0
There are n=2 commands.

For commands[0] = "G", the robot will move forward forever (G --> G --> G --> ...) without ever turning or being restricted to a circle. Set index 0 of the return array to 'NO'.
For commands[1] == "L", the robot will just turn 90 degrees left forever without moving forward (because there is no 'G' instruction). The robot is effectively trapped at one spot, thus bound within a circle. Set index 1 of the return array to 'YES'.
Sample Case 1
Sample Input 1
1
GRGL
Sample Output 1
NO
Explanation 1
Consider the robot's initial orientation to be facing northward toward the positive y direction. The robot performs the following four steps in a loop:

Go forward one step. The robot moves from (0, 0) to (0, 1).
Turn right. The robot turns eastward, facing the positive x direction.
Go forward one step. The robot moves from (0, 1) to (1, 1).
Turn left. The robot turns northward, facing the positive y direction again.
                  ^
                  |
         RG  ->  LG
         ^
         |
RG  ->  LG
^
|
G
The robot then repeats these steps indefinitely, following an endless zig-zag path in the northeasterly direction. Because the robot will never turn in such a way that it would be restricted to a circle, set index 0 of the return array to NO.
'''