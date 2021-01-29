# phil welsby - 24 jan 2021
# program to keep track on finances

import os
os.system('clear')  # clear screen
# variables to hold direct debits
british_gas = 1.45
mortgage = 439.16
united_utilities = 34.86
tv_licence = 13.37
natwest_loan = 136.08
trafford_mbc = 128.00
denplan_dentist = 43.35
unite_the_union = 14.95
eon = 82.00
virgin_media = 26.00

# total outgoings
total_out = british_gas + mortgage + united_utilities + tv_licence + natwest_loan + trafford_mbc + denplan_dentist + unite_the_union + eon + virgin_media


feb_mar_outgoings = total_out - united_utilities - trafford_mbc


current_ballance = float(input('Enter current ballance: '))
os.system('clear')  # clear screen


reduced_month = current_ballance - feb_mar_outgoings

normal_month = current_ballance - total_out


print('\n\n\n')
print('NORMAL MONTH')
print('Current Ballance is £', '%.2f' % current_ballance)
print('Normal months payments are £', '%.2f' % total_out)
print('End of a normal month, estimate is', '£', '%.2f' % normal_month)
print()
print('------------------------------------------------------------------')
print()
print('REDUCED MONTH')
print('Current Ballance is £', '%.2f' % current_ballance)
print('Reduced month payments are £', '%.2f' % feb_mar_outgoings)
print('End of reduced month, estimate is £', '%.2f' % reduced_month)
