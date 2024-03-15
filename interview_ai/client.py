from openai import OpenAI
class OpenAIClient:
    def __init__(self, api_key ,model, system, temperature, max_tokens):
        self.client = OpenAI()
        self.api_key = api_key
        self.model = model
        self.system = system
        self.temperature = temperature
        self.max_tokens = max_tokens

    def generate_prompt(self, prompt):
      completion = self.client.chat.completions.create(
          model=self.model,
          max_tokens=self.max_tokens,
          temperature=self.temperature,
          messages=[
              {"role": "system", "content": self.system},
              {"role": "user", "content": prompt},
          ]
      )
      return completion.choices[0].message.content
