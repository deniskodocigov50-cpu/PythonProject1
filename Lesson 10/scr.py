with open ('example.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    print(content)
with open('example.txt', 'w', encoding='utf-8') as file:
    file.write('Hello World')
with open('example.txt', 'a', encoding='utf-8') as file:
    file.write('\nHi there')

contacts = {'Иван': "123-456", 'Mary': "456-789"}

with open ('contacts.txt', 'w', encoding='utf-8') as file:
    for name, number in contacts.items():
        file.write(f"{name}: {number}\n")

try:
    with open ('contacts.txt', 'r', encoding='utf-8') as file:
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print("File not found")

#with open('', 'rb') as file:
    #data = file.read()
    #print(data.decode())

