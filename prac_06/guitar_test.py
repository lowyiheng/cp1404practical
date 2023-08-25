from guitar import Guitar

guitars = Guitar("Gibson L-5 CES", 1922, "16035.40")
Another_guitar = Guitar("Another_guitar", 2013, "2342.40")
third_guitar = Guitar("tian ba", 2003, "888,888.88")
print(guitars.get_age())
print(guitars.is_vintage())
print(guitars)