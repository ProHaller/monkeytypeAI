import os
from dotenv import load_dotenv
from openai import OpenAI


def initialize_openai():
    load_dotenv()

    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    OPENAI_ORG = os.getenv("OPENAI_ORG")

    client = OpenAI(
        api_key=OPENAI_API_KEY,
        organization=OPENAI_ORG,
    )
    return client


def split_into_sentences(text, max_length=80):
    sentences = []
    current_sentence = ""

    for word in text.split():
        if len(current_sentence + " " + word) <= max_length:
            current_sentence += " " + word
        else:
            sentences.append(current_sentence.strip())
            current_sentence = word

    if current_sentence:
        sentences.append(current_sentence.strip())

    return sentences


def get_text(
    input_text: str,
    system_prompt: str = "You are a MonkeyType text generator bot. Given a theme, you will generate a series of sentences related to it, breaking the line between each sentence.",
    temperature: float = 0,
    model: str = "gpt-3.5-turbo",
):
    client = initialize_openai()
    response = client.chat.completions.create(
        model=model,
        temperature=temperature,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": input_text},
        ],
    )
    text = response.choices[0].message.content
    sentences = split_into_sentences(text)
    return "\n".join(sentences)
