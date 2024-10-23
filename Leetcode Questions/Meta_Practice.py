from typing import List

def getHitProbability(R: int, C: int, G: List[List[int]]) -> float:
    total_cells = R * C
    is_battleship_cell = 0
    
    for row in range(R):
        for col in range(C):
            if G[row][col] == 1:
                is_battleship_cell += 1
    
    return is_battleship_cell / total_cells

def run_test_case(R, C, G, expected_output):
    result = getHitProbability(R, C, G)
    print(f"R = {R}, C = {C}")
    print(f"G = {G}")
    print(f"Expected output: {expected_output}")
    print(f"Actual output: {result}")
    print(f"Test {'passed' if abs(result - expected_output) < 1e-6 else 'failed'}")
    print()

# Test case 1: Sample test case from the problem
run_test_case(2, 3, [[0, 0, 1], [1, 0, 1]], 0.5)

# Test case 2: All cells contain battleships
run_test_case(2, 2, [[1, 1], [1, 1]], 1.0)