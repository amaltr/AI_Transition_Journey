import sys

# 1. The "Box" (List)
list_data = [x**2 for x in range(1000000)]
print(f"List size in bytes: {sys.getsizeof(list_data)}")

# 2. The "Instruction" (Generator Expression)
gen_data = (x**2 for x in range(1000000))
print(f"Generator size in bytes: {sys.getsizeof(gen_data)}")

# for i in gen_data:
#     for n in gen_data:
#         print(i,n)
#         break
#     break