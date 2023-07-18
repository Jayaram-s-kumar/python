

import cmath

def find_roots(a, b, c):
    # Calculate the discriminant
    discriminant = (b ** 2) - (4 * a * c)

    # Check the value of the discriminant
    if discriminant >= 0:
        # Real roots
        root1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
        root2 = (-b - cmath.sqrt(discriminant)) / (2 * a)
        return root1, root2
    else:
        # Imaginary roots
        real_part = -b / (2 * a)
        imaginary_part = cmath.sqrt(-discriminant) / (2 * a)
        root1 = complex(real_part, imaginary_part)
        root2 = complex(real_part, -imaginary_part)
        return root1, root2

# Test the function
a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient c: "))

root1 , root2 = find_roots(a, b, c)

# Print the roots
print("Root 1:", root1)
print("Root 2:", root2)
