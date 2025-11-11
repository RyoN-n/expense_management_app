#%%
from datetime import datetime
class Expense:
  def __init__(self, date, category, amount, method, note):
    self.date = date #支出登録日
    self.category = category
    self.amount = amount
    self.method = method
    self.note = note
    self.settlement_day = 4 #カードの引き落とし日
    self.closing_day = 10 #カードの締め日
    self.settlement_date = self.calculate_settlement_date()
    
  def calculate_settlement_date(self):
    if self.method.lower() == "card":
      original_date = datetime.strptime(self.date, "%Y-%m-%d")

      #締め日を基準に翌月または翌々月を計算
      if original_date.day <= self.closing_day:
        next_year, next_month = divmod(original_date.month, 12)
        next_month += 1
      else:
        next_year, next_month = divmod(original_date.month +1, 12)
        next_month += 1

      #年の調整
      next_year += original_date.year

      #引き落とし日を設定
      settlement_date = datetime(next_year, next_month, self.settlement_day)
      return settlement_date.strftime("%Y-%m-%d")
    
    #現金払いの場合は何もしない
    return self.date 

  def to_dict(self):
    return {
      "date": self.date,
      "category": self.category,
      "amount": self.amount,
      "method": self.method,
      "note": self.note
    }



  