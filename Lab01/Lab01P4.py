#
# Myiah Vanderheyden
# 08/22/2024
# This code will demonstrate my ability to write a program from scratch that will
# calculate price total before tax, total amount in taxes, and total after taxes
#

SALES_TAX = 0.065
BOOK_PRICE = 2.25
DVD_PRICE = 4.35
GAME_PRICE = 5.00

# This section will output to the user three prompts to collect item data
# I used int here as it makes sense to purchase whole items

numBooks = int(input('Enter the number of books: '))
numDvds = int(input('Enter the number of DVDs: '))
numGames = int(input('Enter the number of games: '))

# This section will process the user input data

totalForBooks = BOOK_PRICE * numBooks
totalForDvds = DVD_PRICE * numDvds
totalForGames = GAME_PRICE * numGames

totalBeforeTax = totalForBooks + totalForDvds + totalForGames
amountOfSalesTax = totalBeforeTax * SALES_TAX
totalAfterTax = amountOfSalesTax + totalBeforeTax

# This section will output the processed user data

print(f'Cost before tax: ${totalBeforeTax:10,.2f}')
print(f'      Sales tax: ${amountOfSalesTax:10,.2f}')
print(f' Cost after tax: ${totalAfterTax:10,.2f}')
