# Implement a simplified version of Twitter which allows users to post tweets, follow/unfollow each other, 
# and view the 10 most recent tweets within their own news feed.
# Users and tweets are uniquely identified by their IDs (integers).
# Implement the following methods:
# Twitter() Initializes the twitter object.
# void postTweet(int userId, int tweetId) Publish a new tweet with ID tweetId by the user userId. You may assume that each tweetId is unique.
# List<Integer> getNewsFeed(int userId) Fetches at most the 10 most recent tweet IDs in the user's news feed. Each item must be posted by users who the user is following or by the user themself. Tweets IDs should be ordered from most recent to least recent.
# void follow(int followerId, int followeeId) The user with ID followerId follows the user with ID followeeId.
# void unfollow(int followerId, int followeeId) The user with ID followerId unfollows the user with ID followeeId.

# Example 1:
# Input:
# ["Twitter", "postTweet", [1, 10], "postTweet", [2, 20], "getNewsFeed", [1], "getNewsFeed", [2], "follow", [1, 2], "getNewsFeed", [1], "getNewsFeed", [2], "unfollow", [1, 2], "getNewsFeed", [1]]
# Output:
# [null, null, null, [10], [20], null, [20, 10], [20], null, [10]]
# Explanation:
# Twitter twitter = new Twitter();
# twitter.postTweet(1, 10); // User 1 posts a new tweet with id = 10.
# twitter.postTweet(2, 20); // User 2 posts a new tweet with id = 20.
# twitter.getNewsFeed(1);   // User 1's news feed should only contain their own tweets -> [10].
# twitter.getNewsFeed(2);   // User 2's news feed should only contain their own tweets -> [20].
# twitter.follow(1, 2);     // User 1 follows user 2.
# twitter.getNewsFeed(1);   // User 1's news feed should contain both tweets from user 1 and user 2 -> [20, 10].
# twitter.getNewsFeed(2);   // User 2's news feed should still only contain their own tweets -> [20].
# twitter.unfollow(1, 2);   // User 1 follows user 2.
# twitter.getNewsFeed(1);   // User 1's news feed should only contain their own tweets -> [10].


#time complexity: O(nlogn) for getNewsFeed, O(1) for postTweet, follow, unfollow
#space complexity: O(n*m + N*M + n) where n is total number of followeeids associted with userid,
# m is maximum number of tweets by any user, N is total number of userIds and M is the maximum number of followees for any user


#for tweetMap, we're using a default dict containing a list, that list contains [count, tweetId]
# count we keep track of globally for the max heap, its decremented for every tweet for ordering
#followmap is a defaultdict of sets so the remove doesn't have to do expensive removals
#followmap is a hashmap of userId -> set of followeeId

#follow and unfollow are easy, just add or remove the followeeId from the followMap
# sets use .add and .remove
#make sure on unfollow to check if the followeeId is in the followMap[followerId] before removing

#postTweet is simple, just append the [count, tweetId] to the tweetMap[userId]
#and decrement the count

#getNewsFeed is a bit more complicated
#initialize a minHeap
#initialize a res list
#heapify the minHeap

#add the current user id to the followmap since everyone follows themselves in this problem and it is not called in tests
#loop through the followMap[userId] and get the followeeIds
#loop through the tweetMap[followeeId] and get the count and tweetId
#push the count and tweetId to the minHeap with the count as the priority

#loop through 10 if the minheap has greater than 10 values, otherwise loop through the minHeap
#pop the minheap and append the tweetId to the res list
#return the res list

#there is a more optimal solution that involves taking the most recent value from each tweetmap for followeeids and adding the values 1 by 1 like that
#but there is only a performance gaain if the number of tweets is 10, like this problem. For n, this solution is the same as the optimal solution
#any realistic application is going to have N and not 10, so this solution is fine hopefully if I'm asked this the interviewer will understand

class Twitter:
  
    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list) #userId -> list of [count, tweetIds]
        self.followMap = defaultdict(set) # userId -> set of followeeId

    def postTweet(self, userId: int, tweetId: int) -> None:
        #hashmap userId -> list of tweets [count, tweetid] 
        #count is how many total tweets for order
        #decrement count cuz python maxHeap 
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []
        heapq.heapify(minHeap)
        self.followMap[userId].add(userId)
        for followeeId in self.followMap[userId]:
            for count, tweetId in self.tweetMap[followeeId]:
                heapq.heappush(minHeap, (count, tweetId))
        j = 10 if len(minHeap) > 10 else len(minHeap)
        for i in range(j):
            res.append(heapq.heappop(minHeap)[1])
        return res        

    def follow(self, followerId: int, followeeId: int) -> None:
        #hashset userid -> hashset of followees
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
