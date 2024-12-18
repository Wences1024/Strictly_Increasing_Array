# Strictly Increasing List Problem

This repository contains a Python script to solve a problem where the goal is to make a given list strictly increasing by incrementing its elements. The objective is to determine the minimum number of increments needed to achieve this condition.

## Problem Description
Given a list of integers, the task is to ensure that each element is strictly greater than the one before it. If an element is not greater than the previous one, it must be incremented by the minimum amount required. The output of the program is the total number of increments performed.

### Example
#### Input
```python
[4, 2, 4, 1, 3, 5]
```
#### Output
```
2
```
#### Explanation
1. Modify `[2, 4]` to `[5, 7]` (increment = 3).
2. Modify `[1, 3, 5]` to `[8, 10, 12]` (increment = 7).

Thus, the total number of moves is `2`.

---

## How to Run the Script

### Prerequisites
- Python 3.x

### Steps to Execute
1. Clone the repository to your local machine:
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the directory:
   ```bash
   cd <repository-directory>
   ```
3. Run the script:
   ```bash
   python strictly_increasing.py
   ```

The script includes test cases that showcase various scenarios for the problem.

---

## Code Logic

### Main Steps in the Algorithm
1. **Initialization:**
   - Calculate the length of the list (`n`).
   - Initialize `moves` to track the total number of increments.
   - Use a `while` loop to traverse the list.

2. **Condition Check:**
   - If the current element is greater than or equal to the next, calculate the required increment.
   - Find the contiguous segment that needs adjustment.

3. **Increment Adjustment:**
   - Instead of modifying all elements in the segment, only modify the last element of the segment to reduce redundant operations.

4. **Update Counters:**
   - Update the total moves and continue to the next segment of the list.

5. **Result:**
   - Return the total number of moves.

This efficient approach ensures that the list is processed in \(O(n)\) time complexity with \(O(1)\) space complexity.

---

## Notes
- This script is solely for educational purposes and aims to practice Python coding skills.
- **All rights for the problem statement are reserved by Codility.**
- The script is not intended for commercial or competitive use.

---

## License
This project is open source. However, the problem statement remains the intellectual property of Codility.
