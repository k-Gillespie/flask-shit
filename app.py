from flask import Flask, jsonify
import random
import json

app = Flask(__name__)

# Read quotes from the JSON file
with open('quotes.json', 'r') as file:
    quotes = json.load(file)

@app.route('/random-quote', methods=['GET'])
def get_random_quote():
    # Randomly pick a quote from the list
    random_quote = random.choice(quotes)
    
    # Return the randomly picked quote as JSON
    return jsonify(random_quote)

if __name__ == '__main__':
    app.run(debug=True)
