df = read.csv("grain.csv")

#Problem 4
fit <- lm(log(price) ~ log(quantity)+seas1+seas2+seas3+seas4+seas5+seas6+seas7+seas8+seas9+seas10+seas11+seas12, data=df)
summary(fit)
library(lmtest)
coeftest(fit, vcov = vcovHC(fit, type = "HC1"))

#Problem 5
#a
cor(df$cartel, log(df$price))
#b
cor(df$ice, log(df$price))

#Problem 6
#1
fit1 <- lm(log(price) ~ cartel+seas1+seas2+seas3+seas4+seas5+seas6+seas7+seas8+seas9+seas10+seas11+seas12, data=df)
coeftest(fit1, vcov = vcovHC(fit1, type = "HC1"))
library(car)
myH0 <- c("seas1 = 0", "seas2 = 0", "seas3 = 0", "seas4 = 0", "seas5 = 0", "seas6 = 0", "seas7 = 0", "seas8 = 0", "seas9 = 0", "seas10 = 0", "seas11 = 0", "seas12 = 0")
linearHypothesis(fit1, myH0, vcov = vcovHC(fit1, type = "HC1"))

#2
fit2 <- lm(log(quantity) ~ log(price)+seas1+seas2+seas3+seas4+seas5+seas6+seas7+seas8+seas9+seas10+seas11+seas12, data=df)
coeftest(fit2, vcov = vcovHC(fit2, type = "HC1"))
linearHypothesis(fit2, myH0, vcov = vcovHC(fit2, type = "HC1"))

#3
library(AER)
fit3 <- ivreg(log(quantity) ~ log(price)+seas1+seas2+seas3+seas4+seas5+seas6+seas7+seas8+seas9+seas10+seas11+seas12|seas1+seas2+seas3+seas4+seas5+seas6+seas7+seas8+seas9+seas10+seas11+seas12+cartel, data=df)
coeftest(fit3, vcov = vcovHC(fit3, type = "HC1"))
linearHypothesis(fit3, myH0, vcov = vcovHC(fit3, type = "HC1"))
#First stage regression:
first_stage <- lm(log(price) ~ seas1+seas2+seas3+seas4+seas5+seas6+seas7+seas8+seas9+seas10+seas11+seas12 + cartel, data=df)
coeftest(first_stage, vcov = vcovHC(first_stage, type = "HC1"))
linearHypothesis(first_stage, c("cartel=0"), vcov = vcovHC(first_stage, type = "HC1"))


#4
fit4 <- ivreg(log(quantity) ~ log(price)+seas1+seas2+seas3+seas4+seas5+seas6+seas7+seas8+seas9+seas10+seas11+seas12|seas1+seas2+seas3+seas4+seas5+seas6+seas7+seas8+seas9+seas10+seas11+seas12+ice, data=df)
coeftest(fit4, vcov = vcovHC(fit4, type = "HC1"))
linearHypothesis(fit4, myH0, vcov = vcovHC(fit4, type = "HC1"))
#First stage regression:
first_stage_4 <- lm(log(price) ~ seas1+seas2+seas3+seas4+seas5+seas6+seas7+seas8+seas9+seas10+seas11+seas12 + ice, data=df)
coeftest(first_stage_4, vcov = vcovHC(first_stage_4, type = "HC1"))
linearHypothesis(first_stage_4, c("ice=0"), vcov = vcovHC(first_stage_4, type = "HC1"))


#5
fit5 <- ivreg(log(quantity) ~ log(price)+seas1+seas2+seas3+seas4+seas5+seas6+seas7+seas8+seas9+seas10+seas11+seas12|seas1+seas2+seas3+seas4+seas5+seas6+seas7+seas8+seas9+seas10+seas11+seas12+ice+cartel, data=df)
coeftest(fit5, vcov = vcovHC(fit5, type = "HC1"))
linearHypothesis(fit5, myH0, vcov = vcovHC(fit5, type = "HC1"))
#First stage regression:
first_stage_5 <- lm(log(price) ~ seas1+seas2+seas3+seas4+seas5+seas6+seas7+seas8+seas9+seas10+seas11+seas12 + ice + cartel, data=df)
myH0 <- c("cartel = 0", "ice = 0")
linearHypothesis(first_stage_5, myH0, vcov = vcovHC(first_stage_5, type = "HC1"))

#J-test
df$res = fit5$residuals
fit5_j <- lm(res ~ seas1+seas2+seas3+seas4+seas5+seas6+seas7+seas8+seas9+seas10+seas11+seas12+ice+cartel, data=df)
jtest <- linearHypothesis(fit5_j, c("ice=0", "cartel=0"), vcov = vcovHC(fit5_j, type = "HC1"))
jstat = jtest$Df[2] * jtest$F[2]
1 - pchisq(jstat,1)



