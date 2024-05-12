from telethon.sync import TelegramClient
import csv
from datetime import datetime
import itertools

api_id = ###
api_hash = ###

# Initialize the iterator for 'i'
counter = itertools.count()
i = next(counter)

# chat_ids = [-1001351403315, -1001288386840, -1001402872747, -1001262083272, -1001170819000, -1001406219671, -1001181553151, -1001163856087, 
#-1001131697343, -1001316735879, -1001165552538, -1001507022465, -1001550995706, -1001204383992, -1001737348964, -1001203122852, 
#-1001142484860, -1001646734746, -1001433922609, -1001909568119, -1001480367444, -1001293837955, -1001486436859]

with TelegramClient('session_name', api_id, api_hash) as client:
    chat_id = -1001402872747
    search_keywords = ["сарказм", "sarcasm", 'сарк', "sarc"]

    with open('udarov.csv', 'a', encoding="utf-8", newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['ConvThread', 'MessageID', 'Date', 'Message', 'UserID'])

        for search_keyword in search_keywords:
            # Reset the i for each keyword
            for x in client.iter_messages(chat_id, search=search_keyword):
                try:
                    if x.reply_to:
                        x2 = x.get_reply_message()
                        if x2.reply_to:
                            y = x2.get_reply_message()
                            for obj in [
                                [i, y.id, y.date.strftime("%Y-%m-%d"), y.message, y.from_id.user_id],
                                [i, x2.id, x2.date.strftime("%Y-%m-%d"), x2.message, x2.from_id.user_id],
                                [i, x.id, x.date.strftime("%Y-%m-%d"), x.message, x.from_id.user_id]]:
                                writer.writerow(obj)
                            i = next(counter)
                        else:
                            for obj in [
                                [i, x2.id, x2.date.strftime("%Y-%m-%d"), x2.message, x2.from_id.user_id],
                                [i, x.id, x.date.strftime("%Y-%m-%d"), x.message, x.from_id.user_id]]:
                                writer.writerow(obj)
                            i = next(counter)
                    else:
                        writer.writerow([i, x.id, x.date.strftime("%Y-%m-%d"), x.message, x.from_id.user_id])
                        i = next(counter)
                except:
                    try: 
                        if x:
                            writer.writerow([i, x.id, x.date.strftime("%Y-%m-%d"), x.message, x.from_id.user_id])
                            i = next(counter)
                    except:
                        print(f"Error processing message")
client.disconnect()


