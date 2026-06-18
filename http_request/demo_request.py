import asyncio
import httpx
import os

import json
from dotenv import load_dotenv

load_dotenv()

async def get_weather(lat: float, lng: float):
    async with httpx.AsyncClient() as client:
        base_url = 'https://api.openweathermap.org/data/2.5/weather'
        response = await client.get(base_url, params={
            'lat': lat,
            'lon': lng,
            'appid': os.getenv('api_key'),
            'units': 'metric',
            'lang': 'fr'
        })
        if response.is_success:
            return response.json()
        

async def get_openai_response(message: str):
    async with httpx.AsyncClient() as client:
        response = await client.post('https://api.openai.com/v1/chat/completions', json={
            'model': 'gpt-5.4-mini',
            'messages': [
                { 'role': 'developer', 'content': 'you are an assistant that user to get the main character information within a text that he will send you. The birthdate must be format into iso8601' },
                { 'role': 'user', 'content': message }
            ],
            'response_format': { 
                'type': 'json_schema',
                'json_schema': {
                    "name": "Person_schema", 
                    "schema": {
                        "type": "object",
                        "required": ["name", "birth_date", "gender"],
                        "properties": {
                            "name": { "type": "string", "maxLength": 50 },
                            "age": { "type":"integer", "minimum": 0 },
                            "birth_date": { "type": "string" },
                            "gender": { "enum": ["MALE", "FEMALE", "OTHER"] }
                        }
                    }
                } 
            }
        }, headers={
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {os.getenv('openai_key')}'
        })
        if response.is_success:
            return response.json()
        print(response.content)


async def main():

    response = await get_openai_response('Michael Turner is a graphic designer from Canada who enjoys photography and hiking. He was born on April 12, 1991, in Toronto, Ontario. Growing up, Michael developed a strong interest in art and technology, which later inspired his career in digital design. Today, he works with several international clients and spends his free time exploring nature trails and creating landscape photographs.')
    text_json = response.get('choices')[0].get('message').get('content')
    data = json.loads(text_json)
    print(data.get('name'))
    print(data.get('age'))
    print(data.get('gender'))
    print(data.get('birth_date'))

asyncio.run(main())

while True:
    pass
