df <- read.csv("401KSUBS.csv")
#Problem C8.10
#i
df$inc_2 = df$inc^2
df$age_2 = df$age^2
fit1 <- lm(e401k ~ inc+inc_2+age+age_2+male, data = df)
summary(fit1)
library(lmtest)
library(sandwich)
coeftest(fit1, vcov = vcovHC(fit1, type = "HC1"))
#iii
df$u_2 = fit1$residuals^2
df$y_hat = fit1$fitted.values
df$y_hat_2 = df$y_hat^2
fit2 <- lm(u_2 ~ y_hat+y_hat_2, data = df)
coeftest(fit2, vcov = vcovHC(fit2, type = "HC1"))
#iiii
max(df$y_hat)
min(df$y_hat)
df$h = df$y_hat * (1 - df$y_hat)
fit3 <- lm(e401k ~ inc+inc_2+age+age_2+male, weights = 1/h, data = df)
coeftest(fit3, vcov = vcovHC(fit3, type = "HC1"))

#Problem C15.8
#i
fit4 <- lm(pira ~ p401k + inc+inc_2+age+age_2, data = df)
coeftest(fit4, vcov = vcovHC(fit4, type = "HC1"))
#iv
fit5 <- lm(p401k ~ e401k+inc+inc_2+age+age_2+male, data=df)
coeftest(fit5, vcov = vcovHC(fit5, type = "HC1"))
#v
df$res1 = fit5$residuals
fit6 <- lm(pira ~ p401k + inc+inc_2+age+age_2+res1, data = df)
coeftest(fit6, vcov = vcovHC(fit6, type = "HC1"))
