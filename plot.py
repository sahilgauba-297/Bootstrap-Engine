import matplotlib.pyplot as plt

import data 

curve = data.curve 

plt.figure(figsize=(9,5))

plt.plot(
    curve["tenor_years"],
    curve["zero_rate"] * 100,
    marker='o'
)

plt.title("Live US Treasury Zero Curve")
plt.xlabel("Maturity (Yrs)")
plt.ylabel("zero rate %")
plt.grid(True)

plt.show()


