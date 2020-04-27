from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
p_dir = 'C:\\Users\\Mineprobe-B\\Desktop\\RandD\\Dash\\sentdex tut\\positive.txt'
n_dir = 'C:\\Users\\Mineprobe-B\\Desktop\\RandD\\Dash\\sentdex tut\\negative.txt'

pos_count = 0
pos_correct = 0

with open(p_dir,"r") as f:
    for line in f.read().split('\n'):
        analysis = TextBlob(line)

        if analysis.sentiment.polarity >= 0.1:
            if analysis.sentiment.polarity > 0:
                pos_correct += 1
            pos_count +=1


neg_count = 0
neg_correct = 0

with open(n_dir,"r") as f:
    for line in f.read().split('\n'):
        analysis = TextBlob(line)
        if analysis.sentiment.polarity <= -0.0001:
            if analysis.sentiment.polarity <= 0:
                neg_correct += 1
            neg_count +=1

print("Positive accuracy = {}% via {} samples".format(pos_correct/pos_count*100.0, pos_count))
print("Negative accuracy = {}% via {} samples".format(neg_correct/neg_count*100.0, neg_count))


'''analyzer = SentimentIntensityAnalyzer()

pos_count = 0
pos_correct = 0

with open('C:\\Users\\Mineprobe-B\\Desktop\\RandD\\Dash\\sentdex tut\\positive.txt',"r") as f:
    for line in f.read().split('\n'):
        vs = analyzer.polarity_scores(line)
        if not vs['neg'] > 0.1:
            if vs['pos']-vs['neg'] > 0:
                pos_correct += 1
            pos_count +=1


neg_count = 0
neg_correct = 0

with open('C:\\Users\\Mineprobe-B\\Desktop\\RandD\\Dash\\sentdex tut\\negative.txt',"r") as f:
    for line in f.read().split('\n'):
        vs = analyzer.polarity_scores(line)
        if not vs['pos'] > 0.1:
            if vs['pos']-vs['neg'] <= 0:
                neg_correct += 1
            neg_count +=1

print("Positive accuracy = {}% via {} samples".format(pos_correct/pos_count*100.0, pos_count))
print("Negative accuracy = {}% via {} samples".format(neg_correct/neg_count*100.0, neg_count))
'''