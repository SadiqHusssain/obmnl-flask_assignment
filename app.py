# Import libraries
from flask import Flask, request, url_for, redirect, render_template, make_response

# Instantiate Flask functionality
app = Flask('__name__')

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
@app.route('/edit/<int:transaction_id>', methods=['GET', 'POST'])
def edit_transaction(transaction_id):
    if request.method == 'POST':
        for transaction in transactions:
            if transaction['id'] == transaction_id:
                transaction['date'] = request.form['date']
                transaction['amount'] = float(request.form['amount'])
                break
        return redirect(url_for('get_transactions'))

    for transaction in transactions:
        if transaction['id'] == transaction_id:
            return render_template('edit.html', transaction=transaction)  
    
        
# Delete operation
@app.route('/delete/<int:transaction_id>')
def delete_transaction(transaction_id):
    for transaction in transactions:
        if transaction['id'] == transaction_id:
            transactions.remove(transaction)
            break

    return redirect(url_for('get_transactions'))

# Search functionality based on amount range
@app.route('/search', methods=['GET', 'POST'])
def search_transactions():
    filtered_transactions = []
    if request.method == 'POST':
        min = float(request.form['min_amount'])
        max = float(request.form['max_amount'])

        for transaction in transactions:
            if transaction['amount'] <= max and transaction['amount'] >= min:
                filtered_transactions.append(transaction)
                print(transaction)

        if filtered_transactions:
            return render_template('search_list.html', transactions=filtered_transactions)

        return render_template('search_list.html', message={"message":"No record in the specified range"})
    return render_template('search.html')

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
