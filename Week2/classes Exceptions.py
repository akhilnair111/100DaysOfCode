""" There’s one very important family of class definitions built in to the Python language. An Exception is a class that inherits from Python’s Exception class.

We can validate this ourselves using the issubclass() function. issubclass() is a Python built-in function that takes two parameters. issubclass() returns True if the first argument is a subclass of the second argument. It returns False if the first class is not a subclass of the second. issubclass() raises a TypeError if either argument passed in is not a class.

issubclass(ZeroDivisionError, Exception)
# Returns True
Above, we checked whether ZeroDivisionError, the exception raised when attempting division by zero, is a subclass of Exception. It is, so issubclass returns True.

Why is it beneficial for exceptions to inherit from one another? Let’s consider an example where we create our own exceptions. What if we were creating software that tracks our kitchen appliances? We would be able to design a suite of exceptions for that need:

class KitchenException(Exception):
  """
  Exception that gets thrown when a kitchen appliance isn't working
  """

class MicrowaveException(KitchenException):
  """
  Exception for when the microwave stops working
  """

class RefrigeratorException(KitchenException):
  """
  Exception for when the refrigerator stops working
  """
In this code, we define three exceptions. First, we define a KitchenException that acts as the parent to our other, specific kitchen appliance exceptions. KitchenException subclasses Exception, so it behaves in the same way that regular Exceptions do. Afterward we define MicrowaveException and RefrigeratorException as subclasses.

Since our exceptions are subclassed in this way, we can catch any of KitchenException‘s subclasses by catching KitchenException. For example:

def get_food_from_fridge():
  if refrigerator.cooling == False:
    raise RefrigeratorException
  else:
    return food

def heat_food(food):
  if microwave.working == False:
    raise MicrowaveException
  else:
    microwave.cook(food)
    return food

try:
  food = get_food_from_fridge()
  food = heat_food(food)
except KitchenException:
  food = order_takeout()
In the above example, we attempt to retrieve food from the fridge and heat it in the microwave. If either RefrigeratorException or MicrowaveException is raised, we opt to order takeout instead. We catch both RefrigeratorException and MicrowaveException in our try/except block because both are subclasses of KitchenException.

Explore Python’s exception hierarchy in the Python documentation!

Instructions
1.
In script.py we’ve defined a CandleShop class for our new candle shop that we’ve named Here’s a Hot Tip: Buy Drip Candles. We want to define our own exceptions for when we run out of candles to sell.

Define your own exception called OutOfStock that inherits from the Exception class.

2.
Have CandleShop raise your OutOfStock exception when CandleShop.buy() tries to buy a candle that’s out of stock. """



# Define your exception up here:
class OutOfStock(Exception):
  pass

# Update the class below to raise OutOfStock
class CandleShop:
  name = "Here's a Hot Tip: Buy Drip Candles"
  def __init__(self, stock):
    self.stock = stock
    
  def buy(self, color):
    if self.stock[color] < 1:
      raise OutOfStock
    self.stock[color] = self.stock[color] - 1

candle_shop = CandleShop({'blue': 6, 'red': 2, 'green': 0})
candle_shop.buy('blue')

# This should raise OutOfStock:
# candle_shop.buy('green')