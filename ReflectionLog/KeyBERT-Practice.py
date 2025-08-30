from keybert import KeyBERT


model = KeyBERT()

text  = "I had a lot of classes today but its was ok.I played tabletennis and foosball a lot today.I am geting worried about quant and its work.About the tasks.I have to make the Quant Alpha report by tomorrow eod.I have to do Dynamic Programming and The Green book as much as i can tomorrow.",
              
print(model.extract_keywords(text))

print(model.extract_keywords(text,keyphrase_ngram_range=(1,3),stop_words = "english",highlight=True))