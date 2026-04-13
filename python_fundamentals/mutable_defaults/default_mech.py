def test_func(data=[]):
    data.append(1)

print(test_func.__defaults__) # Output: ([],)
test_func()
print(test_func.__defaults__) # Output: ([1],) <-- It changed!