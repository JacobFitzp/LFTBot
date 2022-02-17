# Lateral Flow Test Bot

This Python script will automatically attempt to order a pack of lateral flow tests from the government website.

### Disclaimer

I do not condone the use of this script for anything other than ordering the LFT's that you actually **need** - It is intended to help automoate the process for people who are having trouble getting hold of them.

## Setup

### Prerequisites 

- Install Python 3
- Install dependencies 
  - `pip install selenium`

### Setup

1. Open config.py and enter your NHS login details - You will need to create an account manually if you don't already have one.
2. Go to https://chromedriver.chromium.org/downloads and download the relevant chromium driver (the one included is for an M1 Mac).
3. Replace `drivers/chromedriver` with the driver you downloaded above.
