import sys
from currency_converter import CurrencyConverter


cur = CurrencyConverter()
class Currency:
    """
    Описывает валюту с именем и курсом.
    """

    def __init__(self, name, rate):
        self.name = name
        self.rate = rate

class Wallet:

    """
        Описывает кошелек с валютой и суммой.
    """

    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def convert_to(self, new_currency):
        exchange_rate = new_currency.rate / self.currency.rate
        self.currency = new_currency
        self.amount *= exchange_rate

class Exchange:

    """
        Описывает обменник с методом обмена валюты.
    """

    def __init__(self):
        self.currencies = []

    def add_currency(self, currency):
        self.currencies.append(currency)

    def exchange_currency(self, wallet, new_currency):
        if new_currency in self.currencies:
            wallet.convert_to(new_currency)
        else:
            print("Данная валюта не поддерживается!")


class CurrencyExchange:
    """
        Описывает класс для конвертации валют.
    """

    def __init__(self,cur):
        self.cur = cur
        self.c = cur.currencies

    def exchange_usd_to_rub(self, amount):

        return amount * self.usd_rate

    def exchange_rub_to_usd(self, amount):

        return amount / self.rub_rate

    def exchange_usd_to_eur(self, amount):

        return amount * self.usd_rate

    def exchange_eur_to_usd(self, amount):

        return amount / self.eur_rate

    def exchange_usd_to_sek(self, amount):

        return amount * self.usd_rate

    def exchange_sek_to_usd(self, amount):

        return amount / self.byn_rate

    def exchange_usd_to_jpy(self, amount):

        return amount * self.usd_rate

    def exchange_jpy_to_usd(self, amount):

        return amount / self.jpy_rate


usd = Currency("USD", 1)


rub = Currency("RUB", 73)


eur = Currency("EUR", 0.85)


sek = Currency("SEK", 2.6)


jpy = Currency("JPY", 109)

wallet = Wallet(usd, 100000)

exchange = Exchange()

exchange.add_currency(usd)


exchange.add_currency(rub)


exchange.add_currency(eur)


exchange.add_currency(sek)


exchange.add_currency(jpy)


bank_number = input("Введите номер вашего счета ")

if bank_number == '20102006' :

    print('Добро пожаловать!')

else:
    print('Неправильный номер!')

    sys.exit()



print("Ваш баланс (USD):", wallet.amount)




print('Меню возможных действий:')


print("1. Обмен RUB на USD")

print("2. Обмен USD на EUR")

print("3. Обмен EUR на USD")

print("4. Обмен USD на SEK")

print("5. Обмен SEK на USD")

print("6. Обмен USD на JPY")

print("7. Обмен JPY на USD")


choice = input("Выберите операцию: ")

exchange = CurrencyExchange(cur)

if choice == '1':

    rub_amount = float(input("Введите сумму в RUB: "))

    usd_amount = cur.convert(rub_amount, 'RUB', 'USD')

    print(f"Вы получите {usd_amount} USD")

elif choice == '2':

    usd_amount = float(input("Введите сумму в USD: "))

    eur_amount = cur.convert(usd_amount, 'USD', 'EUR')

    print(f"Вы получите {eur_amount} EUR")


elif choice == '3':

    eur_amount = float(input("Введите сумму в EUR: "))

    usd_amount = cur.convert(eur_amount, 'EUR', 'USD')

    print(f"Вы получите {usd_amount} USD")

elif choice == '4':

        usd_amount = float(input("Введите сумму в USD: "))

        sek_amount = cur.convert(usd_amount, 'USD', 'SEK')

        print(f"Вы получите {sek_amount} SEK")

elif choice == '5':

    sek_amount = float(input("Введите сумму в SEK: "))

    usd_amount = cur.convert(sek_amount, 'SEK', 'USD')

    print(f"Вы получите {usd_amount} USD")

elif choice == '6':

    usd_amount = float(input("Введите сумму в USD: "))

    jpy_amount = cur.convert(usd_amount, 'USD', 'JPY')

    print(f"Вы получите {jpy_amount} JPY")

elif choice == '7':

    jpy_amount = float(input("Введите сумму в JPY: "))

    usd_amount = cur.convert(jpy_amount, 'JPY', 'USD')

    print(f"Вы получите {usd_amount} USD")


else:

    print("Неправильный выбор. Пожалуйста, выберите 1, 2, 3, 4, 5, 6 или 7")