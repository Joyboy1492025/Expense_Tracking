from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///expenses.db'
db = SQLAlchemy(app)

CURRENCIES = {
    'USD': '$',
    'EUR': '€',
    'GBP': '£',
    'JPY': '¥',
    'INR': '₹',
    'AUD': 'A$',
    'CAD': 'C$',
    'CHF': 'CHF',
    'CNY': '¥',
    'SEK': 'kr',
    'NZD': 'NZ$',
    'SGD': 'S$',
    'HKD': 'HK$',
    'MXN': '$',
    'BRL': 'R$',
    'ZAR': 'R'
}

class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(50), nullable=False)
    currency = db.Column(db.String(3), nullable=False, default='USD')
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

with app.app_context():
    db.create_all()
    result = db.session.execute(text("PRAGMA table_info(expense)"))
    existing_columns = [row[1] for row in result.fetchall()]
    if 'currency' not in existing_columns:
        db.session.execute(text("ALTER TABLE expense ADD COLUMN currency VARCHAR(3) NOT NULL DEFAULT 'USD'"))
        db.session.commit()

@app.route('/')
def index():
    selected_currency = request.args.get('currency', 'USD').upper()
    if selected_currency not in CURRENCIES:
        selected_currency = 'USD'

    expenses = Expense.query.order_by(Expense.date_added.desc()).all()
    # Calculate totals per category
    stats = {}
    total = 0
    for e in expenses:
        stats[e.category] = stats.get(e.category, 0) + e.amount
        total += e.amount

    return render_template(
        'index.html',
        expenses=expenses,
        stats=stats,
        total=total,
        currency=selected_currency,
        symbol=CURRENCIES[selected_currency],
        currencies=CURRENCIES
    )

@app.route('/add', methods=['POST'])
def add():
    selected_currency = request.form.get('currency', 'USD').upper()
    if selected_currency not in CURRENCIES:
        selected_currency = 'USD'

    new_expense = Expense(
        title=request.form.get('title'),
        amount=float(request.form.get('amount')),
        category=request.form.get('category'),
        currency=selected_currency
    )
    db.session.add(new_expense)
    db.session.commit()
    return redirect(f'/?currency={selected_currency}')

@app.route('/delete/<int:id>')
def delete(id):
    selected_currency = request.args.get('currency', 'USD').upper()
    if selected_currency not in CURRENCIES:
        selected_currency = 'USD'

    expense = Expense.query.get(id)
    db.session.delete(expense)
    db.session.commit()
    return redirect(f'/?currency={selected_currency}')

if __name__ == '__main__':
    app.run(debug=True)