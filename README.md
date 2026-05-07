# Treasury Yield Curve Engine

## Overview

This project builds a **live U.S. Treasury yield curve pipeline** using market data from FRED. It converts raw Treasury yields into a structured **zero-coupon curve**, which is the foundation for fixed income pricing and interest rate risk modeling.

---

## Data Pipeline

We start with real market data from FRED:

- 3M → DGS3MO  
- 6M → DGS6MO  
- 1Y → DGS1  
- 2Y → DGS2  
- 5Y → DGS5  
- 10Y → DGS10  

These are **constant-maturity Treasury yields updated daily**.

---

## Step 1: Build Yield Curve Snapshot

We extract the latest available observation and construct a cross-sectional curve:

- Maturity (in years)
- Market yield (in %)

This gives us a **single point-in-time yield curve**.

---

## Step 2: Convert Yields to Decimal Form

Market yields are quoted in percentage form:

$$
r = \frac{\text{yield}}{100}
$$

This is necessary because all financial formulas operate on decimal rates.

---

## Step 3: Construct Discount Factors

We convert yields into present value multipliers using continuous compounding:

$$
D(t) = e^{-r(t)t}
$$

Where:
- \(D(t)\) = discount factor
- \(r(t)\) = yield at maturity \(t\)
- \(t\) = time in years

---

##  Step 4: Build Zero Curve

We convert discount factors back into continuously compounded zero rates:

$$
r(t) = -\frac{\ln D(t)}{t}
$$

This produces the **zero-coupon yield curve**, which is the true term structure of interest rates.

---

## Output Structure

The final data contains:

| Column | Meaning |
|---|---|
| tenor_years | Time to maturity |
| yield_pct | Market observed yield |
| r | Decimal yield |
| discount_factor | Present value of $1 |
| zero_rate | Continuously compounded zero rate |

---

## Visualization

We plot:

- X-axis → maturity (years)
- Y-axis → zero rate (%)

This gives a **live Treasury zero curve snapshot**.

---

## What This System Represents

We have built a simplified **rates curve engine**:

> Market yields → discount factors → zero rates → yield curve visualization

---

## Future Idea

The current system is a **discrete curve model**.

Next upgrades will include:

- Spline interpolation for smooth curves  
- Forward rate curve extraction  
- Interest rate shock simulations  
- Bond duration & convexity engine  
- Full bootstrapped bond pricing system  

---