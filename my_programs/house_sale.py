# phil welsby - 20 june 2021

# program to calculate cost of selling house

# import libraries
from os import system

# clear screen
system('clear')

# get data from user
nat_west = float(input('How much is your Nat West account? '))
nat_west_rewards = float(input('How much are your Nat West Rewards? '))
halifax = float(input('How much is your Halifax account? '))
loan = float(input('How much is owed on your Nat West loan? '))
cash = float(input('How much cash do you have? '))
house_sold_for = float(input('How much are you selling your house for? '))
house_bought_for = float(input('How much are you paying for your new house? ' ))
existing_mortgage = float(input('How much is owed on your mortgage? '))
existing_mortgage = existing_mortgage/100*102
estate_agent_fee = house_sold_for / 100 * 0.75
estate_agent_fee = estate_agent_fee / 100 * 120
misc_costs = int(input('How much are any miscellaneous costs? '))
refurb = int(input('How much are you spending on refurbishment? '))
balance = house_sold_for - house_bought_for - existing_mortgage - misc_costs - estate_agent_fee - refurb

# print results
print('\n' * 10)
print('House sold for                 £', house_sold_for)
print('House bought for               £', house_bought_for)
print('Existing mortgage inc fee      £', existing_mortgage)
print('misc costs (solicitor etc)     £', misc_costs)
print('Estate Agent Fee inc VAT       £', estate_agent_fee)
print('Cost of any refurbishment      £', refurb)
print('Your remaining balance from the house sale will be £', balance)
print()
print('Nat West balance               £', nat_west)
print('Nat West Rewards               £', nat_west_rewards)
print('Halifax balance                £', halifax)
print('Cash                           £', cash)
print('Cash total after sale          £', nat_west + nat_west_rewards + halifax + balance + cash)
#print('Assets                         £', house_bought_for)
#print('Ammount owed on Nat West Loan  £', loan)
print()
print('Value of new house             £', house_bought_for)
print('Total Cash to hand             £', nat_west + nat_west_rewards + halifax + balance + cash)
print('Your Assets are                £', balance + nat_west + nat_west_rewards + halifax + house_bought_for)
print('Your liabilities are           £', loan)
print()
print('Your Net Worth is               £', balance + nat_west + nat_west_rewards + halifax + house_bought_for - loan)


