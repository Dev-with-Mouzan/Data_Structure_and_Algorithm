class Fractional_Knapsack:
    def __init__(self,profit,weight):
        self.profit=profit
        self.weight=weight
    def knapsack(self,capacity):
        ratio=[0]*len(self.profit)
        for i in range(len(self.profit)):
            ratio[i]=self.profit[i]/self.weight[i]
        for i in range(len(self.profit)):
            for j in range(i+1,len(self.profit)):
                if ratio[i]<ratio[j]:
                    ratio[i],ratio[j]=ratio[j],ratio[i]
                    self.profit[i],self.profit[j]=self.profit[j],self.profit[i]
                    self.weight[i],self.weight[j]=self.weight[j],self.weight[i]
        total_profit=0
        for i in range(len(self.profit)):
            if self.weight[i]<=capacity:
                total_profit+=self.profit[i]
                capacity-=self.weight[i]
            else:
                total_profit+=capacity*ratio[i]
                break
        return total_profit
    
profit=[60,100,120]
weight=[10,20,30]
capacity=50
knapsack=Fractional_Knapsack(profit,weight)
print(knapsack.knapsack(capacity))
