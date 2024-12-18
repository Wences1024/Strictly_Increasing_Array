class Strictly_Increasing:
    def Solution(self, A : list) -> int:
        #First we get the length of the list
        n = len(A)
        #We initialize the total amount of movement to perform
        moves = 0
        #We initialize the index
        i = 0
        #While Loop to iterate over the whole list
        while i < n - 1:
            #If the current element in the list is equal or greater than the next one, the list is not trictly increasing, and therefore we need to adjust this
            if A[i] >= A[i + 1]:
                #We stablish the necessary incremenet the segment will eed
                increment = A[i] - A[i + 1] + 1
                #We sstablish a pointer variables.
                start = i + 1
                point_A = start
                end = start + 1
                #We advance in the list while the next value is is greater than the current or we reach the end of the list
                while end < n and A[end] > A[point_A]:
                    point_A += 1
                    end += 1
                    
                #Uncomment if you want to modify the values of the list to making it increasing order
                # for modification in range(start,end):
                #     A[modification] = A[modification] + increment
                
                #Comment if you are modifying the values of the list to making it increasing order
                #We just need to modify the las value to keep searching in the next iteration!
                A[end-1] = A[end-1] + increment
                #We increment the total amount of moves needed
                moves += 1
                #We increment the index of the list
                i = end - 1
            #If the current value is not greater or equal than the next one, we increase the index and keep analizing
            else:
                i += 1
        #We return the total amount of moves 
        return moves


if __name__ == "__main__":
    Test = Strictly_Increasing()
    test_cases = [
        [4, 2, 4, 1, 3, 5], #Expected 2
        [3, 5, 7, 7], #Expected 1
        [1, 5, 6, 10], #Expected 0
        [1,2,3,1,2,3,4,20], #Expected 1
        [10,9,8,7,1,2,3,4,5,6], #Expected 4
        [5], #Expected 0
        [7,7,7,7,7,7,7,7,7,7,7], #Expected 10
    ]
    
    for case in test_cases:
        print(f"The minimum moves to make the list {case} strickly increasing would be: {Test.Solution(case)}")
        