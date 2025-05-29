# In the world of Dota2, there are two parties: the Radiant and the Dire.

# The Dota2 senate consists of senators coming from two parties. Now the Senate wants to decide on a change in the Dota2 game. 
# The voting for this change is a round-based procedure. In each round, each senator can exercise one of the two rights:

# Ban one senator's right: A senator can make another senator lose all his rights in this and all the following rounds.
# Announce the victory: If this senator found the senators who still have rights to vote are all from the same party, 
# he can announce the victory and decide on the change in the game.
# Given a string senate representing each senator's party belonging. The character 'R' and 
# 'D' represent the Radiant party and the Dire party. Then if there are n senators, the size of the given string will be n.

# The round-based procedure starts from the first senator to the last senator in the given order. 
# This procedure will last until the end of voting. All the senators who have lost their rights will be skipped during the procedure.

# Suppose every senator is smart enough and will play the best strategy for his own party. 
# Predict which party will finally announce the victory and change the Dota2 game. The output should be "Radiant" or "Dire".

 

# Example 1:

# Input: senate = "RD"
# Output: "Radiant"
# Explanation: 
# The first senator comes from Radiant and he can just ban the next senator's right in round 1. 
# And the second senator can't exercise any rights anymore since his right has been banned. 
# And in round 2, the first senator can just announce the victory since he is the only guy in the senate who can vote.
# Example 2:

# Input: senate = "RDD"
# Output: "Dire"
# Explanation: 
# The first senator comes from Radiant and he can just ban the next senator's right in round 1. 
# And the second senator can't exercise any rights anymore since his right has been banned. 
# And the third senator comes from Dire and he can ban the first senator's right in round 1. 
# And in round 2, the third senator can just announce the victory since he is the only guy in the senate who can vote.

#solution using queue
#time complexity O(n)
#space complexity O(n)

#essentially, the senators will do their ban and move to the end of the queue after, which isnt really explained
# DDRRR - the first D moves to the back and takes out the first R
# DRRD - the first D moves to the back and takes out the first R
# RDD - the first R moves to the back and takes out the first D
# DR - the first (and only) D moves to the back and takes out the first (and only) R
# D - D wins the vote.

#so we count the Rs and Ds in the string
#keep track of bans with ints
#create a deque from the string

#do a while loop on the rcount and dcount
#pop the left item
#if its a D:
#if theres a ban, reduce dcount and dban
#else add an r ban and append the d to the queue
#reverse for R
#return radiant if rcount else dire


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
         # Eligible Senators of each party
        r_count = senate.count('R')
        d_count = len(senate) - r_count

        # Floating Ban Count
        d_floating_ban = 0
        r_floating_ban = 0

        # Queue of Senators
        q = deque(senate)

        # While any party has eligible Senators
        while r_count and d_count:

            # Pop the senator with turn
            curr = q.popleft()

            # If eligible, float the ban on the other party, enqueue again.
            # If not, decrement the floating ban and count of the party.
            if curr == 'D':
                if d_floating_ban:
                    d_floating_ban -= 1
                    d_count -= 1
                else:
                    r_floating_ban += 1
                    q.append('D')
            else:
                if r_floating_ban:
                    r_floating_ban -= 1
                    r_count -= 1
                else:
                    d_floating_ban += 1
                    q.append('R')

        # Return the party with eligible Senators
        return 'Radiant' if r_count else 'Dire'