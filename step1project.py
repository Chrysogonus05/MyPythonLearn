# Step 1: Get user input
name = input("Enter your name: ")
age = int(input("Enter your age: "))  # Convert input to integer
hobby = input("Enter your hobby: ")

# Step 2: Calculate future age
future_age = age + 10

# Step 3: Display the info card
print("=== Personal Info Card ===")
print("Name:", name)
print("Age:", age)
print("Hobby:", hobby)
print("In 10 years, you’ll be:", future_age)
print("==========================")