# დავალებაN1: ჰიპოტენუზას გამომთვლელი პროგრამა
a = int(input("შეიყვანეთ პირველი კათეტის სიგრძე: ")) # პრიველი კათეტის სიგრძე
b = int(input("შეიყვანეთ მეორე კათეტის სიგრძე: ")) # მეორე გაკეთის სიგრძე
c = int((a ** 2 + b ** 2) ** .5) # ჰიპოტენუზას სიგრძე
print(f"ჰიპოტენუზას სიგრძეა: {c}")

# დავალება N2: წამების გამოსაანგარიშეებელი პროგრამა
total_seconds = int(input("შეიყვანეთ წამების რაოდენობა: "))
hours = total_seconds // 3600
remaining_seconds = total_seconds % 3600
minutes = remaining_seconds // 60
seconds = remaining_seconds % 60
print(f"{total_seconds} წამი არის {hours} საათი, {minutes} წუთი, {seconds} წამი.")
