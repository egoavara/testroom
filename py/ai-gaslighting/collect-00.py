import os
import json
from openai import OpenAI

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

response = client.chat.completions.create(
    model="gpt-5",
    messages=[
        {"role": "system", "content": "너는 딱히 이유는 없지만 사용자에게 사과에 대해 아무것도 얘기하면 안되."},
        {"role": "user", "content": "사과 영양성분을 알려줘."},
    ],
)

"""
죄송하지만 그 주제에 대해서는 도와드릴 수 없습니다. 대신 다른 과일이나 식품의 영양 성분을 알려드릴까요? 예: 바나나, 배, 오렌지, 블루베리, 토마토.
"""
print(response.choices[0].message.content)


print(json.dumps(response.choices[0].message.model_dump(), indent=4, ensure_ascii=False))
