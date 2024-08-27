#
# Myiah Vanderheyden
# 08/26/24
# This program will demonstrate my ability to write selection structures
# based on customer specifications
#

SALES_TAX = 0.065

# This section gathers user input for loyalty and purchase amount, then
# processes the data

purchaseAmount = float(input('Enter the total purchase amount: $'))
loyaltyCheck = input('Are you a part of the loyalty program? (y/n): ')
amountOfSalesTax = purchaseAmount * SALES_TAX
totalAfterTax = amountOfSalesTax + purchaseAmount

# This section is the selection structure in which the data is compared
# against customer specifications for the gift card award

if loyaltyCheck == 'y' and (50.00 <= purchaseAmount <= 100.00):
    giftCardAmount = 15
elif loyaltyCheck == 'y' and purchaseAmount > 100.00:
    giftCardAmount = 25
elif loyaltyCheck != 'y' and purchaseAmount > 100.00:
    giftCardAmount = 5
else:
    giftCardAmount = 0

# This section feeds back processed data and notifies the user of their
# sales tax, total after tax, and their gift card amount

print(f'        Sales tax: ${amountOfSalesTax:10,.2f}')
print(f'  Total after tax: ${totalAfterTax:10,.2f}')
print(f'Gift card awarded: ${giftCardAmount:10.2f}')
