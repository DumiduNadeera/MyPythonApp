class Car:
	# Define a Car class for storing brand and speed data.

	def __init__(self, brand, speed):
		# Initialize a new Car instance with its brand and starting speed.
		self.brand = brand
		self.speed = speed

	def display(self):
		# Print the car's current brand and speed.
		print(f"Car is {self.brand} & speed {self.speed}")

	def accelarate(self, speed):
		# Increase the car's speed by the given amount.
		self.speed = self.speed + speed

# Create first Car instance with brand Toyota and speed 60.
my_car = Car("Toyota", 60)
# Create second Car instance with brand BMW and speed 0.
my_car2 = Car("BMW", 0)
# Show the first car's details.
my_car.display()
# Show the second car's details.
my_car2.display()
				
