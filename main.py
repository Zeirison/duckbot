from duckduckgo import *
import sys
import telepot
import time

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

answerer = telepot.helper.Answerer(bot)

if __name__ == '__main__':
    bot.message_loop({'inline_query': on_inline_query,
                      'chosen_inline_result': on_chosen_inline_result},
                     run_forever='Listening ...')

    while 1:
        time.sleep(10)
