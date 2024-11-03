from programming_language import ProgrammingLanguage

# Create instances of ProgrammingLanguage
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

# Test the __str__ method
print(python)

# Create a list of ProgrammingLanguage objects
languages = [python, ruby, visual_basic]

# Loop through and print the names of all the languages with dynamic typing
print("The dynamically typed languages are:")
for language in languages:
    if language.is_dynamic():
        print(language.name)
