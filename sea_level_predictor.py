import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# 1. Import the data
df = pd.read_csv('epa-sea-level.csv')

# 2. Create scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='b', label='Data')

# 3. Create first line of best fit using all the data
slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
years_extended = pd.Series(range(1880, 2051))  # Extend the range to 2050
line_fit = intercept + slope * years_extended

# Plot the first line of best fit
plt.plot(years_extended, line_fit, 'r', label='Best fit line (1880-2050)', linewidth=2)

# 4. Create second line of best fit using data from year 2000 onwards
df_recent = df[df['Year'] >= 2000]
slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
years_recent_extended = pd.Series(range(2000, 2051))
line_recent_fit = intercept_recent + slope_recent * years_recent_extended

# Plot the second line of best fit
plt.plot(years_recent_extended, line_recent_fit, 'g', label='Best fit line (2000-2050)', linewidth=2)

# 5. Add labels, title, and legend
plt.xlabel('Year')
plt.ylabel('Sea Level (inches)')
plt.title('Rise in Sea Level')
plt.legend()

# 6. Save plot and return data for unit tests
plt.savefig('sea_level_plot.png')
plt.show()
