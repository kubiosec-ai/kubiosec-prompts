import requests
import urllib3
import pypdf
from openai import OpenAI

# Step 1: Download the text from the given URL
# Disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Retrieve system prompt
system_prompt_url = "https://raw.githubusercontent.com/kubiosec-ai/kubiosec-prompts/refs/heads/main/project001/system_prompts/003_system.md"
system_response = requests.get(system_prompt_url, timeout=10, verify=False)
system_response.raise_for_status()  # Check if the request was successful
retrieved_system_prompt = system_response.text
print(retrieved_system_prompt)

# Retrieve user prompt
user_prompt_url = "https://raw.githubusercontent.com/kubiosec-ai/kubiosec-prompts/refs/heads/main/project001/tasks/001_task.md"
user_response = requests.get(user_prompt_url, timeout=10, verify=False)
user_response.raise_for_status()  # Check if the request was successful
retrieved_user_prompt = user_response.text
print(retrieved_user_prompt)


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
          "text": retrieved_system_prompt
        }
      ]
    },
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": retrieved_user_prompt
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
