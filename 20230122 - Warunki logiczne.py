# Warunki logiczne
# "and" ma pierwszeństwo przed "or"
# https://pythongeeks.org/python-operator-precedence/

temp = 12
is_sun_shining = False

# Example 1
if temp > 0 and is_sun_shining is not False:
    print("Idziemy na spacer")
else:
    print("Zostajemy w domu")

# Example 2
if temp > 0 or is_sun_shining is not False:
    print("Idziemy na spacer")
else:
    print("Zostajemy w domu")

# Example 3
if temp < 0 or is_sun_shining == False:
    print("Zostajemy w domu")
else:
    print("Idziemy na spacer")

# Example 4
# Wyświetl tylko liczb nieparzystych
for i in range(0, 10):
    if not (i % 2) == 0:
        print(i)
    else:
        print("*")

# Example 5
b = 1
if b in (1, 2, 3):
    print("TAK")
else:
    print("NIE")

if b not in (1, 2, 3):
    print("TAK")
else:
    print("NIE")

# Example 6
b2 = 1
c = [1, 2, 3]

if b2 not in c:
    print("nie")
    print(type(c))
else:
    print("tak")