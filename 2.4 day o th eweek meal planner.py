# Weekly meal plan [Breakfast, Lunch, Dinner] for 7 days
meal_plan = [
   ["Oatmeal", "Grilled Chicken Salad", "Spaghetti"], #pon
   ["Pancakes", "Sandwich", "Steak"], #wt
   ["Smoothie", "Chicken Wrap", "Salmon"], #śr
   ["Eggs", "Pasta", "Soup"], #czw
   ["Toast", "Burrito", "Pizza"], #pt
   ["Cereal", "Salad", "Fish Tacos"], #sob
   ["Bagel", "Rice and Beans", "Stir-fry"] #nd
]

# Returns a week day name
def weekday(n):
   weekdays = ["Monday", "Tuesday", "Wednesday",
      "Thursday", "Friday", "Saturday", "Sunday"]
   return weekdays[n-1]

# Returns a string with day meal names
# separated by comma

x = int(input("da day? "))

# Prints weekly meal plan
print(weekday(x), meal_plan[x - 1])