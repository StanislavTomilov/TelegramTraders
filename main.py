from pyrogram import Client

# Data for connection to Telegram account
phone_number = '+79896117700'
api_id = 655383
api_hash = '88db0805d24311ea0e8f05e2115aa1a2'

# Getting a connection to Telegram account
app = Client('my-session', phone_number = phone_number, api_id = api_id, api_hash = api_hash)

counter = 1
divider = 1

crypto_solyanka_dict = {
                        -384882468: -1001442805574,         #test
                        -1001442805574: -1001442805574, #TelegramTraders
                        940152572: -100142914981,       #crypto_solyanka_cryptoangel_bot
                        964236548: -1001471225365,      #crypto_solyanka_german_bot
                        725595486: -1001443655853,      #crypto_solyanka_rose_bot
                        969227740: -1001294788098,      #crypto_solyanka_cointrade_bot
                        725420715: -1001403623279,      #crypto_solyanka_james_bot
                        902178497: -1001341953633,      #crypto_solyanka_wcg_bot
                        954117019: -1001193842012,      #crypto_solyanka_artem_bot
                        854070442: -1001167690912,      #crypto_solyanka_pirate_bot
                        981862130: -1001457275719,      #crypto_solyanka_marginwhales_bot
                        909453054: -1001354472158,      #crypto_solyanka_asian_whales_bot
                        928204131: -1001341569964,      #crypto_solyanka_coincoach_bot
                        863139972: -1001233068606,      #crypto_solyanka_crypto_coach_bot
                        938258245: -1001412736228       #crypto_solyanka_palm_bot
                        }

crypto_solyanka_list = [key for key in crypto_solyanka_dict.keys()]
tt_list = [value for value in crypto_solyanka_dict.values()]


def tt_sender(message):
    global counter
    counter += 1
    if counter % divider == 0:
        message.forward(-1001442805574)


@app.on_message()
def start_app(t_client, message) -> None:
    if message.chat.id in crypto_solyanka_list:
        new_message = message.forward(chat_id=crypto_solyanka_dict[message.chat.id], as_copy=True)
        tt_sender(new_message)

app.run()