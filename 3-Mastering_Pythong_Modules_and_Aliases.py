# Task 1: Custom Module with Aliases

import text_utils as tu # Import text_utils using an alias

s = "This is my test string."

# Testing
print(f"Original String: {s}")
print(f"Reverse String: {tu.reverseString(s)}")
print(f"Capitalize String: {tu.capitalizeString(s)}")
print(f"Lowercase String: {tu.lowercaseString(s)}")