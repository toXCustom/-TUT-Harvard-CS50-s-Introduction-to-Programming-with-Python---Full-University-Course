# Ask user for their name, remove whitespace from str and capitalize user's name
name = input("What's your name? ").strip().title()

# Say hello to user
print("hello, " + name)
print("hello,", name)
print("hello, ", end="")
print(name)
print(f"hello, {name}") 

# Split user's name into first name and last name
first, last = name.split(" ")

print(f"hello, {first}")