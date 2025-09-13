# Triangle Classifier
# Write a program that classifies a triangle based on its side lengths.
# Given three input values representing the lengths of the sides,
# determine if the triangle is equilateral (all sides are equal),
# isosceles (exactly two sides are equal), or scalene (no sides are equal).
# Use an if-else statement to classify the triangle

# user i/p - s1,s2,s3 - int
# o/p - iso, eq, scelene

s1 = int(input("Enter a first side length: "))
s2 = int(input("Enter a second side length: "))
s3 = int(input("Enter a third side length: "))

if s1==s2 and s1==s3:
    print("All sides are equal, Hence, it's a equilateral triangle")
elif s1==s2 or s1==s3 or s2==s3:
    print("Two sides are equal, Hence, it's a isosceles triangle")
else:
    print("All sides are not equal, Hence, it's a scalene triangle")
