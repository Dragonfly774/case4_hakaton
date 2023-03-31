
import time

import openai

f = open('text.txt', 'w')

openai.api_key = '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'
messages = [
    {'role': 'system', 'content': 'ты составляешь датасет'},
]
message = 'составь датасет из 10 предложений, чтобы в каждом предложении в случайном порядке были: номер договора, ' \
          'имя и количество денег. Номера договоров должны быть от 1 до 6. Количество денег может быть как целым ' \
          'числом, так и дробным, например половина или четверть. Примеры предложений: "заплати в договор №1 на имя ' \
          'Семен Бакин 500 рублей", "оплати половину счета Романову Данилу в пятый договор", "по договору №2 оплати ' \
          'треть долга на имя Костя Синицын", "короче такая ситуация моему другу Малешеву Николаю нужно перевести 200 ' \
          'рублей в третий договор"'

if message:
    messages.append(
        {"role": "user", "content": message},
    )
    chat = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=messages
    )

reply = chat.choices[0].message.content
messages.append({"role": "assistant", "content": reply})
f.write(reply + '\n')
while True:
    message = 'еще 10 предложений'
    star_time = time.time()
    if message:
        messages.append(
            {"role": "user", "content": message},
        )
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )

    reply = chat.choices[0].message.content
    print(f" Время {time.time() - star_time}")
    print(f"ChatGPT: {reply}")
    f.write(reply + '\n')
    messages.append({"role": "assistant", "content": reply})