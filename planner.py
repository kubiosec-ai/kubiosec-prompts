import requests
import urllib3
import pypdf
from openai import OpenAI

# Step 1: Download the text from the given URL
# Disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = "https://raw.githubusercontent.com/kubiosec-ai/kubiosec-prompts/refs/heads/main/project001/system_prompts/003_system.md"
response = requests.get(url, timeout=10, verify=False)
response.raise_for_status()  # Check if the request was successful
text_from_url = response.text
print(text_from_url)


# Step 2: Use the downloaded text in the OpenAI client call
client = OpenAI()

response = client.chat.completions.create(
  model="gpt-4o",
  messages=[
    {
      "role": "system",
      "content": [
        {
          "type": "text",
          "text": text_from_url
        }
      ]
    },
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "Write me a training on CNAPP (cloud native application protection platform). I need to explain high level concepts as well as interesting low level details."
        }
      ]
    }
  ],
  temperature=1,
  max_tokens=2048,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0,
  response_format={
    "type": "text"
  }
)

print("----------------------  Response from OpenAI  ----------------------")
with open("plan.md", "w") as file:
  file.write(response.choices[0].message.content)
