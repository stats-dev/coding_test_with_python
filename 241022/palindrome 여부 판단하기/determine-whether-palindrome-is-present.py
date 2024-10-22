def is_palindrome(A):
    if A[::-1] == A:
        return True
    return False


A = input()

if is_palindrome(A):
    print("Yes")
else:
    print("No")