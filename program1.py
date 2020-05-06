def multiplication_or_sum(num1, num2):
  product = num1 *num2
  if(product <= 1000):
    return product
  else:
    return num1 +num2

number1 = int(input("Enter 1st number "))
number2 = int(input("Enter 2nd number"))

result = multiplication_or_sum(number1, number2)
print("The result is", result)