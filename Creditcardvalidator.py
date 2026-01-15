#remove -  or "  "
# add digits
# double  evry second digit
# sum totals
# if sum is divisible by 10  valid

sum_odd = 0
sum_even = 0
total = 0

#step 1
card_num = input("Enter credit card number: ")
card_num = card_num.replace("-", "")
card_num = card_num.replace(" ", "")

card_num = card_num[::-1]


#step 2
for x in card_num[::2]:
    sum_odd += int(x)
    
#step 3
for x in card_num[1::2]:
    x = int(x) * 2
    if x >=  10:
        sum_even += ((x %  10) + 1)
    else:
        sum_even += x
        
#step 4
total = sum_odd + sum_even


#step 5
if total % 10  ==0:
    print("Valid credit card number")
else:
    print("Invalid credit card number")