from duckduckgo import *
import group_utilities
import sys
import telepot
import time
from random import randrange

stfu_phrases = group_utilities.read_lines('stfu_phrases.txt')

bot = telepot.Bot(sys.argv[1])

from telepot.namedtuple import InlineQueryResultArticle, InputTextMessageContent

def on_inline_query(msg):
    def compute():
        query_id, from_id, query_string = telepot.glance(msg, flavor='inline_query')
        print('Inline Query:', query_id, from_id, query_string)
        response = get_zci(query_string)
        articles = [InlineQueryResultArticle(
                        id='abc',
                        title=response,
                        input_message_content=InputTextMessageContent(
                            message_text="Result for '{}':\n".format(query_string) + get_zci(query_string)
                        )
                   )]

        return articles

    answerer.answer(msg, compute)

def on_chosen_inline_result(msg):
    result_id, from_id, query_string = telepot.glance(msg, flavor='chosen_inline_result')
    print ('Chosen Inline Result:', result_id, from_id, query_string)

def on_chat(msg):
    # Handle 'shutthefuckup' command
    if msg['entities'][0]['type'] == 'bot_command':
        if msg['text'] == '/shutthefuckup@duckans_bot':
            bot.sendMessage(msg['chat']['id'], stfu_phrases[randrange(len(stfu_phrases))])


answerer = telepot.helper.Answerer(bot)

bot.message_loop({'inline_query': on_inline_query,
                  'chosen_inline_result': on_chosen_inline_result,
                  'chat': on_chat},
                 run_forever='Listening ...')

while 1:
    time.sleep(10)
