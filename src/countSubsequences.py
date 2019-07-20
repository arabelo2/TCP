# Python 3 program to count subsequences of the form a^i b^j c^k

# Returns count of subsequences of the form a^i b^j c^k
def countSubsequences(s):
    aCount = 0
    bCount = 0
    cCount = 0
    for i in range(len(s)):
        if (s[i] == 'a'):
            aCount = (1 + 2 * aCount)
        elif (s[i] == 'b'):
            bCount = (aCount + 2 * bCount)
        elif (s[i] == 'c'):
            cCount = (bCount + 2 * cCount)
    return cCount

# Driver code
if __name__ == "__main__":
    s = "aaaaabc"
    print(countSubsequences(s))
 
# This code is contributed by ChitraNayal