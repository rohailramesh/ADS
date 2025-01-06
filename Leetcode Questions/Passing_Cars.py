'''
"""
# Passing Cars

Count the number of passing cars on the road.

A non-empty array A consisting of N integers is given.
The consecutive elements of array A represent consecutive cars on a road.

Array A contains only 0s and/or 1s:

        0 represents a car traveling east,
        1 represents a car traveling west.

The goal is to count passing cars. We say that a pair of cars (P, Q),
where 0 ≤ P < Q < N, is passing when P is traveling to the east
and Q is traveling to the west.

For example, consider array A such that:
  A[0] = 0
  A[1] = 1
  A[2] = 0
  A[3] = 1
  A[4] = 1

We have five pairs of passing cars: (0, 1), (0, 3), (0, 4), (2, 3), (2, 4).

Write a function:

    def passing_cars(A)

that, given a non-empty array A of N integers, returns the number of pairs of passing cars.

The function should return -1 if the number of pairs of passing cars exceeds 1,000,000,000.

For example, given:
  A[0] = 0
  A[1] = 1
  A[2] = 0
  A[3] = 1
  A[4] = 1

the function should return 5, as explained above.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [1..100,000];
        each element of array A is an integer that can have one of the following values: 0, 1.
'''

'''
Plan:
Car going towards east is P (0)
Car going towards west is Q (1)
P < Q means car travelling from west will cross car travelling to east
A[0] = 0
A[1] = 1
A[2] = 0
A[3] = 1
A[4] = 1

A[0] will cross A[1], A[3], A[4] and A[2] will cross A[3] and A[4] but not A[1] since that has already passed as it is before A[2]

If a car is going in east, just increment the counter of east
If a car is going in west, increment the pass counter with value of east counter as that is the number of cars that have crossed each other
If pass counter exceed 1E6, return -1
'''
# import unittest
def passing_cars(car_direction_ls):
    east_bound_counter = 0
    total_passes_counter = 0
    MAX_PASS_LIMIT = int(1e9)
    for direction in car_direction_ls:
        if direction == 0:
            east_bound_counter += 1
        else:
            total_passes_counter += east_bound_counter
        if total_passes_counter > MAX_PASS_LIMIT:
            return -1
    return total_passes_counter

car_direction_ls1 = [0,1,0,1,1]
result = passing_cars(car_direction_ls1)
print(result)

# making use of unit testing in python
# class Test_Passing_Cars(unittest.TestCase):
    
#     def test_example_1(self):
#         self.assertEqual(passing_cars([0,1,0,1,1]),5)
        
#     def test_minimal(self):
#         self.assertEqual(passing_cars([0]), 0)
#         self.assertEqual(passing_cars([1]), 0)
#         self.assertEqual(passing_cars([0, 0]), 0)
#         self.assertEqual(passing_cars([1, 1]), 0)
#         self.assertEqual(passing_cars([0, 1]), 1)
#         self.assertEqual(passing_cars([1, 0]), 0)


# if __name__ == "__name__":
#     unittest.main()