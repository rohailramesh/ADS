'''
A gym membership card allows entry for a one-week period that always begins on a Monday and ends on the following Sunday. Ellis attends the gym once a day at most. 

You are given a list visits of length N, which represents the days Ellis visits the gym, in chronological order. 

What is the minimum number of gym membership cards that Ellis has to purchase?

TASK -- Write a function:
def solution(visits)
that, given a list visits of length N, returns the minimum number of gym membership cards that Ellis must purchase based on the order of visits specified.

Days of the week in visits are represented as three-letter strings (Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun").
Examples:
1. For visits = ["Tue", "Sat", "Mon", "Fri"], the function should return 2. In the first week, Ellis visits
the gym on Tuesday and Saturday. In the second week, Ellis visits the gym on Monday and Friday.
2. For visits = ["Mon", "Mon", "Mon"], the function should return 3. Ellis visits the gym only on Monday
each week.
3. For visits = ["Sun", "Sat", "Fri", "Thu", "Wed", "Tue", "Mon"], the function should return 7.
Assume that:
* N is an integer within the range [1..100];
* The only strings in visits are: "Mon", "Tue", "Wed", 'Thu", "Fri", "Sat" and/or "Sun".
'''
def solution(visits):
    # Convert days to numbers for easier calculation
    day_to_num = {"Mon": 0, "Tue": 1, "Wed": 2, "Thu": 3, "Fri": 4, "Sat": 5, "Sun": 6}
    
    if not visits:
        return 0
    
    # Initialize the number of memberships
    memberships = 1
    # Get the first visit's day number
    current_week_start = day_to_num[visits[0]]  # Start of the week is the first visit's day
    
    for visit in visits[1:]:
        day_num = day_to_num[visit]
        
        # If the visit is on or after the current week's start but within the same week, continue
        if day_num >= current_week_start and day_num < current_week_start + 7:
            # If the visit is on the same day as the current week's start, it's a new week
            if day_num == current_week_start:
                memberships += 1
                current_week_start = day_num  # Start a new week
        else:
            # Otherwise, start a new membership and update the current week's start
            memberships += 1
            current_week_start = day_num  # New week starts on the current visit's day
    
    return memberships

# Test cases
print(solution(["Tue", "Sat", "Mon", "Fri"]))  # Output: 2
print(solution(["Mon", "Mon", "Mon"]))         # Output: 3
print(solution(["Tue", "Tue", "Tue"]))         # Output: 3
print(solution(["Sun", "Sat", "Fri", "Thu", "Wed", "Tue", "Mon"]))  # Output: 7
print(solution([]))  # Output: 0
print(solution(["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun", "Mon"]))  # Output: 2
print(solution(["Mon", "Wed", "Fri", "Sun", "Tue", "Thu", "Sat", "Mon"]))  # Output: 2
print(solution(["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun", "Mon", "Tue", "Wed", "Thu"]))  # Output: 3


'''
Pseudocode:
- Assign each day of the week a num from 0 to 6 using a dict
- base case -> if visits is empty then return 0 (that is num of cards needed)
- assign valye 1 to total_cards assuming atleast 1 card will be needed if not the base case
- find the current_start_week_num of Ellis which will be the value at index 0 in visits
- run a for loop now from index 1 and not 0 since that is already handled above
- for curent value in that loop, get the corresponding number for that day from dict and that will be current_day_num
- if the current_day_num is >= current_start_week_num and current_day_num is < current_start_week_num + 7 (meaning that current_day is within same week) then continue
    within that for loop also check if current_day_num is same as current_week_num then that means its a new week so increase the card count by 1 and also now current_start_week starts on the current_day_num
- else we are in a new week anyways now so increase the card count by 1 and set current_start_week to current_day
- finally return the total number of cards
'''