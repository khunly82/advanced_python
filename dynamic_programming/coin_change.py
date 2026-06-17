# def make_change(coins, total):
#     dp = [0] + [float('inf')] * total
#     for n in range(1, total + 1):
#         available_coins = [c for c in coins if c <= n]
#         for c in available_coins:
#             dp[n] = min(dp[n], 1 + dp[n - c])

#     return dp[total] if dp[total] != float('inf') else -1

from functools import cache

def make_change(coins, total):
    @cache
    def recurse(remaining):
        if remaining == 0:
            return 0
        if remaining in coins:
            return 1
        p = []
        available_coins = [c for c in coins if c <= remaining]
        for c in available_coins:
            prev = recurse(remaining - c)
            if(prev != -1):
                p.append(1 + prev)
        return min(p) if p else -1

    for v in range(total + 1):
        recurse(v)
    return recurse(total)



assert make_change([1,3,4], 6) == 2
assert make_change([3,4], 5) == -1
assert make_change([1,4,6,9], 42) == 5

assert make_change([1,2,3], 1000000) == 333334

print('all tests have passed')