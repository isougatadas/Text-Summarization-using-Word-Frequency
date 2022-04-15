from turtle import pen, title
import streamlit as st
import re
import heapq
import nltk
nltk.download('punkt')
nltk.download('stopwords')


st.set_page_config(
page_title="Text Summarization",
layout="centered", 
initial_sidebar_state="auto", 
menu_items=None
)

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """

st.markdown(hide_st_style, unsafe_allow_html=True)

st.write('''
## Text Summarization using Word Frequency
''')

inp_article = st.text_input("", placeholder="write or paste the sentence here and press 'Enter'")
inp_article = inp_article.lower()
clean_text = re.sub('[^a-zA-Z]', ' ', inp_article)
clean_text = re.sub('\s+', ' ', clean_text)
sentence_list = nltk.sent_tokenize(inp_article)
nltk.download('stopwords')
stopwords = nltk.corpus.stopwords.words('english')

word_frequencies = {}
for word in nltk.word_tokenize(clean_text):
    if word not in stopwords:
        if word not in word_frequencies:
            word_frequencies[word] = 1
        else:
            word_frequencies[word] += 1

maximum_frequency = max(word_frequencies.values())
for word in word_frequencies:
    word_frequencies[word] = word_frequencies[word] / maximum_frequency

sentence_scores = {}
for sentence in sentence_list:
    for word in nltk.word_tokenize(sentence):
        if word in word_frequencies and len(sentence.split(' ')) < 30:
            if sentence not in sentence_scores:
                sentence_scores[sentence] = word_frequencies[word]
            else:
                sentence_scores[sentence] += word_frequencies[word]

summary = heapq.nlargest(5, sentence_scores, key=sentence_scores.get)
##print(" ".join(summary))
st.write('''
##### Below is the summary of the given sentence
''')
st.write(" ".join(summary).capitalize())