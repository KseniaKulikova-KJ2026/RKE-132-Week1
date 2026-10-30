item1 = "apples" 
item2 = "bread"
item3 = "milk"
item4 = "eggs"

shopping_list = ["apples", "bread", "milk", "eggs"] 

#len()
print(f"We have {len(shopping_list)} items on the list.")

#append()
shopping_list.append("cheese")

#extend()
shopping_list.extend(["flour", "sugar", "beaking powder"])

print(f"We have {len(shopping_list)} items on the list.")


for item in shopping_list:
    print(item)