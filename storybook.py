from openai import OpenAI
import os
import streamlit as st


client = OpenAI(
    api_key = os.environ['OPENAI_API_KEY']
)

# Story
def story_gen(prompt):
  system_prompt = """
  You are a renowed author.
  Given a concept of a story, generate a short story in the style of     that concept with a twist ending.
  The story should within 150 words with only english in language
  """
  response = client.chat.completions.create(
      model = "gpt-4o-mini",
      messages = [
          {'role': "system", 'content': system_prompt},
          {'role': "user", 'content': prompt}
      ],
      temperature = 1,
      max_tokens = 2000
  )
  return response.choices[0].message.content

# cover
def art_gen(prompt):
  response = client.images.generate(
      model = "dall-e-3",
      prompt = prompt,
      size = "1024x1024",
      quality = "standard",
      style = "vivid",
      n = 1
  )
  return response.data[0].url


# Streamlit Interface
prompt = st.text_input("Enter a concept for a story")
if st.button("Generate"):
    st.write(story_gen(prompt))
    st.markdown("---")  # Divider
    st.image(art_gen(prompt))
    st.write("Thank you for using our app!")