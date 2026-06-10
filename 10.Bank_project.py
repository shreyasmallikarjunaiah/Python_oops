


class Bank:
    def __init__(self,Holder_name,Account_Number, ATM_pin, Balence,Withdrow):
        self.Holder_name = Holder_name
        self.Account_Number = Account_Number
        self.__ATM_pin = ATM_pin
        self.__Balence = Balence
        self.Withdrow = Withdrow



class Add_Money(Bank):
    @property
    def Credit(self):
        return self.__Balence

    @Credit.setter
    def Credit(self,add_money):
        if self.Holder_name=="Shreyas" and self.Account_Number==123456789:
            self.__Balence +=add_money
        else:
            print("Enter the correct credensitiols")


reason = input("Enter the reason: ")
if reason == "Credit":
    Add_Money.Credit=int(input("Enter the credit amount"))
else:
    print("Enter the correct reason")




add=Bank(input("Enter the name"),int(input("Enter the account  number")), 1234, 10000, 0)
add.Credit=int(input("Enter the credit amount"))
print(f"{add.Holder_name},{add.Account_Number},{add.Credit},{add.Withdrow}")