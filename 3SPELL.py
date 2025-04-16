# Simple Edit Distance (Levenshtein Distance)
def edit_distance(s1, s2):
    # Create matrix with first row and column initialized
    m, n = len(s1), len(s2)
    dp = [[i+j if i==0 or j==0 else 0 for j in range(n+1)] for i in range(m+1)]
    
    # Fill the matrix
    for i in range(1, m+1):
        for j in range(1, n+1):
            # If characters match, no additional cost
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                # Take minimum of delete, insert, or replace operations
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
    
    return dp[m][n]

# Test examples
word1, word2 = "write", "right"
print(f"Edit distance between '{word1}' and '{word2}': {edit_distance(word1, word2)}")
