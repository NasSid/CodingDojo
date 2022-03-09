class User: 
    def __init__ (self,data):
        self.name = data["name"]
        self.balance = data["balance"]


    def user_balance(self):
        print(f"[{self.name}'s balance is {self.balance}]")
        return self

    def make_withdrawal(self, amount):
        print (f"[{self.name} makes a deposit of {amount}]")
        self.balance = self.balance - amount
        return self

    def transfer_money (self, other_user, amount):
        print(f"[{self.name} makes a transfer of {amount} to {other_user.name}]")
        self.balance -= amount
        other_user.balance += amount
        return self

nasir_data = {
    "name" : "Nasir",
    "balance": 100
}
mustafa_data = {
    "name": "Mustafa",
    "balance": 100
}
nasir = User(nasir_data)
mustafa = User(mustafa_data)

nasir.user_balance().make_withdrawal(25).user_balance().transfer_money(mustafa, 25).user_balance()
mustafa.user_balance()