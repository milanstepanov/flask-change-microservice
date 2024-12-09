"""Change application.
"""

from flask import Flask
from flask import jsonify

app = Flask(__name__)


def change(amount):
    """Converts an amount provided in dollars to the change in quarters, dims, nickels
    and pennies"""
    # calculate the resultant change and store the result (res)
    res = []
    coins = [1, 5, 10, 25]  # value of pennies, nickels, dims, quarters
    coin_lookup = {25: "quarters", 10: "dims", 5: "nickels", 1: "pennies"}

    # divide the amount*100 (the amount in cents) by a coin value
    # record the number of coins that evenly divide and the remainder

    coin = coins.pop()
    num, rem = divmod(int(amount * 100), coin)
    # append the coin type and number of coins that had no remainder
    res.append({num: coin_lookup[coin]})

    # while there is still some remainder, continue adding coins to the result
    while rem > 0:
        coin = coins.pop()
        num, rem = divmod(rem, coin)
        if num:
            if coin in coin_lookup:
                res.append({num: coin_lookup[coin]})

    return res


@app.route("/")
def hello():
    """Return a friendly HTTP freeting."""
    print("I am inside hello world")
    return "Hello World! I can make change at route: /change"


@app.route("/change/<dollar>/<cents>")
def changeroute(dollar, cents):
    """Define URL to trigger change functionality."""
    print(f"Make change for {dollar}.{cents}")
    # amount not computed correctly. 1 cent must be provided as '01' !
    amount = f"{dollar}.{cents}"
    result = change(float(amount))
    return jsonify(result)


@app.route("/change/100/<dollar>/<cents>")
def change100route(dollar, cents):
    """Define URL to trigger scaled change functionality. The input change is
    multiplied by 100."""
    amount = float(f"{dollar}.{cents}") * 100
    print(f"This is the {change} x 100")

    result = change(amount)
    return jsonify(result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
