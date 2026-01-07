# keyword arguments = an argument preceded by an identifier
#           helps with readability
#           order of arguments dosn't matter
#           1. positional 2. default 3. KEYWORD 4. arbitrary

def number_cat(country , area, first , last):
    return f"{country}--{area}--{first}--{last}"

phone = number_cat(country = 1, area=123 , first = 456, last=7890)

print(phone)