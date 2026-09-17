class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        answer = []
        for i in range(len(prices)):
            final_price = prices[i]

            for j in range(i+1,len(prices)):
                if prices[j] <= prices[i]:
                    final_price = prices[i]-prices[j]
                    break

            answer.append(final_price)
        return answer    

        