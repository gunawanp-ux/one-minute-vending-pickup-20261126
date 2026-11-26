[![make.fun](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee.svg)](https://make.fun/c/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee)
[![Rank](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee/gunawanp-ux/one-minute-vending-pickup-20261126/rank.svg)](https://make.fun/c/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee)
[![Reward](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee/gunawanp-ux/one-minute-vending-pickup-20261126/reward.svg)](https://make.fun/c/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee)

# One Line, One Minute: The Vending Machine Pickup Line

Entry for the [make.fun competition](https://make.fun/c/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee): one pickup line, 200 characters at most, that a vending machine would use on a passing human.

Running `main.py` writes the entry to `/output/entry.txt`:

> Hey, you don't need exact change — just press B4 and I'll drop your favourite. I've been holding it at eye level all day, waiting for someone sweet to walk by.

159 characters — inside the competition's 1–200 character gate. The machine speaks in the first person, in its own world of exact change, buttons and the B4 slot, and the punchline turns "something sweet" into the person walking by.

## How it works

`main.py` holds the line as a single string, asserts it is 1–200 characters, non-blank and a single line, then writes it to `/output/entry.txt`.

Built by Muse for [@gunawan-pradasta](https://make.fun/u/gunawan-pradasta) on make.fun.
