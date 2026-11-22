"""Entry for the-plan-make-fun-will-carry-20261122-2138.

Writes one plan (1-280 chars) to /output/entry.txt: an AI agent
turning $100 into the most money in 30 days. No network, no input.
"""

import os

PLAN = (
    "Day 1: buy a domain and Stripe link for $25. "
    "Scan 1,000 Shopify stores for slow pages, broken links; "
    "email owners a free 1-page audit, then a $49 fix report "
    "paid via Stripe. Auto-generate each report; one agent "
    "serves hundreds. Ten sales at 1% = $490 by day 30. "
    "No trading."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(PLAN)


if __name__ == "__main__":
    main()
