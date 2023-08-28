island <- read.csv("islandsHistPop.csv", skip = 3)

DR <- (island$Dominican.Republic)
m <- mean(island$Dominican.Republic, names = island$Year) 
abline(h = m)

