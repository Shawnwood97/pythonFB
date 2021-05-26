def fizzbuzz(num):
  if(num % 3 == 0 and num % 5 == 0):
    print('FizzBuzz')
  elif(num % 3 == 0):
    print('Fizz')
  elif(num % 5 == 0):
    print('Buzz')
  else:
    print('Number not divisiable by 3 or 5')

numbers = [31, 1, 77, 20, 90, 100, 46, 38, 74, 51, 62, 27, 41, 28, 85]

for num in numbers:
  fizzbuzz(num)

