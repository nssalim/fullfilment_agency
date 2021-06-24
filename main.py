# Fullfilment Agency
# Program to help minimise costs when delivering goods to consumers.  
# Write functions which can receive a variable number of keywords and positional arguments.
# Working with tests.

from fullfillment_agency import get_distance, format_price, SHIPPING_PRICES
from test import test_function

# Define calculate_shipping_cost()
# shipping_type has default argument
def calculate_shipping_cost(from_coords, to_coords, shipping_type = 'Overnight'):

# Both from_coords and to_coords are tuples, containing first the latitude and then the longitude. Because the get_distance() function looks for all four as separate arguments,  separate these variables out.

# Unpack from_coords and to_coords tuples into from_lat, from_long, to_lat, and to_long.
  from_lat, from_long = from_coords
  to_lat, to_long = to_coords
  # distance = get_distance(from_lat, from_long, to_lat, to_long)
  distance = get_distance(*from_coords, *to_coords)
# shipping_rate 
# use the provided SHIPPING_PRICES dictionary and fetch the key passed in as shipping_type
  shipping_rate = SHIPPING_PRICES[shipping_type]
  price = distance * shipping_rate
# return the formatted price, created by calling the provided format_price() on the price itself.
  return format_price(price)

# Test the function by calling 
test_function(calculate_shipping_cost)

# Define calculate_driver_cost() 


# Test the function by calling 
# test_function(calculate_driver_cost)

# Define calculate_money_made() 


# Test the function by calling 
# test_function(calculate_money_made)
