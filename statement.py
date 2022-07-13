print(((10 + 2) * 100 / 5 - 200))

print(pow(2,10))

print(eval( "2.5+2.5" ))


test = "Learn Python"

print(id(test)) #memory address


# Python will also allocate the same memory address in the following two scenarios.
# The strings don’t have whitespaces and contain less than 20 characters.
# In case of Integers ranging between -5 to +255.


deneme = "batuhan"
print(id(deneme))

deneme_test = deneme
print(id(deneme_test))

test2 = 2 * 5 / 10
print(test2)
1.0
print(type(test2))


list_vowels = ['a','e','i']
list_vowels += ['o', 'u',]
print(list_vowels)

# Multi-line Statement
my_list = [ 1, \
    2, 3\
    ,4,5 \
]

result = (10 + 100
    * 5 - 5
    / 100 + 10
)
print(result)



# Identation
def demo_routine(num):
    print('I am a demo function')
    if num % 2 == 0:
        return True
    else:
        return False

num = int(input('Enter a number:'))
if demo_routine(num) is True:
    print(num, 'is an even number')
else:
    print(num, 'is an odd number')