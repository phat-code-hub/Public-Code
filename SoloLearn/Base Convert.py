letter_set=[chr(i) for i in range(97,123)]
digital_set=[chr(i) for i in range(48,58)]
digital_set.extend(letter_set)
print(digital_set)