# Fullfilment Agency
# Program to help minimise costs when delivering goods to consumers and finding out which employee is the best person for a job.
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
# function to take an arbitrary number of positional driver variables
def calculate_driver_cost(distance, *drivers):
# In order to find the best person, calculate how much it would cost for any of the drivers to fulfill this order.
  cheapest_driver = None
  cheapest_driver_price = None
  for driver in drivers:
    driver_time = driver.speed * distance
    price_for_driver = driver.salary * driver_time
# Now check if the current driver is the cheapest driver.
    if cheapest_driver is None:
      cheapest_driver = driver
      cheapest_driver_price = price_for_driver
    elif price_for_driver < cheapest_driver_price:
      cheapest_driver = driver
      cheapest_driver_price = price_for_driver
  return cheapest_driver_price, cheapest_driver

# Test the function by calling 
test_function(calculate_driver_cost)

# Define calculate_money_made() 


# Test the function by calling 
# test_function(calculate_money_made)


