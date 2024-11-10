from flask import Flask

app = Flask(__name__)

# Token Data
TOTAL_SUPPLY = 8_912_766_789.71  # 10 billion total
CIRCULATING_SUPPLY = 8_912_766_789.71  # Circulating supply

# Total Supply Endpoint
@app.route('/total-supply', methods=['GET'])
def total_supply():
    return str(TOTAL_SUPPLY)

# Circulating Supply Endpoint
@app.route('/circulating-supply', methods=['GET'])
def circulating_supply():
    return str(CIRCULATING_SUPPLY)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
