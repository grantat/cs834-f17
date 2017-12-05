library(cluster)
library(ggplot2)
library(factoextra)

# data
df <- read.csv("./data/cluster-data.csv", header = TRUE)
# Make NxN dimensions with euclidean distance
dist <- dist(df, method = "euclidean")
# select methods to run against
agg_methods <- c("single", "average", "complete", "centroid", "ward.D2")

# iterate through each method and make a plot
for(method in agg_methods){
  p_title <- paste("Using '", method,"' Cluster Method", sep = "")
  print(p_title)
  filename <- paste("../docs/", method, ".pdf", sep = "")
  pdf(filename)
  
  avg <- hclust(dist, method = method)
  sub_grp <- cutree(avg, k = 3)
  cluster <- fviz_cluster(list(data = df, cluster = sub_grp),
                          main = p_title, xlab = "2D Instance", ylab = "Distance Value")
  print(cluster)
  # dendrogram vis
  # filename <- paste("../docs/", method, "-dendro.pdf", sep = "")
  # pdf(filename)
  # plot(avg, cex = 0.6)
  # rect.hclust(avg, k = 4, border = 2:5)
  dev.off()
}
