# The "Recipe" (The function that makes the generator)
def get_data_stream():
    return (x for x in range(5))

# Use it as many times as you want by calling the function
sum_result = sum(get_data_stream()) # 1st pass: The projector starts from the beginning
max_result = max(get_data_stream()) # 2nd pass: A NEW projector starts from the beginning