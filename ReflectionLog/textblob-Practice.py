from textblob import TextBlob


#just to check if a sentence is positive or negative.But it is very simple
sent="boring"

txt = TextBlob(sent)

em = txt.sentiment.polarity

if em>0:
    print("positive")
elif em<0:
    print("negative")
else:
    print("neutral")