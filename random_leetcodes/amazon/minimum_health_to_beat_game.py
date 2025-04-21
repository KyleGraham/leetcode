#other solution
#time complexity: O(n)
#space complexity: O(1)

#bit more efficient, less readable
#sums damage, adds 1, subtracts the minimum between armor and max damage
class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        return sum(damage) + 1 - min(armor, max(damage))


#my solution
#time complexity: O(n)
#space complexity: O(1)

class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        max_damage = max(damage)
        total_damage = 0
        for dam in damage:
            if dam == max_damage:
                d = dam - armor
                if d < 0:
                    d = 0
                total_damage += d
                armor = 0
            else:
                total_damage += dam
        return total_damage + 1