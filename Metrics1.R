df <- read.csv("cps99_ps1.csv")
#Problem 5

ahe_mean <- mean(df$ahe)
ahe_sd <- sd(df$ahe)
yrseduc_mean <- mean(df$yrseduc)
yrseduc_sd <- sd(df$yrseduc)
female_mean <- mean(df$female)
female_sd <- sd(df$female)

#Problem 6
#1
fit <- lm(ahe ~ yrseduc, df)
summary(fit)

#2
library(ggplot2)
test <- function(x) {1.32186 * x -2.60905}

ggplot(df, aes(yrseduc, ahe)) + geom_point() + geom_smooth(method='lm', se = F)

#3
library(sandwich)
library(lmtest)
coeftest(fit, vcov = vcovHC(fit, type = "HC1"))

#4
confint(fit, vcov = vcovHC(fit, type = "HC1"))


