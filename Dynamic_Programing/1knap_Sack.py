class KnapSack_0_1:
    def knapSack(self, W, wt, val, n):
        dp = [[0 for i in range(W + 1)] for j in range(n + 1)]

        for i in range(n + 1):
            for w in range(W + 1):
                if i == 0 or w == 0:
                    dp[i][w] = 0
                elif wt[i - 1] <= w:
                    dp[i][w] = max(val[i - 1] + dp[i - 1][w - wt[i - 1]], dp[i - 1][w])
                else:
                    dp[i][w] = dp[i - 1][w]

        return dp[n][W]
    
# Example usage
if __name__ == "__main__": 
    W = 50
    wt = [10, 20, 30]
    val = [60, 100, 120]
    n = len(val)
    
    knapsack = KnapSack_0_1()
    result = knapsack.knapSack(W, wt, val, n)
    print("Maximum value in Knapsack =", result)