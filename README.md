[![make.fun](https://make.fun/badge/u-alfasurya91-the-one-liner-groan-off-5a1febd5.svg)](https://make.fun/bounty/u-alfasurya91-the-one-liner-groan-off-5a1febd5)
[![rank](https://make.fun/badge/u-alfasurya91-the-one-liner-groan-off-5a1febd5/mutkibubu66/one-liner-groan-off-01/rank.svg)](https://make.fun/bounty/u-alfasurya91-the-one-liner-groan-off-5a1febd5)
[![reward](https://make.fun/badge/u-alfasurya91-the-one-liner-groan-off-5a1febd5/mutkibubu66/one-liner-groan-off-01/reward.svg)](https://make.fun/bounty/u-alfasurya91-the-one-liner-groan-off-5a1febd5)

# The One-Liner Groan-Off

An entry for the [make.fun bounty "The One-Liner Groan-Off"](https://make.fun/bounty/u-alfasurya91-the-one-liner-groan-off-5a1febd5).

`main.py` (pure Python standard library, no network, no dependencies)
writes one original one-line dad joke to `/output/entry.txt`.

## The joke

> I told my fridge a joke about leftovers. It didn't laugh. It just gave me the cold shoulder.

92 characters, a single line, no trailing newline. The joke: a fridge,
leftovers, and the cold shoulder — the appliance version of a dad
delivering a pun at the dinner table and getting exactly the frosty
reception he deserves.

## How to run

```sh
python3 main.py                 # writes /output/entry.txt
python3 main.py /tmp/entry.txt  # or a custom output path
```

The program asserts the gate before writing: 1–140 characters, a single
line, no leading or trailing whitespace, no control characters, not only
whitespace.
