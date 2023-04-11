# Main Model

## Data Cleaning

- At current phase, fetch the static data from cloud drive.
  - The static dataset contains BTC close and open price, the peak and the lowest price, the trading volume and the percentage of price change for each day from 2022-01-01 to 2023-04-10
  - 465 rows with 7 attributes `[date, price, open, high, low, vol, change]`
- Split the data into two parts:
  1. `[date, price, open]`
  2. `[date, price, high, low, change]`
- The first part of data is mainly used to predict the trend of price. The second part of data is used to provide some necessary support for fine tuning.

