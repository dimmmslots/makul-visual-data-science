user_input = input("Enter a number: ")
between_6_and_10 = 6 < int(user_input) < 10
lte_6_or_gte_10 = int(user_input) <= 6 or int(user_input) >= 10
not_6_or_10 = int(user_input) != 6 or int(user_input) != 10
is_6_or_10 = int(user_input) == 6 or int(user_input) == 10

print(f"Between 6 and 10: {between_6_and_10}")
print(f"Less than or equal to 6 or greater than or equal to 10: {lte_6_or_gte_10}")
print(f"Not 6 or 10: {not_6_or_10}")
print(f"Is 6 or 10: {is_6_or_10}")