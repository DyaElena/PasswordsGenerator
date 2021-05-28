import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'

passwords_amount = int(input('Enter how many passwords you need to generate: '))
lengh = int(input("Enter a password's lenght: "))
numbers = input('Do you want numbers in you password? Enter Yes/No: ')
lowercase = input('Do you want lowercase letters in you password? Enter Yes/No: ')
uppercase = input('Do you want uppercase letters in you password? Enter Yes/No: ')
symbols = input('Do you want symbols in you password? Enter Yes/No: ') 
lo01 = input('Include confucing letters and symbols in password: il1Lo0O? Enter Yes/No: ')

chars= ''
def add_smth(reply, smthtoadd):
    if reply.lower() == 'yes':
      return chars + smthtoadd
    else:
      return chars
c1 = add_smth(numbers, digits)
c2 = add_smth(lowercase, lowercase_letters)
c3 = add_smth(uppercase, uppercase_letters)
c4 = add_smth(symbols, punctuation)
char = c1 + c2 + c3 + c4
if lo01.lower() == 'no':
  for i in char:
    if i in ['i', 'l', '1', 'L', 'o', '0', 'O']:
      char = char.replace(i , '')

while passwords_amount > 0:
  for _ in range(lengh):
    password = random.sample(char, lengh)
  print(''.join(password))
  passwords_amount -= 1




