

class Account:
  def __init__(self,account_bal_path):
    self.filepath= account_bal_path
    with open(f'{account_bal_path}','r') as file:
     self.balance= int(file.read())
  
  def withdrawal(self,amount):
    self.balance= self.balance- amount
  def deposit(self,amount):
    self.balance= self.balance + amount   
  def commit_changes(self):
    with open(self.filepath,'w') as file:
      file.write(str(self.balance))


class Inheritance(Account):
  def __init__(self,account_bal_path):
    Account.__init__(self,account_bal_path)
  def Transfer(self,amount):
    self.balance= self.balance- amount  
  def drain(self):
    self.balance= self.balance-self.balance  

instantiate_object= Account(r'C:\Users\ekomobong\Documents\My Projects\Python\Python-sandboxes\Level-Up-basics\OOP\account.txt')  

second_obj= Inheritance(r'C:\Users\ekomobong\Documents\My Projects\Python\Python-sandboxes\Level-Up-basics\OOP\account.txt')

second_obj.deposit(2000)
second_obj.drain()
second_obj.deposit(200000)
second_obj.commit_changes()

