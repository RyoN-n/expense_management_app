import matplotlib.pyplot as plt
from manager import ExpenseManager
import numpy as np

class Visualizer:
  def __init__(self, expense_manager):
    """
    expense_manager: ExpenseManagerのインスタンス
    → そこから支出データ（月別・カテゴリ別など）を取得する
    """
    self.expense_manager = expense_manager
    

  def plot_expense_pie(self):
    """
    カテゴリ別支出の円グラフを描画する。
    必要なデータ: self.manager.get_total_by_category()
    """
    data = self.expense_manager.get_total_by_category()
    categories = list(data.keys())
    amounts = list(data.values())
    total = sum(amounts)

    plt.figure()
    plt.pie(amounts, labels = categories, autopct='%1.1f%%', startangle = 140)
    plt.title('Percentage of Expenses by Category')
    plt.axis('equal')

    #合計金額を右上に表示
    plt.text(1.2,1.5, f"Total amounts: ¥{total}", fontsize = 12, ha='right')
    plt.tight_layout()
    #plt.show()
    plt.savefig("figure/category_expense.png")
    plt.close()

  def plot_monthly_bar(self):
    """
    月別支出の棒グラフを描画する。
    必要なデータ: self.manager.get_monthly_summary()
    """
    # ここにmatplotlibコードを書く
    data = self.expense_manager.get_monthly_summary()
    sorted_items = sorted(data.items())

    dates = list(item[0] for item in sorted_items)
    amounts = list(item[1] for item in sorted_items)

    plt.figure(figsize=(10, 5))
    left = np.arange(len(dates))
    plt.bar(left, amounts, width=0.8, tick_label= dates)
    plt.title('Monthly Expenses')
    plt.xlabel('Month')
    plt.ylabel('Total Amount')
    plt.xticks(rotation = 45)
    plt.tight_layout()
    #plt.show()

    #画像を保存
    plt.savefig("figure/monthly_expense.png")
    plt.close() #メモリ解放
  # def plot_saving_lines(saving_data):
  #   pass