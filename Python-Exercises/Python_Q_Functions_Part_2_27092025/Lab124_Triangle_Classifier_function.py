# Triangle Classifier
# Write a program that classifies a triangle based on its side lengths.
# Given three input values representing the lengths of the sides,
# determine if the triangle is equilateral (all sides are equal),
# isosceles (exactly two sides are equal), or scalene (no sides are equal).
# Use an if-else statement to classify the triangle

# user i/p - s1,s2,s3 - int
# o/p - iso, eq, scelene

s1 = float(input("Enter a first side length: "))
s2 = float(input("Enter a second side length: "))
s3 = float(input("Enter a third side length: "))


def classify_triangle(a, b, c):
    if a > 0 and b > 0 and c > 0:
        if a + b > c and a + c > b and b + c > a:
            if a == b == c:
                return "Equilateral"
            elif a == b or b == c or a == c:
                return "Isosceles"
            else:
                return "Scelene"
        else:
            print("Not a Triangle")
    else:
        print("Not a valid length")


result = classify_triangle(s1, s2, s3)
print(f"The triangle classified as : {result}")

# Triangle Inequality Theorem
# The sum of any two sides of a triangle must be greater than the third side
# If this condition is not met, the inputs cannot form a triangle