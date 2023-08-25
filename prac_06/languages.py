from programming_language import Programming_language

python = Programming_language("Python", "Dynamic", True, 1991)
ruby = Programming_language("Ruby", "Dynamic", True, 1995)
visual_basic = Programming_language("Visual Basic", "Static", False, 1991)
java = Programming_language("Java","Static", True, 1995)
Cpp = Programming_language("C++", "Static", False, 1983)
print(python.is_dynamic())
print(python)
print("The dynamically typed languages are:")
lists = [python, ruby, visual_basic]
for list in lists:
    if list.is_dynamic():
        print(list.getName())