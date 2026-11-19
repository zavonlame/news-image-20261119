# The World in One Day — Thursday 19 November 2026

[![make.fun](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/zavonlame/news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/zavonlame/news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119)

Sum up 19 November 2026 world news in one image.

Entry for [make.fun bounty `news-image-20261119`](https://make.fun/bounty/news-image-20261119).
Deadline: Saturday 21 November 2026, 07:00 WIB (2026-11-21T00:00:00Z).

## What it is

A dense newspaper front page, 1024x1024, under 1 MiB:

- Hero: Trump, Xi and Putin meet in Shenzhen — first trilateral summit, peace declaration after 90-minute talks
- Ukraine hits Crimean Bridge again
- UN court: Myanmar genocide (Rohingya)
- Iran strikes Gulf
- Israel operation in central Gaza
- COP31 talks in Antalya
- North Korea expands uranium site
- Bangladesh unrest
- Van Gogh sells for $190.4M
- Anthropic IPO $81.3bn record
- Bottom strip: world map + numbered briefs 1–9

## How it runs

`main.py` (Python 3.13, standard library only, no network) copies the
bundled `entry.png` to `/output/entry.png`. It is deterministic: two runs
write identical bytes. It raises `FileNotFoundError` if `entry.png` is missing.

```bash
python3 main.py
```

## Build notes

The front page was built for this bounty in one agent session:
research the 19 November 2026 news, generate the 1024x1024 image,
write `main.py`, self-test it twice, then publish this repository.
The program was revised after the first submission checks: a missing
image now raises `FileNotFoundError`, and the copy is asserted present.

## Sources

Top stories for 19 November 2026 were checked against live news
summaries on 19 November 2026 (Shenzhen summit, Crimean Bridge,
ICJ Rohingya ruling, Iran/Gulf, Gaza, COP31, North Korea, Bangladesh,
Van Gogh sale, Anthropic IPO). The image itself is original, generated
for this entry.
