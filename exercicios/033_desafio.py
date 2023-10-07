n1 = int(input('DIgite um número: '))
n2 = int(input('DIgite outro número: '))
n3 = int(input('DIgite outro número: '))

if n1 > n2 and n1 > n3:
    print('{} é maior digitado'.format(n1))

if n2 > n1 and n2 > n3:
    print('{} é maior digitado'.format(n2))

if n3 > n1 and n3 > n2:
    print('{} é maior digitado'.format(n3))

if n1 < n2 and n1 < n3:
    print('{} é menor digitado'.format(n1))

if n2 < n1 and n2 < n3:
    print('{} é menor digitado'.format(n2))

if n3 < n1 and n3 < n2:
    print('{} é menor digitado'.format(n3))
