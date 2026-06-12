import json
import matplotlib.pyplot as plt
import pandas as pd

try:
    with open("poland_eurostat_inflation.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    df = pd.DataFrame(data)
    print("[INFO] Data successfully loaded.")
except FileNotFoundError:
    print(
        "[ERROR] 'poland_eurostat_inflation.json' not found. Please run the data extraction script first."
    )
    exit()


df["date"] = df["year"].astype(str) + "-" + df["month"].str.replace("Month ", "")


df = df.sort_values("date")


plt.figure(figsize=(14, 7))
plt.plot(
    df["date"],
    df["inflation_rate_yoy"],
    marker="o",
    color="#0077B5",  
    linewidth=2.5,
    label="Inflation Rate (YoY %)",
)


plt.title(
    "Poland Annual Inflation Trend (2020 - 2025)", fontsize=16, fontweight="bold"
)
plt.xlabel("Timeline (Year-Month)", fontsize=12)
plt.ylabel("Inflation Rate (%)", fontsize=12)
plt.grid(True, linestyle="--", alpha=0.5)


plt.xticks(rotation=45, fontsize=9)
plt.gca().xaxis.set_major_locator(plt.MaxNLocator(20))

plt.legend(loc="upper right", fontsize=11)
plt.tight_layout()


output_image = "poland_inflation_chart.png"
plt.savefig(output_image, dpi=300)
print(
    f"[SUCCESS] High-res chart generated and saved securely as '{output_image}'!"
)
plt.show()