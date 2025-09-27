# Tuple
# Collection of Items
# ()
# Immutable

my_tuple = (1, 4, 9, 16, 25)
# my_tuple[3] = 64  # TypeError: 'tuple' object does not support item assignment


shopping_list = ["bread", "butter", "Paneer"]
shopping_list[2] = "milk"
print(shopping_list)

# Real of Tuples
my_tuple = ("ttta.com", "sdet.live")
my_api_list = list(my_tuple)
print(my_api_list)
# my_tuple[0] = "abc.com" # TypeError: 'tuple' object does not support item assignment


# Real case, where we use Tuples
API_URLs = ("https://sdet.live/python0x", "https://awesomqa.com" )
print(API_URLs[0])
print(API_URLs[1])