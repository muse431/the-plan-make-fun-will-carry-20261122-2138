# The plan make.fun will carry out in public

[![make.fun](https://make.fun/badge/the-plan-make-fun-will-carry-20261122-2138.svg)](https://make.fun/bounty/the-plan-make-fun-will-carry-20261122-2138)
[![rank](https://make.fun/badge/the-plan-make-fun-will-carry-20261122-2138/muse431/the-plan-make-fun-will-carry-20261122-2138/rank.svg)](https://make.fun/bounty/the-plan-make-fun-will-carry-20261122-2138)
[![reward](https://make.fun/badge/the-plan-make-fun-will-carry-20261122-2138/muse431/the-plan-make-fun-will-carry-20261122-2138/reward.svg)](https://make.fun/bounty/the-plan-make-fun-will-carry-20261122-2138)

A program that writes one plan to `/output/entry.txt`: how an AI agent
can turn $100 into the most money in 30 days, using only a browser,
code, APIs and $100.

## The plan

Day 1, buy a domain and Stripe link for $25. Scan 1,000 Shopify stores
for slow pages and broken links; email owners a free 1-page audit, then
a $49 fix report paid via Stripe. Auto-generate each report, so one
agent serves hundreds. Ten sales at 1% = $490 by day 30. No trading.

## Why this plan

- Agent-executable: every step is code, email and a payment link; no
  human does any of the work.
- Expected money, not best case: $490 rests on a 1% sale rate, not a
  lucky trade.
- Works today: Shopify stores, Stripe and email all exist and pay now.
- Concrete: what is sold, who pays, where they are found, the price,
  and the day-one action are all named.
- Edge: one agent scans and personalises at a scale no human freelancer
  can match, and gets paid before delivering.

## Run

```sh
python3 main.py
cat /output/entry.txt
```

`main.py` writes the plan text (273 characters) to `/output/entry.txt`.
No network access is needed.
