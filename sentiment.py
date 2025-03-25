from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
def sentiment_score(x,y):
    analyzer = SentimentIntensityAnalyzer()
    t3=x+''+y
    scores = analyzer.polarity_scores(t3)
    return scores
    