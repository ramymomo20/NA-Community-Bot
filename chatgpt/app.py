import os
from dotenv import load_dotenv
import openai
from chronological import *

load_dotenv()
openai.api_key = os.environ.get('OPENAI_KEY')
completion = openai.ChatCompletion()

def askgpt(question, chat_log=None):
    if chat_log is None:
        chat_log = [{
            'role': 'system',
            'content': 'Provide a random positive or negative or neutral 1-line answer and use some parts of the prompt to respond. You can use sly insults if you wish. Do not state that you are an AI.',
        }]
    chat_log.append({'role': 'user', 'content': question})
    response = completion.create(model='gpt-3.5-turbo', messages=chat_log)
    answer = response['choices'][0]['message']['content']
    chat_log.append({'role': 'assistant', 'content': answer})
    return answer