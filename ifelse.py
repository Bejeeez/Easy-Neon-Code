
print('Enter Name: ')
name = input()

print('Enter Age: ')
age = input()

if name == 'Alice':
    print('Hi, Alice.')
elif int (age) < 12:
    print('You are not Alice Kiddo')
elif int(age) < 2000:
    print('Unlike you, Alice is not undead, immortal vampire')
elif int(age) > 100:
    print('You are not Alice, grannie')
else:
    print('Hello, Stranger')

