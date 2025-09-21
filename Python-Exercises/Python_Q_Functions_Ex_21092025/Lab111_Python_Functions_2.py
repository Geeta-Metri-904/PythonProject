public_toilet = "PB"

def home():
    private_toilet = "PT" # local variable, within the function
    print(private_toilet)
    print(public_toilet)

def strange():
    print(private_toilet)
    print(public_toilet)

print(public_toilet)
#print(private_toilet)

# local variable has the more preference than the global