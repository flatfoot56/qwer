df <- read.csv('cps99_ps1.csv')

#Problem 3
#a
fit1 <- lm(log(df$ahe) ~ df$yrseduc+age+female+hsdipl, data = df)
reg <- summary(fit1)
#b
sqrt(mean(fit1$residuals^2))
reg$sigma
#c
library(lmtest)
library(sandwich)
confint(fit1, vcov = vcovHC(fit1, type = "HC1"))
#d
coeftest(fit1, vcov = vcovHC(fit1, type = "HC1"))
#e
fit2 <- lm(log(ahe)~hsdipl+age+female, data = df)
summary(fit2)

#f
df$hsdip_1 = df$hsdipl - 1
df$yrseduc_2 = df$yrseduc - 2
fit3 <- lm(log(ahe)~ id+hsdip_1+yrseduc_2+age+female, data=df)
summary(fit3)
confint(fit3, vcov = vcovHC(fit3, type = "HC1"))

#Problem 4
#a
df$age_sq = df$age^2
fit4 <- lm(log(ahe)~yrseduc+age+age_sq+female+hsdipl, data = df)
summary(fit4)

#b
coeftest(fit4, vcov = vcovHC(fit4, type = "HC1"))
#c
cor(df$age^2, df$female)
#d
df$age_cub = df$age^3
fit5 <- lm(log(ahe)~age+age_sq+age_cub+female+hsdipl+yrseduc, data = df)
summary(fit5)
coeftest(fit5, vcov = vcovHC(fit5, type = "HC1"))
#e
library(car)
myH0 <- c("age_sq = 0", "age_cub = 0")
linearHypothesis(fit5, myH0, vcov = vcovHC(fit5, type = "HC1"))