
import os
from openai import OpenAI
from dotenv import load_dotenv

# load .env (API KEY)
load_dotenv()
client = OpenAI()

#Examples of messages being built with two parts: Role & Tasks
#---
#messages = [{"role": "system", "content": "You are a poet"}]
#messages.append({"role": "user", "content": "Get the sum of 5 and 5^2"})
#---
#messages = [{"role": "system", "content": "You are a mathematician"}]
#messages.append({"role": "user", "content": "Get the sum of 5 and 5^2"})

# Interact with User
while True:
    myrole = input("\nWhat is my role? (or type 'quitme' to quit): \n")
    if myrole == 'quitme':
        break
    mytask = input("\nWhat is my task? (or type 'quitme' to quit): \n")
    if mytask == 'quitme':
        break

    messages = [
        {"role": "system", "content": myrole},
        {"role": "user", "content": mytask}
    ]

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
         temperature=1.0,
         max_tokens=30,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        messages=messages
    )

    print("----------------\n")
    print(response.choices[0].message.content)
    print("----------------\n")
