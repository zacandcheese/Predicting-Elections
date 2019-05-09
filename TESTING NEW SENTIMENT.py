#TESTING NEW SENTIMENT
from textblob import TextBlob
message = "GET HIM OUT. Trump sucks"
analysis = TextBlob(message)

print(analysis.sentiment.polarity)
print(analysis.sentiment)