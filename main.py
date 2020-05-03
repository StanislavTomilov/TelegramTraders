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
                        -1001442805574: -1001442805574, #TelegramTraders                    #
                        940152572: -1001429149813,      #crypto_solyanka_cryptoangel_bot    #Crypto Angel
                        964236548: -1001471225365,      #crypto_solyanka_german_bot         #Герман на блокчейне
                        725595486: -1001443655853,      #crypto_solyanka_rose_bot           #Rose
                        969227740: -1001294788098,      #crypto_solyanka_cointrade_bot      #Coin Trade
                        725420715: -1001403623279,      #crypto_solyanka_james_bot          #James Rich
                        902178497: -1001341953633,      #crypto_solyanka_wcg_bot            #WCG
                        954117019: -1001193842012,      #crypto_solyanka_artem_bot          #Artem Trade
                        854070442: -1001167690912,      #crypto_solyanka_pirate_bot         #Pirate VIP Club 2.0
                        981862130: -1001457275719,      #crypto_solyanka_marginwhales_bot   #Margin Whales
                        909453054: -1001354472158,      #crypto_solyanka_asian_whales_bot   #Азиатские Киты
                        928204131: -1001341569964,      #crypto_solyanka_coincoach_bot      #Coin coach
                        863139972: -1001233068606,      #crypto_solyanka_crypto_coach_bot   #Trading Crypto Coach
                        938258245: -1001412736228,      #crypto_solyanka_palm_bot           #Palm Venice Beach
                        703814867: -1001445146705,      #crypto_solyanka_tca_bot            #TCA Exclusive                              -
                        1050648215: -1001406749095,     #crypto_solyanka102_bot             #Chaos Trade
                        1068800127: -1001320562354,     #cryptosolyanka_waveanalysis_bot    #Волновой анализ
                        817128313: -1001469264645,      #crypto_solyanka101_bot             #CryptoBull
                        986428578: -1001360819912       #crypto_solyanka_x100_bot           #x100. Богатейший Ди
                        }

telegram_trader_news_dict = {
                        -1001451038127: -1001264231743,  # Криптовалюта ICO
                        #-1001120865700: -1001264231743,  # Top Traders
                        -1001473033076: -1001264231743,  # Крипто тренды News
                        -1001147571806: -1001264231743,  # CRYPTO SEKTA
                        }

crypto_solyanka_list = [key for key in crypto_solyanka_dict.keys()]
tt_list = [value for value in crypto_solyanka_dict.values()]
telegram_trader_news_list = [key for key in telegram_trader_news_dict.keys()]


def tt_sender(message):
    global counter
    counter += 1
    if counter % divider == 0:
        message.forward(-1001442805574)


@app.on_message()
def start_app(t_client, message) -> None:
    if message.chat.id in crypto_solyanka_list:
        new_message = message.forward(chat_id = crypto_solyanka_dict[message.chat.id], as_copy = True)
        tt_sender(new_message)
    elif message.chat.id in telegram_trader_news_list:
        message.forward(chat_id = telegram_trader_news_dict[message.chat.id], as_copy = True)

app.run()