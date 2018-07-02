def generateParenthesis_recursive(solution, parenteses, left, right):
    if right == 0:
        solution.append(parenteses)
        return
    
    if left > 0:
        generateParenthesis_recursive(solution, parenteses+'(', left - 1, right)
    
    if left < right:
        generateParenthesis_recursive(solution, parenteses+')', left, right - 1)
        
def generateParenthesis(n):
    solution = []
    generateParenthesis_recursive(solution, '', n, n)
    return solution

print(generateParenthesis(3)) 