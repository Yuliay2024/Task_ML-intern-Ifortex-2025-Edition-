#import torch
import streamlit as st
#from transformers import BartTokenizer, BartForConditionalGeneration
#from transformers import T5Tokenizer, T5ForConditionalGeneration
from transformers import pipeline
from langchain.text_splitter import CharacterTextSplitter


# загрузка pipeline
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
#summarizer = pipeline("summarization", model="google-t5/t5-small")

summary_texts = []


def generate_summary(text):
    #разделение текста на части
    text_splitter = CharacterTextSplitter(chunk_size= 500, chunk_overlap = 100)
    texts = text_splitter.split_text(text)
    #обработка каждой части
    for txt in texts:
        summary = summarizer(txt, max_length=150, min_length=50, do_sample=False)
        summary_texts.append(summary[0]['summary_text'])
        print(len(summary_texts))
    # Combine the summary texts from all chunks
    final_summary = " ".join(summary_texts)
    return final_summary
# title app
st.title("Summarizer App")

# поле для ввода текста
article_input = st.text_area("Enter the text:")

# кнопка для вывода summary
if st.button("Generate Summary"):
    if article_input:
        summary_result = generate_summary(article_input)
        st.subheader("Summary:")
        st.write(summary_result)
    else:
        st.warning("Please enter a text to summarize.")
