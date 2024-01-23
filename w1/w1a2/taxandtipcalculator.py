tip = 0.15
tax = 0.21

costofmeal = input()

costofmeal = float(costofmeal)

taxamount = costofmeal * tax
tipamount = costofmeal * tip

taxamount = float(taxamount)
tipamount = float(tipamount)

total = costofmeal + taxamount + tipamount

taxamount = "%.3f" % (taxamount)
tipamount = "%.3f" % (tipamount)
total = "%.3f" % (total)

# print(f"Tax: {taxamount}, Tip: {tipamount}")

print(f"Tax: {taxamount} Tip: {tipamount} Total: {total}")