"""
syntax: lambda arguments: expression
A lambda function can take any number of arguments, but can only have one expression.
"""
number = [1, 2, 3, 4, 5]
result = list(filter(lambda x: x % 2 == 0, number))
print(result)  # Output: [2, 4]