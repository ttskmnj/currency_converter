# currency_converter

## scripts
- `currency_converter_cli.py` - CLI application
- `currency_converter_api.py` - Web API application 
- `currency_converter.py` - library retrieve currency rate from Foreign exchange rates API published by the European Central Bank

## requirement
Web API use flask, so please install flask to run Web API.

## description
Applications support following currencies.

#### supported currencies
Iceland Krona, Canadian Dollar, Mexican Peso, Swiss Franc, 	Australian Dollar, Yuan Renminbin, Pound Sterling, Australian Dollar, Swedish Krona, Norwegian Krone, Turkish Lira, Rupiah, South African Rand, Croatia Kuna, Euro, Hong Kong Dollar, Israel Shekel, New Zealand Dollar, Malaysian Ringgit, Japan Yen, Czech Koruna, Singapore Dollar, Russia Ruble, Romania Leu, Hungary Forint, Bulgaria Lev, India Rupee, Korea Won, Denmark Krone, Thailand Baht, Philippines Peso, Poland Zloty, Brazil Real

you can use currency code to choose any of those currencies and you also can choose currency by currency symbols but some currencies use same symbol, so only symbols don't dupliacte with other currencies will be used.
But there are 2 exceptions $ and £. $ and £ are used as symbol of a lot currencies but one of the most common use for them are for United States Dollar and Pound Sterling. Therefore $ is used as symbol of United States Dollar and £ as Pound Sterling.

following currency codes and sybols are used in applications

#### currency codes
 ISK, CAD, MXN, CHF, AUD, CNY, GBP, USD, SEK, NOK, TRY, IDR, ZAR, HRK, EUR, HKD, ILS, NZD, MYR, JPY, CZK, SGD, RUB, RON, HUF, BGN, INR, KRW, DKK, THB, PHP, PLN, "BRL 
 #### currency symbols
 £, $, Rp, R, kn, €, ₪,RM, Kč, ₽, lei, Ft,лв, ₩, ฿, zł, R$
 
## how to use

### CLI
#### inputs
- `-i, --input_currency` - currency code/ symbol(required) 
- `-a, --amount` - numeric(required)
- `-o, --output_currency` - currency code/ symbol(optional)
##### example
```
$ python currency_converter_cli.py --input_currency USD --amount 100 --output_currency EUR
{
  "input": {
    "currency": "USD",
    "amount": 100.0
  },
  "output": {
    "EUR": 88.17
  }
}
```
```
$ python currency_converter_cli.py -i USD -a 100
{
  "input": {
    "currency": "USD",
    "amount": 100.0
  },
  "output": {
    "ISK": 11964.38, 
    "CAD": 131.86, 
    "MXN": 1915.9, 
    "CHF": 100.0, 
    "AUD": 139.69, 
    "CNY": 672.23, 
    "GBP": 76.66, 
    "USD": 100.0, 
    "SEK": 931.96, 
    "NOK": 858.18, 
    "TRY": 530.68, 
    "IDR": 1404000.18, 
    "ZAR": 1413.81, 
    "HRK": 653.63, 
    "EUR": 88.17, 
    "HKD": 784.92, 
    "ILS": 361.52, 
    "NZD": 145.59, 
    "MYR": 407.19, 
    "JPY": 11074.77, 
    "CZK": 2264.06, 
    "SGD": 135.13, 
    "RUB": 6575.33, 
    "RON": 419.39, 
    "HUF": 27978.31, 
    "BGN": 172.44, 
    "INR": 7115.46, 
    "KRW": 112279.14, 
    "DKK": 657.86, 
    "THB": 3109.5, 
    "PHP": 5202.17, 
    "PLN": 383.05, 
    "BRL": 370.47
  }
}
```
### Web API
flask set up
```
$ export FLASK_APP=currency_converter_api.py 
$ flask run
```
#### inputs
`http://127.0.0.1:5000/currency_converter/<input_currency>/<amount>/<output_currency>/`
- `input_currency` - currency code/ symbol(required) 
- `amount` - numeric(required)
- `output_currency` - currency code/ symbol(optional)
##### example
```
GET http://127.0.0.1:5000/currency_converter/EUR/100/USD/  HTTP/1.1
{
  "input":{
    "amount":100.0,
    "currency":"EUR"
  },
  "output":{
    "USD":113.42
  }
}
```

```
GET http://127.0.0.1:5000/currency_converter/EUR/100/  HTTP/1.1
{
  "input":{
    "amount":100.0,
    "currency":"EUR"
  },
  "output":{
    "AUD":158.44,
    "BGN":195.58,
    "BRL":420.19,
    "CAD":149.56,
    "CHF":113.42,
    "CNY":762.44,
    "CZK":2567.9,
    "DKK":746.14,
    "GBP":86.94,
    "HKD":890.26,
    "HRK":741.35,
    "HUF":31733.0,
    "IDR":1592417.0,
    "ILS":410.04,
    "INR":8070.35,
    "ISK":13570.0,
    "JPY":12561.0,
    "KRW":127347.0,
    "MXN":2173.01,
    "MYR":461.83,
    "NOK":973.35,
    "NZD":165.13,
    "PHP":5900.3,
    "PLN":434.45,
    "RON":475.67,
    "RUB":7457.74,
    "SEK":1057.03,
    "SGD":153.26,
    "THB":3526.8,
    "TRY":601.9,
    "USD":113.42,
    "ZAR":1603.54
  }
}