# Convert a non-negative integer num to its English words representation.

# Example 1:

# Input: num = 123
# Output: "One Hundred Twenty Three"
# Example 2:

# Input: num = 12345
# Output: "Twelve Thousand Three Hundred Forty Five"
# Example 3:

# Input: num = 1234567
# Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"


#basis is to split the number into groups of 3 digits, then from those 3 digits
#split into tens and ones

#solution using iteration
#time complexity: O(log10(n)) because the number is divided by 1000 in each iteration
#space complexity: O(1)

# Given an integer num, convert it to a human-readable string representation in English.
#check if number is 0, if so return "Zero"
#initialize the ones, tens and thousands arrays
#in the ones, keep 0 as ""
#in the tens, keep 0 as "", and go to nineteen
#in the tens, keep 0 as "", and go to ninety
#in the thousands, keep 0 as "" and go "Thousand", "Million", "Billion"
#max number is 2^31 - 1, so we can go up to 3 billion

#initialize result as an empty string
#initialize group index as 0, this is the thousands index
#while num is greater than 0
#mod num by 1000 and check that the result is not 0
#initialize group result as an empty string
#initialize part as num mod 1000
#check if part is greater than or equal to 100
# if so, add the ones at part // 100 to group result and add "Hundred" to group result
#mod part by 100
#check if part is greater than or equal to 20
# if so, add the tens at part // 10 to group result and add " " to group result
#mod part by 10
#check if part is greater than 0
# if so, add the ones at part to group result and add " " to group result
#append the thousands at group index to group result and add " " to group result
#insert the group result at the beginning of the final result
#move to the next chunk of 1000 by dividing num by 1000
#increment the group index by 1

#finally return the result stripped of leading and trailing spaces


class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        
        ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen",        "Seventeen", "Eighteen", "Nineteen"]
        tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        thousands = ["", "Thousand", "Million", "Billion"]

        #StringBuilder to accumulate the result
        result = ""
        group_index = 0

        #process the number in chunks of 1000
        while num > 0:
            #process the last three digits
            if num % 1000 != 0:
                group_result = ""
                part = num % 1000

                #handle hundreds
                if part >= 100:
                    group_result += ones[part // 100] + " Hundred "
                    part %= 100
                
                #handles tens and units
                if part >= 20:
                    group_result += tens[part // 10] + " "
                    part %= 10
                #handle units
                if part > 0:
                    group_result += ones[part] + " "
                
                #append the scale (thousand, million, billion) for the current group
                group_result += thousands[group_index] + " "
                #insert the group result at the beginning of the final result
                result = group_result + result
            #move to the next chunk of 1000
            num //= 1000
            group_index += 1

        return result.strip()