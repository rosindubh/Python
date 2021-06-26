# phil welsby - 26 june 2021
# simple program to calculte my electric bill

from os import system
from time import sleep

# clear screen
def clear():
    system('clear')

clear()

#get starting meter
def start():
    try:
        start_meter = int(input('Enter start meter: '))
        print('Start meter is',start_meter, 'is this correct?')
        check = input()
        if check == 'n':
            start()
        else:
            return start_meter
    except ValueError:
        print('The value you have entered is not recognised!!!')
        print('Please try again')
        input('Hit ENTER to continue...')
        clear()
        start()

# get end meter
def end():
    try:
        end_meter = int(input('Enter end meter: '))
        print('Ending meter is', end_meter, 'is this correct?')
        check = input()
        if check == 'n':
            end()
        else:
            return end_meter
    except ValueError:
        print('The value you have entered is not recognised!!!')
        print('Please try again')
        input('Hit ENTER to continue...')
        clear()
        end()

# get days since last reading
def number_of_days():
    try:
        days = int(input('Enter number of days since last bill: '))
        print('Number of days since last reading is', days, 'is this correct?')
        check = input()
        if check == 'n':
            number_of_days()
        else:
            return days
    except ValueError:
        print('The value you have entered is not recognised!!!')
        print('Please try again')
        input('Hit ENTER to continue...')
        clear()
        number_of_days()

# get cost per kWh
def kwh_cost():
    try:
        cost_per_kwh = float(input('Enter the cost per kWh in pence: '))
        print('Cost per kwh is', cost_per_kwh, 'is this correct?')
        check = input()
        if check == 'n':
            kwh_cost()
        else:
            return cost_per_kwh
    except ValueError:
        print('The value you have entered is not recognised!!!')
        print('Please try again')
        input('Hit ENTER to continue...')
        clear()
        kwh_cost()

# get standing charge cost per day
def std_chg_per_day():
    try:
        standing_charge = float(input('Enter standing charge cost per day in pence: '))
        print('Standing charge cost per day is', standing_charge, 'is this correct?')
        check = input()
        if check == 'n':
            std_chg_per_day()
        else:
            return standing_charge
    except ValueError:
        print('The value you have entered is not recognised!!!')
        print('Please try again')
        input('Hit ENTER to continue...')
        clear()
        std_chg_per_day()


# main

start_meter = start()
clear()
end_meter = end()
clear()
number_of_days = number_of_days()
clear()
kwh_cost = kwh_cost()
clear()
std_chg_per_day = std_chg_per_day()
clear()

# calculate values for print out
energy_used = (end_meter - start_meter)*kwh_cost/100
standing_charge = number_of_days * std_chg_per_day / 100
sub_total = energy_used + standing_charge
vat = sub_total / 100 * 5
total_electric_charges = sub_total / 100 * 105
avg_kwh_per_day = (end_meter - start_meter) / number_of_days

# print out values to stdout
print('Energy used', end_meter-start_meter, '@', kwh_cost, 'p           £', energy_used)
print('Standing charge', number_of_days, '@', std_chg_per_day, 'p        £',standing_charge) 
print('Subtotal of charges before VAT     £', sub_total)
print('VAT @ 5%                           £', vat)
print('Total Electricity Charges          £', total_electric_charges)
print('\n' * 3)
print('Average kWh per day =', avg_kwh_per_day)
print('\n' * 5)

