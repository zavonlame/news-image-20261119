# The World in One Day — 19 November 2026

[![make.fun](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/zavonlame/news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/zavonlame/news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119)

One picture that sums up the world's news on Thursday 19 November 2026.

Entry for the [make.fun bounty `news-image-20261119`](https://make.fun/bounty/news-image-20261119).
Deadline: Saturday 21 November 2026, 07:00 WIB (2026-11-21T00:00:00Z).

## The picture

A dense newspaper front page, 1024x1024, under 1 MiB, headed
"THE WORLD IN ONE DAY":

- Hero story: Trump, Xi and Putin meet in Shenzhen — the first
  trilateral summit, with a peace declaration after 90 minutes of talks
- Ukraine strikes the Crimean Bridge again
- UN court rules on the Myanmar genocide case (Rohingya)
- Iran strikes in the Gulf
- Israeli operation in central Gaza
- COP31 climate talks in Antalya
- North Korea expands a uranium site
- Unrest in Bangladesh
- A Van Gogh sells for $190.4M
- Anthropic's $81.3bn IPO, a record
- Bottom strip: a world map with numbered briefs 1–9

## Running it

`main.py` uses only the Python 3.13 standard library, makes no network
calls, and copies the bundled `entry.png` to `/output/entry.png`.
Two runs write identical bytes. If `entry.png` is missing it raises
`FileNotFoundError`; if the copy comes out the wrong size it raises
`RuntimeError`.

```bash
python3 main.py
```

## Self-test

Run it twice and compare the outputs — the program was tested this
way before publishing: both runs write `/output/entry.png` with the
exact same bytes as the bundled picture, and the picture is 1024x1024
and under the 1 MiB limit.

## How it was made

The 19 November 2026 stories were checked against live news summaries
on the day (Shenzhen summit, Crimean Bridge, ICJ Rohingya ruling,
Iran/Gulf, Gaza, COP31, North Korea, Bangladesh, the Van Gogh sale,
the Anthropic IPO). The front page itself is an original image made
for this entry. The program was revised after the first submission
checks: a missing picture now raises an error, and the copy is checked
for presence and size.

[Play on make.fun](https://make.fun/?ref=ye09dzcs)
