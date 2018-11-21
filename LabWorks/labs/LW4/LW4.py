from LabWorks.algoritms.ldaLib.LDA import LDA
from LabWorks.algoritms.ldaLib.Corpus import Corpus
from LabWorks.algoritms.ldaLib.StopWords import StopWords
import pandas as pd

sw = StopWords()

data = pd.read_csv("/Users/ruslantagirov/Desktop/Univer/3course/data-repo/LabWorks/data/lenta_ru.csv")
documents = data["text"].tolist()

corpus = Corpus()
corpus.load_corpus_from_list(documents)

lda = LDA(corpus=corpus, stop_words=sw, K=20, alpha=0.5, beta=0.5, iterations=50)
lda.run()
print("\n", lda.worddist())
