from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

#not so simple analysis now

sent="i love cheeseburgers"

sen = SentimentIntensityAnalyzer()

em = sen.polarity_scores(sent)

print(em)

if em["compound"]>=0.05:
    print("positive")
elif em["compound"]<=0.05:
    print("negative")
else:
    print("neutral")