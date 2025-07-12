#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from nltk.chat.util import Chat, reflections

pairs = [
    [r"hi|hello", ["Hello!", "Hi there!"]],
    [r"what is your name?", ["I am a chatbot created in Python."]],
    [r"how are you?", ["I'm doing well, thank you!"]],
    [r"quit", ["Bye!"]]
]

chatbot = Chat(pairs, reflections)
chatbot.converse()

