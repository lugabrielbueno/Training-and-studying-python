#Change Return Program - The user enters a cost and then the amount of money given. The program will figure out the change and the number of quarters, dimes, nickels, pennies needed for the change.

class Cash_Register:
    def __init__(self):
        pass

 # A method to receive the cost and money        
    def receive(self):
        self.cost = round(float(input('Cost : ')),2)
        self.money = round(float(input('Money : ')),2)

        #Condition, money need be more than cost 
        if self.money < self.cost:
            print('Sorry, missing {} dollars'.format(self.cost-self.money))

# A method to do the change
    def change(self):
        #Defining parameters
        self.change = round((self.money - self.cost),2)
        self.notes = self.change//1
        self.coins = round((self.change - self.notes),2)*100
        print(self.coins)

        #A function to check every coin
        def check_coins(n):
            self.n = n
            self.coins -=  self.n
            return self.coins
                  
        print('Change : ${}'.format(self.change))
        print('${}'.format(self.notes))

        #Counting each coin that the client will be receive in change
        if self.coins >= 25 :
            print((str(self.coins//25)) + ' twenty five coins')

            #Reducing the '25' coins that has been changed
            check_coins(25*(self.coins//25))
        if self.coins >= 10:
            print((str(self.coins//10))+ ' ten coins')
            #Reducing the '10' coins that has been changed
            check_coins(10*(self.coins//10))
        if self.coins >= 5:
            print((str(self.coins//5))+' five coins')
            #Reducing the '5' coins that has been changed
            check_coins(5*(self.coins//5))


register = Cash_Register()
register.receive()
register.change()