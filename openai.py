
import openai
from config import apikey
print(apikey)
exit()
openai.api_key = 1
responce = openai.Completion.create(
    model="text-davinci-003",
    prompt ="write an email to my boss for resignation",
    temperature = 0.7,
    max_tokens = 256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)