text = "X-DSPAM-Confidence:    0.8475"

zero_position = text.find('0')
numbers = float(text[zero_position:])

print(numbers)