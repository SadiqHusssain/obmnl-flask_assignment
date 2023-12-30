# Import libraries
from flask import Flask, request, url_for, redirect, render_template

# Instantiate Flask functionality
app = Flask('__name__')

# Sample data
# Sample data
transactions = [
    {'id': 1, 'date': '2023-06-01', 'amount': 100},
    {'id': 2, 'date': '2023-06-02', 'amount': -200},
    {'id': 3, 'date': '2023-06-03', 'amount': 300}
]

# Read operation
@app.route('/')
def get_transactions():
    try:
        return render_template('transactions.html', transactions=transactions)
    except NameError:
        return {"message": "transactions is not defined"}, 500


# Create operation
@app.route('/add', methods=['GET', 'POST'])
def add_transaction():
    if request.method == 'POST':
        transaction = {
            'id':len(transactions)+1,
            'date': request.form['date'],
            'amount':float(request.form['amount'])
            }

        transactions.append(transaction)
        return redirect(url_for('get_transactions'))
    else:
        return render_template('form.html')

# Update operation
@app.route('/update', methods=['POST'])
def update_trans(id):
    if request.method == 'POST':
        for transaction in transactions:
            if transaction['id'] == id:
                return render_template('edit.html'), transaction
        return redirect(url_for('read_trans'))
        
# Delete operation

# Update operation
@app.route('/delete', methods=['GET'])
def delete_trans(id):
    if request.method == 'POST':
        for transaction in transactions:
            if transaction['id'] == id:
                transactions.remmove(transaction)
                return redirect(url_for('read_trans'))

# Run the Flask app
if