library(ggplot2)

shelter <- read.csv("DHS_Daily_Report.csv")

shelter$Date.of.Census <- as.Date(shelter$Date.of.Census, format = "%m/%d/%Y")

homeless <- shelter$Total.Children.in.Shelter / shelter$Total.Individuals.in.Shelter

ggplot(shelter, aes(x=dates, y= homeless)) + geom_line(color = "Blue") + ggtitle("Children in Shelter")
