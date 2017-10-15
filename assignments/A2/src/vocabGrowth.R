require(ggplot2)

corpusGrowth <- read.csv("./data/corpusGrowth.csv", head = TRUE, sep = ',')
corpusGrowthRev <- read.csv("./data/corpusGrowthReverse.csv", head = TRUE, sep = ',')

# vocab growth function assuming data formatted appropriately
vocab_growth <- function(df){
  x <- df$corpus_size
  y <- df$vocab_count
  
  # fit to non-linear least squares model
  fit <- nls(y~k*(x^b), data = df, start = list(k=1,b=1))
  print(summary(fit))
  cor(y, predict(fit))
  
  p <- ggplot(data=df, aes(x=corpus_size, y=vocab_count)) +
    geom_line(aes(group = 1, color="Actual")) + 
    geom_line(data=corpusGrowth, aes(x=corpus_size, y=predict(fit), color="Heaps")) + 
    scale_colour_manual(name='', values=c('Actual'='#5EA036', 'Heaps'='#2B56CA'), guide='legend') +
    labs(title='',x = 'Word Count', y = 'Vocab Count')
  
  print(p)
}

# execute on both data frames
vocab_growth(corpusGrowth)
vocab_growth(corpusGrowthRev)
