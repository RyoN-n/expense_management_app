import json
from expense import Expense

class ExpenseManager:
  def __init__(self, file_path = "expenses.json"):
    self.expenses = []
    try:
      with open(file_path) as f: ##インスタンス化して時点でjsonファイルのdataを読み込んでおく
        loaded = json.load(f)
        self.expenses = [Expense(**item) for item in loaded]
    except (FileNotFoundError, json.JSONDecodeError):
      pass

  def add_expense(self, expense):
    self.expenses.append(expense)

  def load_from_json(self, file_path):
    with open(file_path) as f:
      expense_json_load =json.load(f)
      return expense_json_load

  def save_to_json(self, path):
    data = [expense.to_dict() for expense in self.expenses]
    with open(path, 'w') as f:
      json.dump(data, f, ensure_ascii=False, indent=4)

  def get_total_by_category(self):
    totals = {}
    for expense in self.expenses:
      category = expense["category"]
      amount = expense["amount"]
      totals[category] = totals.get(category, 0) + amount
    return totals
  def get_monthly_summary(self):
    monthly_totals = {}
    for expense in self.expenses:
      date = expense["date"]
      amount = expense["amount"]
      month = date[:7]
      monthly_totals[month] = monthly_totals.get(month, 0) + amount
    return monthly_totals

#積み立て管理は未実装で良い