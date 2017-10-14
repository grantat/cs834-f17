require(ggplot2)

unigramFreq <- read.csv("./data/rankFreqUnigram.csv", head = TRUE, sep = ',')
bigramFreq <- read.csv("./data/rankFreqBigram.csv", head = TRUE, sep = ',')