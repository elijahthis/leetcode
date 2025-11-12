from typing import List
from collections import defaultdict

# class Transaction:
#     def __init__(self, name: str, time: int, amount: int, city: str):
#         self.name = name
#         self.time = time
#         self.amount = amount
#         self.city = city

#     def __repr__(self):
#         return f"{self.name},{self.time},{self.amount},{self.city}"

# ["alice,20,800,mtv", "alice,50,100,beijing"]
# [
#     Transaction("alice", 20, 800, "mtv"),
#     Transaction("alice", 50, 100, "beijing")
# ]

class Solution:
    def invalidTransactions(self, transactions: List[Transaction]) -> List[Transaction]:
        invalid = set()
        groups = defaultdict(list)

        # Group transactions by name
        for t in transactions:
            groups[t.name].append(t)

        # For each person, check their transactions
        for name, txns in groups.items():
            # Sort by time for efficient window checking
            txns.sort(key=lambda x: x.time)
            
            for i in range(len(txns)):
                t1 = txns[i]

                # Condition 1: Amount > 1000
                if t1.amount > 1000:
                    invalid.add(t1)

                # Condition 2: Same name, different cities within 60 minutes
                for j in range(i + 1, len(txns)):
                    t2 = txns[j]
                    if t2.time - t1.time > 60:
                        break
                    if t1.city != t2.city:
                        invalid.add(t1)
                        invalid.add(t2)

        return list(invalid)
