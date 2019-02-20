import json
from argparse import ArgumentParser
from currency_converter import CurrencyConverter


if __name__ == "__main__":
    # initialize local variables
    input_currency, amount, output_currency = None, None, None
    error_msg = ""

    parser = ArgumentParser()
    parser.add_argument("-i", "--input_currency")
    parser.add_argument("-a", "--amount")
    parser.add_argument("-o", "--output_currency")
    args = parser.parse_args()

    #######################################
    # validation check for input currency #
    #######################################
    # check if input currency is set
    if not args.input_currency:
        error_msg += "\n--input_currency: please choose input currency"
    # check if input currency is in currency list
    elif args.input_currency not in CurrencyConverter.currency_code\
            and args.input_currency not in CurrencyConverter.currency_symbol:
        error_msg += "\n--input_currency: please choose input currency from this list {}"\
            .format(CurrencyConverter.currency_code)
    else:
        # convert input currency to code if input currency is symbol
        input_currency = CurrencyConverter.currency_symbol[args.input_currency]\
            if args.input_currency in CurrencyConverter.currency_symbol else args.input_currency

    ###############################
    # validation check for amount #
    ###############################
    # check if amount is set
    if not args.amount:
        error_msg += "\n--amount: please choose amount"
    # check if amount is float
    elif not args.amount.replace('.', '', 1).isdigit():
        error_msg += "\n--amount: amount should be float"
    else:
        amount = float(args.amount)

    ########################################
    # validation check for output currency #
    ########################################
    # check if output currency is in currency list
    if args.output_currency and args.output_currency not in CurrencyConverter.currency_code\
            and args.output_currency not in CurrencyConverter.currency_symbol:
        error_msg += "\n--output_currency: please choose output currency from this list {}"\
            .format(CurrencyConverter.currency_code)
    else:
        # convert output currency to code if output currency is symbol
        output_currency = CurrencyConverter.currency_symbol[args.output_currency]\
            if args.output_currency in CurrencyConverter.currency_symbol else args.output_currency

    ######################################
    # interrupt if there is invalid input #
    ######################################
    if error_msg is not "":
        parser.error(error_msg)

    # get currency rate
    rates = CurrencyConverter.get_rates(input_currency, output_currency)

    # generate output dictionary
    generated_results = CurrencyConverter.generate_results(amount, rates)

    # output result in json
    print(json.dumps(generated_results))
