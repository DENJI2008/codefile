with open("sample.txt", "r") as f:
    text = f.read()
vowels = consonants = upper = lower = 0
for ch in text:
    if ch.isalpha():
        if ch.lower() in "aeiou":
            vowels += 1
        else:
            consonants += 1
    if ch.isupper():
        upper += 1
    if ch.islower():
        lower += 1
print("Vowels:", vowels,
      "Consonants:", consonants,
      "Uppercase:", upper,
      "Lowercase:", lower)
