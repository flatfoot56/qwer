df <- read.csv('cps99_ps1.csv')

#Problem 5
cor(df$yrseduc, df$female)

#Problem 7
#a
fit1 <- lm(df$ahe ~ df$yrseduc, data = df)
fit2 <- lm(df$ahe ~ df$yrseduc + df$female, data = df)

summary(fit2)

#b
library(lmtest)
coeftest(fit2, vcov = vcovHC(fit2, type = "HC1"))

#c
summary(fit1)

#Problem 8
fit3 <- lm(df$ahe ~ df$yrseduc + df$ba, data = df)
summary(fit3)
confint(fit3, vcov = vcovHC(fit3, type = "HC1"))
