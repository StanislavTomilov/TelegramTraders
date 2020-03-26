from pyrogram import Client

# Data for connection to Telegram account
phone_number = '+79896117700'
api_id = 655383
api_hash = '88db0805d24311ea0e8f05e2115aa1a2'

# Getting a connection to Telegram account
app = Client('my-session', phone_number = phone_number, api_id = api_id, api_hash = api_hash)

"""
Title : Telegram Traders 
Chat ID : -1001442805574

Chanel list:
First Name : CryptoAngel | @crypto_solyanka Chat ID : 940152572 User Name = crypto_solyanka_cryptoangel_bot
First Name : CoinTrade | @crypto_solyanka Chat ID : 969227740 User Name = crypto_solyanka_cointrade_bot
First Name : Герман на блокчейне | @crypto_solyanka Chat ID : 964236548 User Name = crypto_solyanka_german_bot
First Name : Rose | @crypto_solyanka Chat ID : 725595486 User Name = crypto_solyanka_rose_bot
First Name : Азиатские киты | @crypto_solyanka Chat ID : 909453054 User Name = crypto_solyanka_asian_whales_bot
First Name : Coin Coach Signals | @crypto_solyanka Chat ID : 928204131 User Name = crypto_solyanka_coincoach_bot
First Name : James Rich | @crypto_solyanka Chat ID : 725420715 User Name = crypto_solyanka_james_bot
First Name : WCG | @crypto_solyanka Chat ID : 902178497 User Name = crypto_solyanka_wcg_bot
First Name : Artem Trade | @crypto_solyanka Chat ID : 954117019 User Name = crypto_solyanka_artem_bot
First Name : Pirate VIP Club 2.0 | @crypto_solyanka Chat ID : 854070442 User Name = crypto_solyanka_pirate_bot
First Name : Margin Whales | @crypto_solyanka Chat ID : 981862130 User Name = crypto_solyanka_marginwhales_bot
"""

chat_id_list = {
                "test": -384882468,
                "crypto_solyanka_cryptoangel_bot": 940152572,
                "crypto_solyanka_cointrade_bot": 969227740,
                "crypto_solyanka_german_bot": 964236548,
                "crypto_solyanka_rose_bot": 725595486,
                "crypto_solyanka_asian_whales_bot": 909453054,
                "crypto_solyanka_coincoach_bot": 928204131,
                "crypto_solyanka_james_bot": 725420715,
                "crypto_solyanka_wcg_bot": 902178497,
                "crypto_solyanka_artem_bot": 954117019,
                "crypto_solyanka_pirate_bot": 854070442,
                "crypto_solyanka_marginwhales_bot": 981862130
                }

@app.on_message()
def start_app(t_client, message) -> None:
    for key in chat_id_list:
        if message.chat.id == chat_id_list[key]:
            t_client.send_message(-1001442805574, message.chat.title)
            t_client.send_message(-1001442805574, message.photo)
            t_client.send_message(-1001442805574, message.text)

app.run()