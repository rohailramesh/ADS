'''
# PermCheck
Check whether array A is a permutation.

A non-empty array A consisting of N integers is given.

A permutation is a sequence containing each element from 1 to N once, and only once.

For example, array A such that:
    A[0] = 4
    A[1] = 1
    A[2] = 3
    A[3] = 2

is a permutation, but array A such that:
    A[0] = 4
    A[1] = 1
    A[2] = 3

is not a permutation, because value 2 is missing.

The goal is to check whether array A is a permutation.

Write a function:

    def solution(A)

that, given an array A, returns 1 if array A is a permutation and 0 if it is not.

For example, given array A such that:
    A[0] = 4
    A[1] = 1
    A[2] = 3
    A[3] = 2

the function should return 1.

Given array A such that:
    A[0] = 4
    A[1] = 1
    A[2] = 3

the function should return 0.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [1..100,000];
        each element of array A is an integer within the range [1..1,000,000,000].
'''

'''
Plan:
1: Since we are working with elements that should only occur 1, we should use sets
2. Create an expected set that ranges from 1 to length of given list
3. If expected set is same as set created from original list that means no duplicates and no values from 1 to N is missing. Can return 1 else 0.
'''

def check_permutation(ls):
    if not len(ls):
        return 0
    N = len(ls)
    print(N)
    expected_set = set(range(1,N+1))
    actual_set = set(ls)
    print(expected_set)
    print(actual_set)
    if expected_set == actual_set:
        return 1
    else:
        return 0
    
test_ls_1 = [1,2,3,5]
test_ls_2 = []
result = check_permutation(test_ls_2)
print(result)    
