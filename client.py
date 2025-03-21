from openai import OpenAI

client = OpenAI(
    # The program is totally correct and workable just need api_key to run this
    # Due to security and confidential reason I have revoked my api_key
    # Revoked my api_key so program doesn't give output, you can replace ypor api_key to see the output of this program
    api_key="please place your api key here",
)

completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "system",
            "content": "You are a virtual assistant named jarvis skilled in general taska like Alexa and google cloud.",
        },
        {"role": "user", "content": "what is python."},
    ],
)

print(completion.choices[0].message.content)
