import math

print('Volume/Area Converter')

type_of_conversion = input('''
                    c - Cone
                    y - Cylinder
                    s - Sphere
''').upper()

pi = math.pi

if type_of_conversion == 'C':
    radius = int(input('Radius: '))
    height = int(input('Height: '))
    length = math.sqrt(radius**2 + height**2)

    volume = (pi * radius**2 * height) / 3
    area = pi * radius**2 + pi * radius * length

    print(f'Volume: {volume}')
    print(f'Surface Area: {area}')
elif type_of_conversion == 'Y':
    radius = int(input('Radius: '))
    height = int(input('Height: '))

    volume = pi * radius**2 * height
    area = 2 * pi * radius**2 + 2 * pi * radius * height

    print(f'Volume: {volume}')
    print(f'Surface Area: {area}')
elif type_of_conversion == 'S':
    radius = int(input('Radius: '))

    volume = (4 * pi * radius**3) / 3
    area = 4 * pi * radius**2
    
    print(f'Volume: {volume}')
    print(f'Surface Area: {area}')
else:
    print('That is not a valid calculation type')