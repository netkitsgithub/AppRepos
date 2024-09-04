# print("Welcome to AI")
# high = float(input("Press any key to continue:"))
# weight = float(input("Press any key to continue:"))
# conclusion = print("Hight*Weight"+str(high*weight))



# shopping_list = []
# shopping_list.append("列表1")
# shopping_list.append("列表2")
# shopping_list.append("列表3")
# print(shopping_list)
# shopping_list.remove("列表2")
# print(shopping_list)
#
# wordsDictorys = {1:"你好",
#                 2:"再见",
#                 3:"晚安"}
# print(wordsDictorys[3])

# for i in range(13):
#     print("Hello")
#
# i=0
# while i < 100:
#     print(f"current number is{i}")
#     i=i+1

# class CuteCat:
#     def __init__(self):
#         self.name = "Cute cat"
#         self.description = "cat description"
#         self.weight = "cat weight"
#
#     def speak(self):
#         print("Cute cat says:",self.name,"\nCute cat says:")
# cat1 = CuteCat()
# print(cat1.name)
# cat1.speak()


def calculate_and_print(num,calcuator,formatter):
    result=calcuator(num)
    formatter(num,result)
def caluate_square(num):
    return num*num
def print_formatter(num,result):
    print(f"The number {num} is{result}")

calculate_and_print(5,caluate_square,print_formatter)