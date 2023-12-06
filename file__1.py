
# if __name__ == '__main__':
# print(111)
# print(222)
# print(555)

# a = {'name':'Vasya','surname':'Petrov', 'age':25}
# print(a['surname'])


a = {1:'qwe'}
b = a 
b[1] = 'asv'
print(a)


# c = 500000000000000
# v = 500000000000000
# print(c == v)
# print(c is v)

# print(id(c))
# print(id(v))


# z = ({},2)
# z[0][3]= 'f'
# print(z)

print('=' * 30)

d = 0 
p = d 
print(d,p)

d = d + 1 
print(d,p)
# перезаписали p
p = d
print(d,p)

u = [1,2,3]
y = u
print(u,y)
u.append(7)
print(y)
print(u)
name = "John"
print('Hi, %s' % name)


print("="*30)


get_cube = lambda x : x ** 3
print(get_cube)