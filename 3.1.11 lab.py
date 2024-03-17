#Once upon a time there was a land – a land of milk and honey, inhabited by happy and prosperous people. The people paid taxes, of course – their happiness had limits. The most important tax, called the Personal Income Tax (PIT for short) had to be paid once a year, and was evaluated using the following rule:

#if the citizen's income was not higher than 85,528 thalers, the tax was equal to 18% of the income minus 556 thalers and 2 cents (this was what they called tax relief)
#if the income was higher than this amount, the tax was equal to 14,839 thalers and 2 cents, plus 32% of the surplus over 85,528 thalers.

#answer :

income = float(input("Enter the annual income: "))

if income < 85528:
	tax = income * 0.18 - 556.02
else:
	tax = income * 0.2 + 32/100 - 14839.02
	
if tax < 0.0:
	tax = 0.0

tax = round(tax, 0)
print("The tax is:", tax, "thalers")
 