library(ggplot2)

guns <- read.csv("nics-firearm-background-checks.csv")
guns <- guns[,1:6]

guns$month <- paste(guns$month, "-01", sep = "")
guns$month <- as.Date(guns$month)

guns_roses <- subset(guns, subset = state == "New York" | state == "Connecticut" | state == "New Hampshire" | state == "Pennsylvania" | state == "New Jersey" | state == "Vermont")

ggplot(guns_roses, aes(x=long_gun, y=handgun, color = factor(state))) + geom_point() + ggtitle("Long Guns and Hand Guns")
