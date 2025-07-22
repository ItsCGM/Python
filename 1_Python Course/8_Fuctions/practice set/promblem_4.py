#Write a recursive function to calculalte the sum of first "n" natural numbers.

def sum_of_n(A):
    if A==1:
        return 1
    return A+sum_of_n(A-1)
print(sum_of_n(5))
    
