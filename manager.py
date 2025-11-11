import json
from expense import Expense

class ExpenseManager:
  SETTLEMENT_DAY = 25 #給料日

  def __init__(self, file_path = "expenses.json"):
    self.expenses = []
    try:
      with open(file_path, encoding='utf-8') as f: ##インスタンス化して時点でjsonファイルのdataを読み込んでおく
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
    with open(path, 'w', encoding = 'utf-8') as f:
      json.dump(data, f, ensure_ascii=False, indent=4)

  def get_total_by_category(self):
    totals = {}
    for expense in self.expenses:
      category = expense.category
      amount = expense.amount
      totals[category] = totals.get(category, 0) + amount
    return totals
  def get_monthly_summary(self):
    monthly_totals = {}
    for expense in self.expenses:
      date = expense.settlement_date
      year, month, day = map(int, date.split('-'))

      if day > self.SETTLEMENT_DAY:
        month = (month % 12) + 1 
        year += (month == 1)
        settlement_month = f"{year}-{month:02d}"
      else:
        settlement_month = f"{year}-{month:02d}"

      amount = expense.amount
      monthly_totals[settlement_month] = monthly_totals.get(settlement_month, 0) + amount
    return monthly_totals

#積み立て管理は未実装で良い