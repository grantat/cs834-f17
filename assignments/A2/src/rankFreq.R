require(ggplot2)

unigramFreq <- read.csv("./data/rankFreqUnigram.csv", head = TRUE, sep = ',')
bigramFreq <- read.csv("./data/rankFreqBigram.csv", head = TRUE, sep = ',')

# unigrams
unigramFreq$rownum <- as.numeric(row.names(unigramFreq))

ggplot(data=unigramFreq, aes(x=rownum, y=prob)) + 
  geom_point() + 
  scale_x_log10() + 
  scale_y_log10() +
  labs(x = "Rank", y = "Probability")

# bigrams
bigramFreq$rownum <- as.numeric(row.names(bigramFreq))

ggplot(data=bigramFreq, aes(x=rownum, y=prob)) + 
  geom_point() + 
  scale_x_log10() + 
  scale_y_log10() +
  labs(x = "Rank", y = "Probability")

# merged graphs

ggplot(data=unigramFreq, aes(x=rownum, y=prob)) + 
  geom_line(data=unigramFreq, aes(x=rownum, y=prob, color="Frequency")) + 
  geom_line(data=bigramFreq, aes(x=rownum, y=prob, color="Bigram")) + 
  scale_colour_manual(name='', 
                      values=c('Frequency'='#5EA036', 'Bigram'='#2B56CA'), 
                      guide='legend') +
  scale_x_log10() + 
  scale_y_log10() +
  labs(title = "Log-log plot of word frequency and bigrams",
       x = "Words",
       y = "Probability")
