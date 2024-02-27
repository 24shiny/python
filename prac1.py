# 2-3
name = "eric"
print(f"morning, {name}, how are you doing?")

# 2-4
print(name.upper())
print(name.lower())
print(name.title())

#2-5, 2-6
name_quote = "Ernesto Che Guevara"
quote = "Be the realist, but dream unrealistic dream in your heart."
motivation_msg = f"{name_quote}, quote"
print(motivation_msg)

#2-7
name_test = "\nErnesto\t"
print(name_test.rstrip())
print(name_test.lstrip())
print(name_test.strip())

#2-8
file_name="python_notes.txt"
print(file_name.removesuffix(".txt"))