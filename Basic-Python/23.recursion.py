# def fact(n):
#     if n== 1:
#         return 1
#     return n*fact(n-1) #=> 5*fact(4),4*fact(3), 3*fact(2), 2*fact(1), 1

# def sum_no(n):
#     if n==0:
#         return 0
#     return n + sum_no(n-1) #=> 5+sum(4), 4+sum(3), 3+sum(2), 2+sum(1), 0



# print(fact(5))
# print(sum_no(5))



def multiply_dependencies(number, level=0):
    """
    Multiply a number recursively with its dependencies (factors).
    Each number depends on factors less than itself.
    """
    if number <= 1:
        return []  # Base case: no dependencies for 1 or below

    # Direct dependencies are the factors of the current number (except 1 and itself)
    factors = [i for i in range(2, number) if number % i == 0]

    # Resulting products for this level
    products = []
    for factor in factors:
        # Multiply the current number by the factor
        product = number * factor
        products.append(product)
        print(f"Level {level}: Multiplying {number} * {factor} = {product}")
        
        # Recursively find and extend dependencies (sub-products) for the factor
        sub_products = multiply_dependencies(factor, level + 1)
        print('products',products)
        print('sub_products',sub_products)
        products.extend(sub_products)  # Add sub-products to the current product list
        print('products-2',products)
    return products


# Call the function with an initial number, e.g., 6
result = multiply_dependencies(6)

# Print the final list of all products
print("All multiplications:", result)