
#Method 1
def data_factory():
    return (x for x in range(5))

total = sum(data_factory())
maximum = max(data_factory())

print(total, maximum)

#Method 2
from itertools import tee

data_gen = (x for x in range(5))
# Split the original into two independent streams
gen1, gen2 = tee(data_gen) 

print(sum(gen1)) # Consumes gen1
print(max(gen2)) # Consumes gen2 (completely separate from gen1)


#Method 3: Re-instantiating
# The Template (The Recipe)
recipe = lambda: (x for x in range(5))

# Instantiation 1
gen1 = recipe() 
# Instantiation 2 (A brand new projector)
gen2 = recipe()