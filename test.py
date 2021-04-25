class Test:
    a = 123


b = Test()
print(b.a, Test.a)
b.a = 213
print(b.a, Test.a)