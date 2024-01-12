"""
    DS 2001 Weekly Exercise 11
    Sean Ayoub
"""

class Customer:
    def __init__(self, name):
        self.name = name
        self.orders_total = 0
        self.orders_quarter = 0
        self.recency = 100
        self.frequency = 0
        self.monvalue = 0

    def new_month(self):
        self.recency += 1
        
    def new_quarter(self):
        self.frequency = self.orders_quarter
        self.orders_quarter = 0
        
    def new_order(self, spend):
        total = self.monvalue * self.orders_total + spend
        self.orders_total += 1
        self.orders_quarter += 1
        self.monvalue = total / self.orders_total
        self.recency = 0
    
def main():
    sean = Customer("Sean")
    sean.new_order(32)
    
    sean.new_month()
    sean.new_order(56)
    
    sean.new_month()
    sean.new_order(45)
    sean.new_order(28)
    
    sean.new_month()
    sean.new_quarter()
    
    print("Name:", sean.name)
    print("Total Orders:", sean.orders_total)
    print("Total Quarterly Orders:", sean.orders_quarter)
    print("RFM: {0}, {1}, {2}". 
          format(sean.recency, sean.frequency, sean.monvalue))
main()