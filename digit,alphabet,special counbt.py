sample_str = "P@yn2at&#i5ve"
char_count = 0
digit_count = 0
symbol_count = 0
for char in sample_str:
    if char.isalpha():
            char_count += 1
    elif char.isdigit():
            digit_count += 1

# if it is not letter or digit then it is special symbol
else:

    symbol_count += 1

print("Chars =", char_count, "Digits =", digit_count, "Symbol =", symbol_count)