# phil welsby - 22 june 2021

# program to calculate electricity usage
# current charge for 1 kWh is 18.31p
# current charge for standing charge is 24.39p per day
# vat is 5% of net

# show current prices
print('price per kWh is currently 18.31p')
print('price per day standing charge is currently 24.39p')
# get meter reading
start_meter = float(input('Enter the START meter: '))
end_meter = float(input('Enter the END meter: '))
total_meter = end_meter - start_meter
#print('Meter Reading', total_meter)

# get cost of kWh in pence
cost_per_kWh = float(input('Enter cost per kWh in pence: '))
cost_per_kWh = cost_per_kWh / 100
#print('cost per kWh £', cost_per_kWh)

# get number of days since last reading
days = int(input('Enter number of days since last reading: '))
#print('Days', days)

# calculate standing charge
standing_charge_per_day = float(input('Enter standing charge per day in pence: '))
standing_charge_per_day = standing_charge_per_day / 100
standing_charge = standing_charge_per_day * days
#print('Standing charge £', standing_charge)

# calculate cost of energy used
cost_of_energy_used = total_meter * cost_per_kWh
total_net_cost = cost_of_energy_used + standing_charge
print('\n\n')
#print('Subtotal of charges before VAT £', total_net_cost)

# calculate vat
vat = total_net_cost / 100 * 5
#print('Vat                            £', vat)

# calculate cost of total energy used
total_electricity_charges = total_net_cost + vat
#print('Total Energy Charges           £', total_electricity_charges)

print('Energy Used', total_meter, 'kWh @', cost_per_kWh * 100,'p/kWh   £',cost_of_energy_used)
print('Standing charge', days, 'days @', standing_charge_per_day * 100, 'p   £',standing_charge)
print('Subtotal of charges before VAT       £', total_net_cost)
print('VAT @ 5%                             £', vat)
print('Total Electricity Charges            £', total_electricity_charges)

kWh_average = total_meter/days

print('\nAverage kWh per day for this period is', kWh_average, 'kWh')
print()
