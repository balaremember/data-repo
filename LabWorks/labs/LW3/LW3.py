from LabWorks.algoritms.plsaLib.PLSA import PLSA
from LabWorks.algoritms.plsaLib.StopWords import StopWords
from LabWorks.algoritms.plsaLib.Corpus import Corpus
import pandas as pd

sw = StopWords("/Users/ruslantagirov/Desktop/Univer/3course/data-repo/LabWorks/data/stopwords.dic")
sw.loadStopWordsFromFile()

data = pd.read_csv("/Users/ruslantagirov/Desktop/Univer/3course/data-repo/LabWorks/data/lenta_ru.csv")
documents = data["text"].tolist()
tags = data["tags"].tolist()

corpus = Corpus()
corpus.loadCorpusFromList(documents, tags)

K = 10    # number of topic
maxIteration = 25
threshold = 10.0
topicWordsNum = 10
docTopicDist = '/Users/ruslantagirov/Desktop/Univer/3course/data-repo/LabWorks/labs/LW3/results/' \
               'docTopicDistribution.txt'
topicWordDist = '/Users/ruslantagirov/Desktop/Univer/3course/data-repo/LabWorks/labs/LW3/results/' \
                'topicWordDistribution.txt'
dictionary = '/Users/ruslantagirov/Desktop/Univer/3course/data-repo/LabWorks/labs/LW3/results/dictionary.dic'
topicWords = '/Users/ruslantagirov/Desktop/Univer/3course/data-repo/LabWorks/labs/LW3/results/topics.txt'

plsa = PLSA(corpus, sw, K, maxIteration, threshold, topicWordsNum, docTopicDist, topicWordDist, dictionary, topicWords)
plsa.EM_Algo()
