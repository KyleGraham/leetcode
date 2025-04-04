# implement a time based key value store\
# essentially it has a set that takes in a key, value, and timestamp.
# the get takes a key and timestamp and returns the value that was set at the most recent timestamp
# if there is no value set at the timestamp, it should return the most recent value set before the timestamp
# if there is no values it returns an empty string

#question text
# Implement a time-based key-value data structure that supports:
# Storing multiple values for the same key at specified time stamps
# Retrieving the key's value at a specified timestamp
# Implement the TimeMap class:
# TimeMap() Initializes the object.
# void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
# String get(String key, int timestamp) Returns the most recent value of key if set was previously called on it and the most recent timestamp 
# for that key prev_timestamp is less than or equal to the given timestamp (prev_timestamp <= timestamp). If there are no values, it returns "".
# Note: For all calls to set, the timestamps are in strictly increasing order. ------- shows you to use binary search since sorted

# Example 1:
# Input:
# ["TimeMap", "set", ["alice", "happy", 1], "get", ["alice", 1], "get", ["alice", 2], "set", ["alice", "sad", 3], "get", ["alice", 3]]
# Output:
# [null, null, "happy", "happy", null, "sad"]
# Explanation:
# TimeMap timeMap = new TimeMap();
# timeMap.set("alice", "happy", 1);  // store the key "alice" and value "happy" along with timestamp = 1.
# timeMap.get("alice", 1);           // return "happy"
# timeMap.get("alice", 2);           // return "happy", there is no value stored for timestamp 2, thus we return the value at timestamp 1.
# timeMap.set("alice", "sad", 3);    // store the key "alice" and value "sad" along with timestamp = 3.
# timeMap.get("alice", 3);           // return "sad"

# optimal solution using binary search
# time complexity O(1) for set and O(log n) for get
# space complexity O(n * m) n = number of values, m = number of keys

#solution uses a hash that stores an array of arrays
# the array has the value and the timestamp
# set function just checks if key exists and initializes an array if not, then apends an array of value and timestamp

# get function does typical binary search with r being the length of the vals at the key, defaulting to empty array
# since we return the last timestamp if it overflows:
# when the timestamp is greater or equal to, we set the return value to the value before shifting right
#else we just shift left
# return the value

class TimeMap:
  
    def __init__(self):
        self.hash = {}

        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hash:
            self.hash[key] = []
        self.hash[key].append([value, timestamp])    

    def get(self, key: str, timestamp: int) -> str:
        vals = self.hash.get(key, [])
        res = ""
        l = 0
        r = len(vals) -1
        while l <= r:
            m = (l + r) // 2
            if timestamp >= vals[m][1]:
                res = vals[m][0]
                l = m + 1
            else:
                r = m - 1
        return res
