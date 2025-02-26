# 1 დავალება
# def transaction_fee(func):
#     def wrapper(balance, amount):
#         fee = 1
#         total_amount = amount + fee
#         if balance < total_amount:
#             return "Error: Insufficient funds in the account."
#         return func(balance - total_amount, amount)
#     return wrapper
#
# @transaction_fee
# def make_transaction(balance, amount):
#     return f"Transaction successful! Remaining balance: {balance} GEL."
#
# print(make_transaction(10, 5))
# print(make_transaction(5,5))

# 2 დავალება
#
# class MethodNameValidatorMeta(type):
#     def __new__(cls, name, bases, class_dict):
#         for attr_name, attr_value in class_dict.items():
#             if callable(attr_value) and not attr_name.startswith("_"):
#                 raise ValueError(f"Method name '{attr_name}' must start with an '_' symbol!")
#         return super().__new__(cls, name, bases, class_dict)
#
# მაგალითები
# class ValidClass(metaclass=MethodNameValidatorMeta):
#     def _valid_method(self):
#         pass
#
# class InvalidClass(metaclass=MethodNameValidatorMeta):
#     def invalid_method(self):
#         pass