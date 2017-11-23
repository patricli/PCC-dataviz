import csv
from datetime import datetime

from matplotlib import pyplot as plt

# Get data for CSCO stock.
filename = 'CSCO.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, CSCO_highs = [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            CSCO_high = float(row[2])

        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            CSCO_highs.append(CSCO_high)

#get data for NTAP
filename2 = 'NTAP.csv'
with open(filename2) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    NTAP_highs = []
    for row in reader:
        try:
            NTAP_high = float(row[2])

        except ValueError:
            print(current_date, 'missing data')
        else:

            NTAP_highs.append(NTAP_high)

# Plot data.
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, CSCO_highs, c='red', alpha=0.5)
plt.plot(dates, NTAP_highs, c='blue', alpha=0.5)
#plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot.
title = "Tech stocks, Last 30 days"
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Price", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
