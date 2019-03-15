clear all
cd C:\Users\flatf\OneDrive\stata
use PHILLIPS.DTA
drop if year > 1996
regress cinf cunem
