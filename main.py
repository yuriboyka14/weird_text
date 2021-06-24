from encoder import Encoder
from tests import test1, test2, test3


print("This is the ENCODER program!\n")
print("Options: \n1. Random test1 \n2. Random test1 \n3. Random test3 \n4. Custom test \n")

x = input("Choose your option (enter the number): ")

if x == '1':
    test1()
elif x == '2':
    test2()
elif x == '3':
    test3()
elif x == '4':
    y = input("Write the sentence to encode: ")
    Encoder(y)
else:
    print("Invalid input. Program stopped.")













