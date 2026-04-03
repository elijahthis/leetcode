from collections import defaultdict

class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        parsed = []
        invalid = set()
        
        for i, t in enumerate(transactions):
            name, time, amount, city = t.split(',')
            parsed.append((name, int(time), int(amount), city, i))
        
        # Group by name
        groups = defaultdict(list)
        for p in parsed:
            groups[p[0]].append(p)
        
        for name, txns in groups.items():
            txns.sort(key=lambda x: x[1])
            for i in range(len(txns)):
                n1, t1, a1, c1, idx1 = txns[i]
                if a1 > 1000:
                    invalid.add(idx1)
                for j in range(i+1, len(txns)):
                    n2, t2, a2, c2, idx2 = txns[j]
                    if t2 - t1 > 60:
                        break
                    if c1 != c2:
                        invalid.add(idx1)
                        invalid.add(idx2)
        
        return [transactions[i] for i in invalid]
