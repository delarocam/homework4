"""This file is to make plots to investiage the campus dataset"""

import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# importing data

data = pd.read_csv(r"campus.csv")

# 1.1 .)

plt.figure(1)

plt.hist(data["crime"], bins=10)

plt.title("Frequency of Crime")

plt.xlabel("num Crimes")

hist_crime = plt.ylabel("Count of campuses")


# 1.2 .)

plt.figure(2)

plt.scatter(data["lenroll"], data["lcrime"])

plt.title("lenroll vs lcrime")

plt.xlabel("lenroll")

scatter_crime = plt.ylabel("lcrime")


# 1.3 .)


fig_crime, axs = plt.subplots(2, 2)
axs[0, 0].scatter(data["lenroll"], data["lcrime"])
axs[0, 0].set_title("Lenroll vs Lcrime")
axs[0, 1].scatter(data["lpolice"], data["lcrime"])
axs[0, 1].set_title('lpolice vs lcrime')
axs[1, 0].scatter(data["priv"], data["crime"])
axs[1, 0].set_title("Private vs crime")

plt.figure(3)

# 1.4 .)
# saving ols estimates recieved from previous problem set

plt.figure(4)

Beta_0 = -6.63136926
Beta_1 = 1.26976026

plt.scatter(data["lenroll"], data["lcrime"], color="b")

plt.plot(data["lenroll"], Beta_1 * data["lenroll"] + Beta_0,
         color="r", label="logcrime=-6.631 +  1.269* logenroll")

plt.title("OLS line")

plt.xlabel("lenroll")

plt.ylabel("lcrime")


regress_crime = plt.legend()
