class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        # ANALYSIS:
        # - We can parse the transactions into a structured format
        # - We can sort the transactions by time
        # - We can iterate through the transactions and check if the amount is greater than 1000
        # - We can iterate through the transactions and check if the name is the same but the city is different
        # - We can iterate through the transactions and check if the time difference is greater than 60
        # - The time complexity is O(n^2) where n is the number of transactions
        # - The space complexity is O(n) where n is the number of transactions
    
        parsed_transactions = []
        invalid_indexes = set()

        # Parse the transactions into a structured format
        for i, transaction in enumerate(transactions):
            name, time, amount, city = transaction.split(',')
            parsed_transactions.append([name, int(time), int(amount), city, i])
        
        # Sort transactions by time
        parsed_transactions.sort(key=lambda x: x[1])

        for i, t1 in enumerate(parsed_transactions):
            name1, time1, amount1, city1, index1 = t1
            if t1[2] > 1000:
                invalid_indexes.add(index1)
            
            for j in range(i+1, len(parsed_transactions)):
                name2, time2, amount2, city2, index2 = parsed_transactions[j]

                if time2 - time1 > 60:
                    break
                
                if name1 == name2 and city1 != city2:
                    invalid_indexes.add(index1)
                    invalid_indexes.add(index2)

        return [transactions[i] for i in invalid_indexes]