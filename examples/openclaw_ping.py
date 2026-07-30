import os

from dotenv import load_dotenv
from openai import OpenAI
from openai.types.chat.chat_completion import ChatCompletion

load_dotenv()


def openclaw_ping() -> ChatCompletion:
    url = os.getenv("OPENCLAW_GATEWAY_URL", default="http://127.0.0.1:18789/v1")
    client = OpenAI(base_url=url, api_key=f"{os.getenv('OPENCLAW_GATEWAY_PASSWORD')}")

    response = client.chat.completions.create(
        model="openclaw/default", messages=[{"role": "user", "content": "Ping!"}]
    )

    return response


def main():
    response = openclaw_ping()
    print(response.choices[0].message.content)


if __name__ == "__main__":
    main()
