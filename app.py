from manager import ExpenseManager
from expense import Expense

print("Welcome to the expense management app!")
print("Select the mode form below.")
mode  = input("1. Resister expense/incomes\n\
      2. View expense namagement data\n\
      3. View saving plan chart\n")

expenses = ExpenseManager() ##インスタンス化した時点でjsonファイルのdataが読み込まれている

if (int(mode) == 1):
  date = input("input today's date (YYYY-MM-DD):")
  category = input("input category of the expense (food, hobby, loan):")
  amount = input("input the amount of the expense:")
  method = input("input the method of the pay (cash/card)")
  note = input("write sthg about the expense:")
  daily_expense = Expense(date, category, amount, method, note)  ##Expenseクラスをインスタンス化して支出データを格納
  expenses.add_expense(daily_expense) ##一日分の支出を支出全体を管理するリストに追加
  expenses.save_to_json("expenses.json") ##支出データを辞書式に変更してjsonファイルに書き込み
  print("saved the expense data successfully!")

if(int(mode) == 2):
  print("2")

if (int(mode)==3):
  print("3")
