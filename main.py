# This program creates a chatbot that learns from YouTube, websites, and PDFs and answers your questions continuously.

# Algorithm - 
# 1. Create a chatbot
# 2. Teach it using:
#       * YouTube video
#       * Website
#       * PDF
# 3. Keep asking questions
# 4. Chatbot answers based on what it learned

from embedchain import App
import os

api_key = os.environ['OPENAI_API_KEY']

chat_bot = App()  #Create a chatbot

chat_bot.add("youtube_video","https://youtu.be/1bc-30XyEeI?si=Md87dLISlwWq2foU") #Teach it using YouTube video
# chat_bot.add("Website/Webpage","") #Teach it using Website
# chat_bot.add("Pdf file","") #Teach it using PDF

while True: # Keep asking questions
  input_query = input("\nAsk your question: ") #Ask a question
  answer = chat_bot.query(input_query) #Chatbot answers based on what it learned
  print(f"Answer: {answer}\n") #Print the answer
  
  