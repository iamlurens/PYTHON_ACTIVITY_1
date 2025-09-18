
user_name = "Lawrence Sanchez"
user_city = "Alcala"
user_age = 21
user_height = 1.67
is_student = True


greeting = "Hello, " + user_name + " from " + user_city + "!"
print("Concatenated greeting:", greeting)
print("-" * 30)

print("Name in uppercase:", user_name.upper())
print("Name in lowercase:", user_name.lower())
print("Name length:", len(user_name), "characters")


print(f"Formatted user info: {user_name} is {user_age} years old, "
      f"{user_height}m tall, and lives in {user_city}.")


print("=== DATA TYPE INFORMATION ===")
print("Type of user_name:", type(user_name))
print("Type of user_age:", type(user_age))
print("Type of user_height:", type(user_height))
print("Type of is_student:", type(is_student))
