from LabWorks.algoritms.plsaLib.PLSA import PLSA
from LabWorks.algoritms.plsaLib.StopWords import StopWords
from LabWorks.algoritms.plsaLib.Corpus import Corpus

sw = StopWords()
sw.loadStopWords()

corpus = Corpus()
corpus.generateCorpus("/Users/ruslantagirov/Desktop/Univer/3course/data-repo/LabWorks/data/lenta_ru.csv")

plsa = PLSA(corpus, sw)
plsa.EM()
