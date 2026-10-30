# *args allows a function to accept any number of positional arguments,
# and **kwargs allows it to accept any number of keyword arguments.

# Inside the function, *args becomes a tuple and **kwargs becomes a dictionary.

def order_summary(*args, **kwargs):
    print("Items ordered:", args)
    print("Delivery details:", kwargs)

order_summary("pizza", "garlic bread", city="Delhi", time="8 PM")
