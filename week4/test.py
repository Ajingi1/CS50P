# import random
# def main():
#     rang_inpt = level()
#     randm_int = random.randint(1, rang_inpt)
#     while True:
#         user_gues = gues()
#         if user_gues < randm_int:
#             print("Too small!")
#         elif user_gues > randm_int:
#             print("Too large!")
#         elif user_gues == randm_int:
#             print("Just right!")
#             break
# def level():
#     try:
#         level_input = int(input("Level:"))
#         if level_input > 0:
#             return level_input
#         else:
#             return level()
#     except ValueError:
#         return level()
# def gues():
#     try:
#         user_gues = int(input("Guess:"))
#         return user_gues
#     except ValueError:
#         return gues()
# if __name__ == '__main__':
#     main()
# range_input = int(input("Level:"))
# gues_n = random.randint(1, range_input)
# while True:
#     user_input = input("Guess:")
#     if user_input.isnumeric():
#         user_input = int(user_input)
#         if user_input <= 0:
#             ...
#         if not user_input < range_input :
#             print("Too large!")
#         elif user_input > gues_n:
#             print("Too large!")
#         elif user_input < gues_n:
#             print("Too small!")
#         elif user_input == gues_n:
#             print("Just right!")
#             break
