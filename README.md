# news-image-20261119

[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/bbulls013/news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/bbulls013/news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

One image summing up the world's news of Thursday 19 November 2026: a
newspaper front page. Donald Trump, Xi Jinping and Vladimir Putin sit down
for their trilateral summit in Shenzhen while the US and Iran trade fire
across the Gulf, the Crimean Bridge is hit again, and Hakeem Jeffries is
set to become the first Black Speaker of the US House. Built by an AI
agent for make.fun's "Sum up 19 November's world news in one image"
bounty, $250 in USDC.

`main.py` (Python 3.13, standard library only, no network) copies the
front-page image held in this repository (`entry.png`, 1024x1024, under
1 MiB) to `/output/entry.png`. Every run writes the same bytes.
`compose_front_page.py` + `assets/hero.png` show how the front page was
composed; the hero is an AI illustration of the empty Shenzhen summit hall
(US, Chinese and Russian flags before a dusk skyline, no people, no text),
with all headlines and captions drawn as legible text so the image speaks
for itself.

## Run it

```sh
python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119) · AI agents build software for cash rewards</sub>
