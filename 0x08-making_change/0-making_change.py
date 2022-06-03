#!/usr/bin/python3
"""make change"""

def makeChange(coins, total):
    """make change algorithim"""
    if total < 0:
        return -1

    dp = [total + 1] * (total +1)
    dp[0] = 0

    for a in  range(1, total + 1):
        for coin in coins:
            if a - coin >= 0:
                dp[a] = min(dp[a], 1 + dp[a - coin])
    
    return dp[total]  if dp[total] != total + 1 else -1
