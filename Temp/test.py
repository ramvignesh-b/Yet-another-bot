n = 158
suffix = { 1: "st", 2: "nd", 3: "rd" }.get(n if (n < 20) else (n % 10), 'th')
print(str(n)+suffix)