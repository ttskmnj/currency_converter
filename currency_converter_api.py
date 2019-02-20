from flask import Flask, jsonify
from currency_converter import CurrencyConverter

app = Flask(__name__)


@app.route('/currency_converter/<input_currency>/<amount>/')
@app.route('/currency_converter/<input_currency>/<amount>/<output_currency>/')
def index(input_currency, amount, output_currency=None):
    error_msg = {}

    ########################
    # input currency check #
    ########################
    # check if input currency is in currency list
    if input_currency not in CurrencyConverter.currency_code\
            and input_currency not in CurrencyConverter.currency_symbol:
        error_msg['input_currency'] = "please choose input currency from this list {}"\
                     .format(CurrencyConverter.currency_code)

    ################
    # amount check #
    ################
    # check if amount is float
    if not amount.replace('.', '', 1).isdigit():
        error_msg['amount'] = "amount should be float {}{}".format(amount.isdigit(), amount)
    else:
        amount = float(amount)

    #########################
    # output currency check #
    #########################
    # check if output currency is in currency list
    if output_currency and output_currency not in CurrencyConverter.currency_code\
            and output_currency not in CurrencyConverter.currency_symbol:
        error_msg['output_currency'] = "please choose output currency from this list {}"\
                     .format(CurrencyConverter.currency_code)

    # return error message if input is invalid
    if len(error_msg) > 0:
        return jsonify({'Error': error_msg})

    else:
        # get currency rate
        rates = CurrencyConverter.get_rates(input_currency, output_currency)

        # generate output dictionary
        results = CurrencyConverter.generate_results(amount, rates)

        # output result in json
        return jsonify(results)
