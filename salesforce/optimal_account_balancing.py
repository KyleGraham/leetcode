# You are given an array of transactions transactions where transactions[i] = [fromi, toi, amounti] 
# indicates that the person with ID = fromi gave amounti $ to the person with ID = toi.

# Return the minimum number of transactions required to settle the debt.

 

# Example 1:

# Input: transactions = [[0,1,10],[2,0,5]]
# Output: 2
# Explanation:
# Person #0 gave person #1 $10.
# Person #2 gave person #0 $5.
# Two transactions are needed. One way to settle the debt is person #1 pays person #0 and #2 $5 each.
# Example 2:

# Input: transactions = [[0,1,10],[1,0,1],[1,2,5],[2,0,5]]
# Output: 1
# Explanation:
# Person #0 gave person #1 $10.
# Person #1 gave person #0 $1.
# Person #1 gave person #2 $5.
# Person #2 gave person #0 $5.
# Therefore, person #1 only need to give person #0 $4, and all debt is settled.
 

# Constraints:

# 1 <= transactions.length <= 8
# transactions[i].length == 3
# 0 <= fromi, toi < 12
# fromi != toi
# 1 <= amounti <= 100

#solution using recursion
#time complexity O((n - 1)!)
#space complexity O(n)


#instead of who owes who money, it comes down the the net balance of each person and zeroing it out
#edge cases make this way harder


# Algorithm
# Create a hash map to store the net balance of each person.

# Collect all non-zero net balance in an array balance_list.

# Define a recursive function dfs(cur) to clear all balances in the range balance_list[0 ~ cur]:

# Ignore cur if the balance is already 0. While balance_list[cur] = 0, proceed to the next person by incrementing cur by 1.

# If cur = n, return 0.
# Otherwise, set cost to a large integer like inf.
# Traverse through the index of nxt from cur + 1, if balance_list[nxt] * balance_list[cur] < 0,

# add the balance of balance_list[cur] to balance_list[nxt]: balance_list[nxt] += balance_list[cur].

# recursively call dfs(cur + 1) as dfs(cur) = 1 + dfs(cur + 1).

# remove the previous transferred balance from cur: balance_list[nxt] -= balance_list[cur] (backtrack).

# Repeat from step 5 and keep tracking of the minimum number of operations of cost = min(cost, 1 + dfs(cur + 1)) 
# encountered in the iteration. Return cost when the iteration is complete.

# Return dfs(0).


class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        balance_map = defaultdict(int)
        for f, t, a in transactions:
            balance_map[f] += a
            balance_map[t] -= a
        
        balance = [amount for amount in balance_map.values() if amount]
        n = len(balance)
        
        def dfs(cur):
            while cur < n and not balance[cur]:
                cur += 1
            if cur == n:
                return 0
            cost = float('inf')
            for nxt in range(cur + 1, n):
                if balance[nxt] * balance[cur] < 0:
                    balance[nxt] += balance[cur]
                    cost = min(cost, 1 + dfs(cur + 1))
                    balance[nxt] -= balance[cur]
            return cost
        return dfs(0)


