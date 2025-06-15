import matplotlib.pyplot as plt
from manager import ExpenseManager

class Visualizer:
  def __init__(self, expense_manager):
    """
    expense_manager: ExpenseManagerのインスタンス
    → そこから支出データ（月別・カテゴリ別など）を取得する
    """
    self.manager = expense_manager
    

  def plot_expense_pie(self):
    """
    カテゴリ別支出の円グラフを描画する。
    必要なデータ: self.manager.get_total_by_category()
    """
    pass  # ここにmatplotlibコードを書く

  def plot_monthly_bar(self):
    """
    月別支出の棒グラフを描画する。
    必要なデータ: self.manager.get_monthly_summary()
    """
    pass  # ここにmatplotlibコードを書く

  # def plot_saving_lines(saving_data):
  #   pass