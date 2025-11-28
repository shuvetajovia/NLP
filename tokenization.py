from tensorflow.keras.preprocessing.text import Tokenizer
sentences = [
    'i love learning NLP',
    'I, love myself',
    'Im passionate !'
]

tokenizer = Tokenizer(num_words = 100)
tokenizer.fit_on_texts(sentences)
word_index = tokenizer.word_index
print(word_index)