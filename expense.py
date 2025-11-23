#%%
from datetime import datetime
class Expense:
  #カードのルールを集中管理
  CARD_RULES = {
    "card": {"closing_day": 10, "settlement_day": 4},
    "card2": {"closing_day": 30, "settlement_day": 27}
  }
  def __init__(self, date, category=None, amount=0, method=None, note=None,settlement_date = None, **kwargs):
    self.date = date #支出登録日
    self.category = category
    self.amount = amount
    self.method = method
    #正規化：既存dataの"card"を規定カード"card1"に変換する
    # method_key = (method or "").strip().lower()
    # if method_key == "card":
    #   method_key = "card1"
    # self.method = method_key
    self.note = note

    self.settlement_day = None
    self.closing_day = None

    #methodを参照して、それがCARD＿RULESにあればそれをキーとして指定して、そのvaluesを取ってくるようにする
    rules = self.CARD_RULES.get(self.method) #methodがCARD_RULESのkeyに存在すればそのvaluesを返す
    if rules:
      self.closing_day = rules["closing_day"]
      self.settlement_day = rules["settlement_day"]

    self.settlement_date = self.calculate_settlement_date()
    
  def calculate_settlement_date(self):
    if self.method and self.method in self.CARD_RULES:
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
      "note": self.note,
      "settlement_date": self.settlement_date,
    }



  