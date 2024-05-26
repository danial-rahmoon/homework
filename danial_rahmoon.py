#################  1 (A)
L1=["HTTP","HTTPS","FTP","DNS"]
L2=[80,443,21,53]
d = {}
for i in range(len(L1)):
    d[L1[i]] = L2[i]
print(d)
#Another solution
d1 = dict(zip(L1,L2))
print(d1)
################## 1 (B)
def factorial(num):
    if num == 0:
        return 1
    else:
        fact = 1
        for i in range(1, num + 1 ):
            fact = fact * i
        return fact

num = int(input("Enter the number: "))


if num < 0:
    print("factorial is not possible for negative numbers.")
else:
    print("Factorial factorial of the number:", num, "is", factorial(num))
######################### 1 (C)
L = ['Network', 'Bio', 'Programming', 'Physics', 'Music']

for item in L:

    if item.startswith('B'):

        print(item)
############################ 1 (D)
d1 = {}

for i in range (11):
    d1[i] = i+1
print(d1)
###################### 2
def binary_to_decimal(binary_num):
   
    if not set(binary_num).issubset('01'):
        return "This is not a valid binary number."
        
    else:
        decimal_num = int(binary_num, 2)
        return decimal_num

binary_num = input("Enter the binary number: ")

print("The equivalent decimal number is: ", binary_to_decimal(binary_num))

########################## 3
import json

with open('quiz.json', 'r',encoding='utf-8') as f:
    quiz = json.load(f)

score = 0

for question, answer in quiz.items():
    user_answer = input(question + " ")
    if user_answer.lower() == answer.lower():
        score += 1

print("لقد أجبت على", score, "أسئلة بشكل صحيح.")


user_name = input("أدخل اسمك: ")
results = {user_name: score}
with open('results.json', 'w') as f:
    json.dump(results, f)
################################ 4
class BankAccount:
    def __init__(self, number, holder):
        self.number = number
        self.holder = holder
        self._balance = 0.0

    def add(self, amount):
        self._balance += amount
        print(f"تم إضافة ${amount}. الرصيد الحالي هو ${self._balance}.")

    def remove(self, amount):
        if amount > self._balance:
            print("الرصيد غير كافي.")
        else:
            self._balance -= amount
            print(f"تم إزالة ${amount}. الرصيد الحالي هو ${self._balance}.")

    def current_balance(self):
        return self._balance


class SavingsAccount(BankAccount):
    def __init__(self, number, holder, rate):
        super().__init__(number, holder)
        self.rate = rate

    def interest(self):
        self._balance += self._balance * self.rate
        print(f"تم تطبيق الفائدة. الرصيد الحالي هو ${self._balance}.")

    def display(self):
        print(f"الرصيد الحالي هو ${self._balance} والمعدل هو {self.rate}.")


acc = BankAccount("000000", "jaffer")
acc.add(1000)
acc.remove(500)

savings_acc = SavingsAccount("002836", "danial" , 0.05)
savings_acc.interest()
savings_acc.display()
