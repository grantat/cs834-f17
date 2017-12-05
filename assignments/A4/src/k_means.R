library(cluster)
library(ggplot2)
library(factoextra)

# data
df <- read.csv("./data/cluster-data.csv", header = TRUE)

# Make NxN dimensions with euclidean distance
euc_dis <- dist(df, method = "euclidean")

cosineDist <- function(x){
  as.dist(1 - x%*%t(x)/(sqrt(rowSums(x^2) %*% t(rowSums(x^2))))) 
}
cos_sim <- cosineDist(as.matrix(df))

pdf("../docs/kmeans-euc.pdf")
k2 <- kmeans(euc_dis, centers = 2, nstart = 25)
clust <- fviz_cluster(k2, data = df,
                      main = "Euclidean Distance K-Means",
                      xlab = "2D Instance", ylab = "Cluster Height")
print(clust)
dev.off()

pdf("../docs/kmeans-cos.pdf")
cos_k2 <- kmeans(cos_sim, centers = 2, nstart = 25)
clust <- fviz_cluster(cos_k2, data = df,
                      main = "Cosine Similarity K-Means",
                      xlab = "2D Instance", ylab = "Cluster Height")
print(clust)
dev.off()