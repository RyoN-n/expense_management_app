# %%
from manager import ExpenseManager
from expense import Expense
from visualizer import Visualizer
from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime, timedelta

app = Flask(__name__)
manager = ExpenseManager()

@app.route('/input', methods = ["GET", "POST"])
def input_expense():
  if request.method == "POST":
    date = request.form['date']
    category = request.form['category']
    amount = int(request.form['amount'])
    method = request.form.get('method', '')
    note = request.form.get('note', '')

    new_expense = Expense(date, category, amount, method, note)
    manager.add_expense(new_expense)
    manager.save_to_json("expenses.json")

    return redirect('/')
  return render_template('input.html')


@app.route('/', methods = ['GET', 'POST'])
def index():
  selected_month = request.form.get('month') 
  raw_months = sorted(
    set(
      (getattr(exp, "settlement_date", exp.date)[:7])
      for exp in manager.expenses
    )
  )

  #月選択用表示ラベルの作成（YYYY年MM月）
  months = []
  for m in raw_months:
    start_date = datetime.strptime(m, "%Y-%m") - timedelta(days = 1)
    start_date = start_date.replace(day = 25)
    end_date = datetime.strptime(m, "%Y-%m") + timedelta(days = 24)
    months.append({
      'value': m,
      'label': f"{int(m[:4])}年{int(m[5:7])}月",
      'start_date': start_date.strftime("%m月%d日"),
      'end_date': end_date.strftime("%m月%d日")
    })
    
  chart_path = None
  bar_chart_path = None
  viz = Visualizer(manager)
  #月別棒グラフ作成
  bar_chart_path = viz.plot_monthly_bar_chart()
  
  #選択月があれば円グラフを作成
  if selected_month:
    # 前月25日から当月25日までの範囲を計算
    start_date = datetime.strptime(selected_month, "%Y-%m") - timedelta(days=1)
    start_date = start_date.replace(day =25)
    end_date = datetime.strptime(selected_month, "%Y-%m") + timedelta(days=24)

    # グラフ生成時に範囲を渡す
    chart_path = viz.plot_category_pie_chart_for_month(start_date, end_date)
    #YYYY-MM形式をYYYY年MM月の表示ラベルに変換
    selected_month_label = datetime.strptime(selected_month, "%Y-%m").strftime("%Y年%m月")
    
  else:
    selected_month_label = None

  return render_template('index.html',
                          months = months,
                          selected_month = selected_month,
                          selected_month_label = selected_month_label,
                          chart_path = chart_path,
                          bar_chart_path = bar_chart_path)
if __name__ == '__main__':
  app.run(debug=True)

