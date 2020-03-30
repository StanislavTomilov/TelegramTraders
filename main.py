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
                "crypto_solyanka_german_bot": 964236548,
                "crypto_solyanka_rose_bot": 725595486,
                "crypto_solyanka_cointrade_bot": 969227740,
                "crypto_solyanka_james_bot": 725420715,
                "crypto_solyanka_wcg_bot": 902178497,
                "crypto_solyanka_artem_bot": 954117019,
                "crypto_solyanka_pirate_bot": 854070442,
                "crypto_solyanka_marginwhales_bot": 981862130,
                "crypto_solyanka_asian_whales_bot": 909453054,
                "crypto_solyanka_coincoach_bot": 928204131
                }
tt_chats_list ={
                "test": -384882468,
                "TelegramTraders": -1001442805574,
                "CryptoAngel": -100142914981,
                "German": -1001471225365,
                "Rose": -1001443655853,
                "CoinCoach": -1001341569964,
                "AsianWhales": -1001354472158,
                "MarginWhales": -1001457275719,
                "PirateVipClub": -1001167690912,
                "ArtemTrade": -1001193842012,
                "WSG": -1001341953633,
                "JamesRich": -1001403623279,
                "CoinTrade": -1001294788098
                }

counter = 1
divider = 5

def tt_sender(message):
    global counter
    counter += 1
    if counter % divider == 0:
        message.forward(tt_chats_list["TelegramTraders"])

@app.on_message()
def start_app(t_client, message) -> None:
    if message.chat.id == chat_id_list["test"]:
        new_message = message.forward(chat_id=tt_chats_list["TelegramTraders"], as_copy=True)
        tt_sender(new_message)
    elif message.chat.id == chat_id_list["crypto_solyanka_cryptoangel_bot"]:
        new_message = message.forward(chat_id = tt_chats_list["CryptoAngel"], as_copy = True)
        tt_sender(new_message)
    elif message.chat.id == chat_id_list["crypto_solyanka_german_bot"]:
        new_message = message.forward(chat_id = tt_chats_list["German"], as_copy = True)
        tt_sender(new_message)
    elif message.chat.id == chat_id_list["crypto_solyanka_rose_bot"]:
        new_message = message.forward(chat_id = tt_chats_list["Rose"], as_copy = True)
        tt_sender(new_message)
    elif message.chat.id == chat_id_list["crypto_solyanka_cointrade_bot"]:
        new_message = message.forward(chat_id = tt_chats_list["CoinTrade"], as_copy = True)
        tt_sender(new_message)
    elif message.chat.id == chat_id_list["crypto_solyanka_james_bot"]:
        new_message = message.forward(chat_id = tt_chats_list["JamesRich"], as_copy = True)
        tt_sender(new_message)
    elif message.chat.id == chat_id_list["crypto_solyanka_wcg_bot"]:
        new_message = message.forward(chat_id = tt_chats_list["WSG"], as_copy = True)
        tt_sender(new_message)
    elif message.chat.id == chat_id_list["crypto_solyanka_artem_bot"]:
        new_message = message.forward(chat_id = tt_chats_list["ArtemTrade"], as_copy = True)
        tt_sender(new_message)
    elif message.chat.id == chat_id_list["crypto_solyanka_pirate_bot"]:
        new_message = message.forward(chat_id = tt_chats_list["PirateVipClub"], as_copy = True)
        tt_sender(new_message)
    elif message.chat.id == chat_id_list["crypto_solyanka_marginwhales_bot"]:
        new_message = message.forward(chat_id = tt_chats_list["MarginWhales"], as_copy = True)
        tt_sender(new_message)
    elif message.chat.id == chat_id_list["crypto_solyanka_asian_whales_bot"]:
        new_message = message.forward(chat_id = tt_chats_list["AsianWhales"], as_copy = True)
        tt_sender(new_message)
    elif message.chat.id == chat_id_list["crypto_solyanka_coincoach_bot"]:
        new_message = message.forward(chat_id = tt_chats_list["CoinCoach"], as_copy = True)
        tt_sender(new_message)


app.run()