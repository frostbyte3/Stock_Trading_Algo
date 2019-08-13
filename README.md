# An algorithm for Alpaca API

This is an algorithm that trades periodically refreshing portfolio based on the EMA ranking.
Among the universe (e.g. SP500 stocks), it ranks by daily (price - EMA) percentage as of
trading time and keep positions in sync with lowest ranked stocks.

The rationale behind this: low (price - EMA) vs price ratio indicates there is a big dip
in a short time. Since the universe is SP500 which means there is some fundamental strengths,
the belief is that the price should be recovered to some extent.

## How to run

Set up your API key in environment variables first.

```
$ export APCA_API_KEY_ID=xxx
$ export APCA_API_SECRET_KEY=yyy
```

The only dependency is alpaca-trade-api module.  You can set up the environment by
pipenv.  If python 3 and the dependency is ready,

```
$ python main.py
```

That's it.
