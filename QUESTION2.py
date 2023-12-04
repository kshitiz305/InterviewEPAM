def solution(R, V):
    # Implement your solution here
    borrowA = 0
    borrowB = 0
    balanceA=0
    balanceB=0
    for trans,amount in zip(R,V):
        if trans == "B":
            remb = balanceA - amount
            if remb < 0:
                borrowA = borrowA + abs(remb)
                balanceB += amount
                balanceA = balanceA - amount + abs(remb)
            else:
                balanceB += amount
                balanceA -= amount
        else:
            rema = balanceB - amount
            if rema < 0:
                borrowB = borrowB + abs(rema)
                balanceA += amount
                balanceB = balanceB - amount + abs(rema)
            else:
                balanceA += amount
                balanceB -= amount
    return [borrowA,borrowB]


# Test cases
print(solution("BAABA", [2, 4, 1, 1, 2]))  # Output: [2, 4]
print(solution("ABAB", [10, 5, 10, 15]))  # Output: [0, 15]
print(solution("B", [100]))  # Output: [100, 0]
