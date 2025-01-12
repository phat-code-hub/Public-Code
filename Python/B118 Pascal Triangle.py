"""_summary_
    Given an integer numRows, return the first numRows of Pascal's triangle.

    In Pascal's triangle, each number is the sum of the two numbers directly above it :
    Example 1:

        Input: numRows = 5
        Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
    Example 2:
        Input: numRows = 1
        Output: [[1]]
        
    Created by Ueda
"""
numRows =5
triangle = [[1]]
for i in range(1,numRows):
    currRow = [1]
    preRow = triangle[i-1]
    for j in range(1,len(preRow)):
        currRow.append(preRow[j-1]+preRow[j])
    currRow.append(1)    
    triangle.append(currRow)
print(triangle)