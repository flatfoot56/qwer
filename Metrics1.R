df <- read.csv("cps99_ps1.csv")
#Problem 5

ahe_mean <- mean(df$ahe)
ahe_sd <- sd(df$ahe)
yrseduc_mean <- mean(df$yrseduc)
yrseduc_sd <- sd(df$yrseduc)
female_mean <- mean(df$female)
female_sd <- sd(df$female)

#Problem 6
#a
fit <- lm(ahe ~ yrseduc, df)
summary(fit)

#b
library(ggplot2)
test <- function(x) {1.32186 * x -2.60905}

ggplot(df, aes(yrseduc, ahe)) + geom_point() + geom_smooth(method='lm', se = F)

#c
library(sandwich)
library(lmtest)
coeftest(fit, vcov = vcovHC(fit, type = "HC1"))

#d
confint(fit, vcov = vcovHC(fit, type = "HC1"))

#f
cor(df$ahe, df$yrseduc)

#g
sqrt(mean(fit$residuals^2))

#Problem 7
fit2 <- lm(ahe ~ female, df)
summary(fit2)

#b
coeftest(fit2, vcov = vcovHC(fit2, type = "HC1"))

#c
male_mean <- mean(df$ahe[df$female == 0])
female_mean <- mean(df$ahe[df$female == 1])
sd_w = sd(df$ahe[df$female == 1])
sd_m = sd(df$ahe[df$female == 0])
t.test(df$ahe[df$female == 1], df$ahe[df$female == 0])