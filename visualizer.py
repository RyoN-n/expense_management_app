import matplotlib
matplotlib.use('Agg')  # 画像出力専用バックエンドに変更
import matplotlib.pyplot as plt
from manager import ExpenseManager
import numpy as np
import os
from datetime import datetime

class Visualizer:
  def __init__(self, expense_manager):
    """
    expense_manager: ExpenseManagerのインスタンス
    → そこから支出データ（月別・カテゴリ別など）を取得する
    """
    self.expense_manager = expense_manager
    

  def plot_category_pie_chart_for_month(self, start_date, end_date, output_dir='static/charts'):
    data = {}
    for expense in self.expense_manager.expenses:
        expense_date = datetime.strptime(expense.date, "%Y-%m-%d")
        if start_date <= expense_date <= end_date:
            data[expense.category] = data.get(expense.category, 0) + expense.amount

    if not data:
        return None

    os.makedirs(output_dir, exist_ok=True)
    filename = f'category_{start_date.strftime("%Y-%m")}_to_{end_date.strftime("%Y-%m")}.png'
    output_path = os.path.join(output_dir, filename)

    def make_autopct(values):
        def my_autopct(pct):
            total = sum(values)
            val = int(round(pct * total / 100.0))
            return f"¥{val:,}"
        return my_autopct

    plt.figure(figsize=(6, 6))
    # ラベル順を安定させ、開始角度を「上（北）」に固定して時計回りに描画
    items = sorted(data.items(), key=lambda x: x[0])  # カテゴリ名でソート（必要に応じ変更可）
    labels = [k for k, _ in items]
    values = [v for _, v in items]
    plt.pie(values, labels=labels, autopct=make_autopct(values), startangle=90, counterclock=False)
    plt.title('Expenses by Category (Amount)')
    plt.axis('equal')
    plt.savefig(output_path)
    plt.close()
    return f'charts/{filename}'
  

    """
    カテゴリ別支出の円グラフを描画する。
    必要なデータ: self.manager.get_total_by_category()
    """
  #   data = self.expense_manager.get_total_by_category()
  #   categories = list(data.keys())
  #   amounts = list(data.values())
  #   total = sum(amounts)

  #   plt.figure()
  #   plt.pie(amounts, labels = categories, autopct='%1.1f%%', startangle = 140)
  #   plt.title('Percentage of Expenses by Category')
  #   plt.axis('equal')

  #   #合計金額を右上に表示
  #   plt.text(1.2,1.5, f"Total amounts: ¥{total}", fontsize = 12, ha='right')
  #   plt.tight_layout()
  #   #plt.show()
  #   plt.savefig("figure/category_expense.png")
  #   plt.close()

  def plot_monthly_bar_chart(self, output_dir='static/charts'):
    """
    月別支出の棒グラフを描画する。
    必要なデータ: self.expense_manager.get_monthly_summary()
    """
    # 月別支出データを取得（支払日を考慮済み）
    data = self.expense_manager.get_monthly_summary()
    if not data:
        return None

    # データをソートして月と金額を取得
    sorted_items = sorted(data.items())
    months = [datetime.strptime(m, "%Y-%m").strftime("%Y/%m") for m, _ in sorted_items]
    amounts = [amount for _, amount in sorted_items]

    # グラフの保存先を作成
    os.makedirs(output_dir, exist_ok=True)
    filename = 'monthly_bar_chart.png'
    output_path = os.path.join(output_dir, filename)

    # 棒グラフを描画
    plt.figure(figsize=(8, 5))
    left = np.arange(len(months))
    plt.bar(left, amounts, width=0.6, tick_label=months)
    plt.title('Monthly Expenses (Including Credit Card Payments)')
    plt.xlabel('Month')
    plt.ylabel('Total Amount')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()

    return f'charts/{filename}'
    #plt.show()

  #   #画像を保存
  #   plt.savefig("figure/monthly_expense.png")
  #   plt.close() #メモリ解放
  # # def plot_saving_lines(saving_data):
  # #   pass

