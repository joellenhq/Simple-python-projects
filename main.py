from arithmetic_arranger import arithmetic_arranger
from time_calculator import add_time
import budget
from budget import create_spend_chart
import shape_calculator

print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))


print(add_time("11:59 PM", "24:05"))
print(add_time("11:06 PM", "2:02"))
print(add_time("3:30 PM", "2:12"))

food = budget.Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())
clothing = budget.Category("Clothing")
#food.print_obj()
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = budget.Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)

print(food)
print(clothing)

print(create_spend_chart([food, clothing, auto]))

rect = shape_calculator.Rectangle(5, 10)
print(rect.get_area())
rect.set_width(3)
print(rect.get_perimeter())
print(rect)

sq = shape_calculator.Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)