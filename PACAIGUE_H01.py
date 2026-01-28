word =input("Enter your word")

numbers = []
for i in range (1,7):
      num = int(input(f"enter your number {i}:"))
      numbers.append(num)

print(numbers)

word_length= len(word)
print(f"your word legth is {(word_length)}")

avg= sum(numbers) / len(numbers)
print(f"The average of the number is{avg}")

if word_length >avg:
      print(f"The length of the word{word} is greater than average")

elif word_length <avg:
      print("The length of the word{word} is less than the average")

else:
      print("rai is gay")
