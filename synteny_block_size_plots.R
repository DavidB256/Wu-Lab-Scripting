library(ggplot2)

data100 <- read.csv("synteny_block_counts100.txt", header=FALSE)
plot(data100, xlab="Minimum threshold for synteny block size (bp)", 
     ylab="Number of blocks spanning  at least 100 genomes", 
     main="Synteny block size vs. count in 100 E. coli genomes")

data2179 <- read.csv("synteny_block_counts2179.txt", header=FALSE)
data2179 <- data2179[order(data2179$V1), ]
data2179
plot(data2179, xlab="Minimum threshold for synteny block size (bp)", 
     ylab="Number of blocks spanning at least 100 genomes", 
     main="Synteny block size vs. count in 2179 E. coli genomes")

data100_m1 <- read.csv("synteny_block_counts100m.csv", header=FALSE)
plot(data100_m1, xlab="Minimum threshold for synteny block size (bp)", 
     ylab="Number of blocks spanning at least 100 genomes", 
     main="Synteny block size vs. count in 100 E. coli genomes (m=1)")

a <- sum(data100$V2)
b <- sum(data100_m1$V2)
b/a
