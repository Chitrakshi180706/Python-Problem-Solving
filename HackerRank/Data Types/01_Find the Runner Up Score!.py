Task
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given n scores. 
Store them in a list and find the score of the runner-up.

Input Format

The first line contains n. The second line contains an array A[] of n integers each separated by a space.

Solution

  if __name__ == '__main__':
    n = int(input())
    numbers = list(map(int, input().split()))
    numbers = list(set(numbers))
    numbers.sort()
    print(numbers[-2])
    
