__author__ = 'pasha'
import collections

def count_word(text):
    words = str(text).split()
    repeat = dict()
    for word in words:
        try:
            repeat[word] += 1
        except KeyError:
            repeat[word] = 1
    for word in repeat:
        print(word," : ",repeat[word])

def average_word(text):
    sentences = str(text).split('.')
    lens_sent = 0
    for sentence in sentences:
        lens_sent += len(sentence.split())
    print(lens_sent/len(sentences))

def median_word(text):
    sentences = str(text).split('.')
    lens_sent = []
    for sentence in sentences:
        lens_sent.append(len(sentence.split()))
    lens_sent.sort()
    print(lens_sent)
    if (len(lens_sent) % 2) == 1:
        print(lens_sent[(len(lens_sent)/2)])
    else:
        print((lens_sent[(len(lens_sent) / 2) - 1] + lens_sent[(len(lens_sent)) / 2])/2)

def topngram(text,k,n):
    words = str(text).split()
    ngrams = collections.Counter()
    for word in words:
        for i in range(len(word)-n+1):
            try:
                ngrams[word[i:n+i]] += 1
            except KeyError:
                ngrams[word[i:n+i]] = 1
    print(ngrams.most_common(k))
