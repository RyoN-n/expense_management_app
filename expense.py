#%%
class Expense:
  def __init__(self, date, category, amount, method, note):
    self.date = date
    self.category = category
    self.amount = amount
    self.method = method
    self.note = note
    
  def to_dict(self):
    return {
      "date": self.date,
      "category": self.category,
      "amount": self.amount,
      "method": self.method,
      "note": self.note
    }



  