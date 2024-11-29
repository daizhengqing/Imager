from zhipuai import ZhipuAI

class Bot:
  def __init__(self, api_key, model="glm-4-flash", personality=""):
    self.client = ZhipuAI(api_key=api_key)
    self.model = model
    self.messages = [{ "role": "system", "content": personality }]

  def create_message(role, content):
    return { "role": role, "content": content }
  
  def send_message(self, prompt):
    self.messages.append(self.create_message("user", prompt))

    res = self.client.chat.completions.create(
      model=self.model,
      messages=self.messages
    )

    print(res)

    self.messages.append(self.create_message("assistant", res.choices[0].message.content))
  
eliza = Bot(api_key="5b6a0901235b54cc77aa434b0da46952.HtufflSsBbGKNKqE")

eliza.send_message()