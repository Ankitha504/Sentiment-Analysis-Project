import pandas as pd
from textblob import TextBlob

# Read dataset
df = pd.read_csv("7817_1.csv")

# Function to classify sentiment
def get_sentiment(text):
    analysis = TextBlob(str(text))
    polarity = analysis.sentiment.polarity

    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

# Create Sentiment column
df["Sentiment"] = df["reviews.text"].apply(get_sentiment)

# Count sentiments
print(df["Sentiment"].value_counts())
import matplotlib.pyplot as plt

counts = df["Sentiment"].value_counts()
counts.plot(kind="bar")

plt.title(" Sentiment Analysis")
plt.xlabel("Sentiment")
plt.ylabel("Number of Reviews")

plt.show()