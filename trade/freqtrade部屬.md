<!--
 * @Author: error: git config user.name && git config user.email & please set dead value or install git
 * @Date: 2022-10-30 10:58:59
 * @LastEditors: error: git config user.name && git config user.email & please set dead value or install git
 * @LastEditTime: 2022-10-30 22:53:00
 * @FilePath: \筆記本\freqtrade部屬.md
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->

# Freqtrade 部屬教學 (雲端伺服器版)

## 0. 聲明

![vscode](https://badges.aleen42.com/src/visual_studio_code.svg)![python](https://badges.aleen42.com/src/python.svg)

```text
本教學的策略是出於教育目的，不構成任何投資建議。
USE THE SOFTWARE AT YOUR OWN RISK. THE AUTHORS AND ALL AFFILIATES ASSUME NO RESPONSIBILITY FOR YOUR TRADING RESULTS.
建議接觸過基礎python語法，和基礎linux指令。
```

## 1. 前言

本教學將會教你如何在雲端伺服器上部屬 Freqtrade，並且使用 Telegram Bot 和 Web UI 來控制 Freqtrade。</br>

## 2. 前置作業

### 2.1. 註冊 Telegram Bot

首先，我們需要先註冊一個 Telegram Bot，並且取得 Bot Token。

  1. 在 Telegram 上搜尋 [@BotFather](https://t.me/BotFather) 並且開始對話。
  2. 輸入 `/newbot` 並且按下 Enter。
  3. 輸入 Bot 名稱，並且按下 Enter。
  4. 輸入 Bot 帳號，並且按下 Enter。
  5. 複製 Bot Token，並且儲存起來，之後會用到。
  6. 按下 Bot 帳號，並且按下 Start 按鈕，開始對話。

### 2.2. 取得 Telegram user ID

接著，我們需要取得 Telegram user ID，並且儲存起來，之後會用到。

  1. 在 Telegram 上搜尋 [@userinfobot](https://t.me/userinfobot) 並且開始對話。
  2. 複製 user ID，並且儲存起來，之後會用到。

### 2.3. 建立雲端伺服器

接著，我們需要建立一個雲端伺服器，你可以選擇使用

- [![DigitalOcean](https://img.shields.io/badge/Digital_Ocean-0080FF?style=for-the-badge&logo=DigitalOcean&logoColor=white)](https://m.do.co/c/64da99d0346b)
- [![Linode](https://img.shields.io/badge/Linode-00A95C?style=for-the-badge&logo=Linode&logoColor=white)](https://www.linode.com/linuxexperiment)
- [![Vultr](https://img.shields.io/badge/Vultr-0078D7?style=for-the-badge&logo=Vultr&logoColor=white)](https://www.vultr.com/?ref=9273883-8H)
- [![GCP](https://img.shields.io/badge/Google_Cloud-4285F4?style=for-the-badge&logo=google-cloud&logoColor=white)](https://cloud.google.com/)
- [![AWS](https://img.shields.io/badge/Amazon_AWS-232F3E?style=for-the-badge&logo=amazon-aws&logoColor=white)](https://aws.amazon.com/)
- [![Azure](https://img.shields.io/badge/Microsoft_Azure-0089D6?style=for-the-badge&logo=microsoft-azure&logoColor=white)](https://azure.microsoft.com/)
- [![Heroku](https://img.shields.io/badge/Heroku-430098?style=for-the-badge&logo=heroku&logoColor=white)](https://www.heroku.com/)

以上的服務。

#### 機器規格

- CPU: 2 核心
- RAM: 4 GB
- SSD: 25 GB
- OS: Ubuntu 20.04 or Kali Linux

#### 防火牆設定

- 加上 PORT 8080 的防火牆規則 (可以改成其他的 PORT，但是之後要記得改)

### 2.4. 連線到雲端伺服器

接著，我們需要連線到雲端伺服器，如果你是用GCP或是AWS，可以使用 [Google Cloud Shell](https://cloud.google.com/shell) 或是 [AWS Cloud9](https://aws.amazon.com/tw/cloud9/) 來連線到雲端伺服器。

如果是其他的服務，可以使用 [Windows PowerShell](https://docs.microsoft.com/zh-tw/powershell/scripting/install/installing-powershell?view=powershell-7.1) 或是 [MacOS Terminal](https://support.apple.com/zh-tw/guide/terminal/welcome/mac) 來連線到雲端伺服器。

#### Example

![Linode](https://media.discordapp.net/attachments/868759966431973416/1036177566454775808/unknown.png)
![GCP](https://media.discordapp.net/attachments/868759966431973416/1036178787999698974/unknown.png)

#### Windows PowerShell

  1. 開啟 Windows PowerShell。
  2. 輸入 `ssh root@<IP Address>`，並且按下 Enter。
  3. 輸入密碼，並且按下 Enter。
  4. 連線成功。

#### Google Cloud Shell

  1. 開啟 Google Cloud Platform。
  2. 切換到Compute Engine 頁面。
  3. 選擇你的雲端伺服器。
  4. 選擇 SSH 按鈕。

#### MacOS Terminal

  1. 開啟 MacOS Terminal。
  2. 輸入 `ssh root@<IP Address>`，並且按下 Enter。
  3. 輸入密碼，並且按下 Enter。
  4. 連線成功。

## 3. 安裝Freqtrade

接著，我們需要安裝 Freqtrade。

#### 更新系統

  1. 輸入 `apt update`，並且按下 Enter。
  2. 輸入 `apt upgrade`，並且按下 Enter。
  3. 等待更新完成。

![apt update](https://media.discordapp.net/attachments/868759966431973416/1036181013023424562/unknown.png)

#### 安裝pip3

  1. 輸入 `apt install python3-pip`，並且按下 Enter。
  2. 等待安裝完成。

#### 安裝Freqtrade

```bash
git clone https://github.com/freqtrade/freqtrade.git
cd freqtrade
./setup.sh -i
```

接下來會自動安裝 Freqtrade，途中會詢問你是否安裝其他的套件，可以依照你的需求選擇。

- Reset git branch? (y/n)：選擇 n。
- Do you want to install dependencies for dev? (y/n)：選擇 n。
- Do you want to install plotting dependencies (plotly) ? (y/n)：選擇 y。
- Do you want to install hyperopt dependencies ? (y/n)：選擇 y。
- Do you want to install dependencies for freqai ? (y/n) : 選擇 y。

等待安裝完成。

#### Freqtrade 設定

接下來，我們需要設定 Freqtrade。

  1. 確認目前的目錄，並且進入freqtrade目錄。
  2. `source .env/bin/activate`，並且按下 Enter。
  3. `cd ..`，並且按下 Enter。
  4. `mkdir bot01`，並且按下 Enter。 (bot01 可以改成其他的名稱)
  5. `cd bot01`，並且按下 Enter。
  6. `freqtrade create-userdir --userdir user_data`，並且按下 Enter。
  7. `freqtrade new-config --config config.json`，並且按下 Enter。

按下 Enter 之後，會詢問一些設定，可以依照你的需求選擇，可以事後到 `config.json` 裡面修改。

![freqtrade new-config](https://media.discordapp.net/attachments/868759966431973416/1036188070757797918/unknown.png?width=1195&height=449)

![freqtrade new-config](https://media.discordapp.net/attachments/868759966431973416/1036187626308386816/unknown.png)

![freqtrade new-config](https://media.discordapp.net/attachments/868759966431973416/1036187418077970452/unknown.png)

#### 檢查
  
  1. `cd user_data`，並且按下 Enter。
  2. `ls`，並且按下 Enter。
  3. 確認是否有 `config.json`、`user_data` 這些資料夾，會呈現下方圖片的樣子。

![ls](https://media.discordapp.net/attachments/868759966431973416/1036189147871846480/unknown.png)

### 3.1. Freqtrade 基本操作

#### 查看可用的指令

  1. `freqtrade -h`，並且按下 Enter。
  2. 會出現下方圖片的樣子，可以看到可用的指令。

![freqtrade -h](https://media.discordapp.net/attachments/868759966431973416/1036189937516675144/unknown.png?width=843&height=658)

#### 查看可用的策略

  1. `freqtrade list-strategies`，並且按下 Enter。
  2. 會出現下方圖片的樣子，可以看到可用的策略，預設會有一個策略叫做 `SampleStrategy`。

![freqtrade list-strategies](https://media.discordapp.net/attachments/868759966431973416/1036190353134460958/unknown.png?width=1195&height=409)

#### 修改 config 檔案

  1. `vim config.json`，並且按下 Enter。
  
```json
"exchange": {
    "name": "binance",
    "key": "", 
    "secret": "",
    "ccxt_config": {},
    "ccxt_async_config": {},
    "pair_whitelist": [
        ""
    ],
    "pair_blacklist": [
        "BNB/.*"
    ]
},
```

  2. 將 `key` 跟 `secret` 是交易所的API，在真實運行的時候需要加上去，現在要修改 `"pair_whitelist"` 裡面的值。
  3. 按下 `i`，進入編輯模式。
  4. 將 `""` 改成你要交易的幣種，例如 `BTC/USDT`，範例如下。

```json
"exchange": {
    "name": "binance",
    "key": "", 
    "secret": "",
    "ccxt_config": {},
    "ccxt_async_config": {},
    "pair_whitelist": [
        "BTC/USDT"
    ],
    "pair_blacklist": [
        "BNB/.*"
    ]
},
```

  5. 按下 `Esc`，離開編輯模式。
  6. 按下 `:`，進入指令模式。
  7. 輸入 `wq`，並且按下 Enter。

***注意：*** </br>

- 如果你是用 `nano` 編輯器，請按下 `Ctrl + X`，然後按下 `Y`，最後按下 `Enter`。
- 如果你是用 `vim` 編輯器，請按下 `Esc`，然後按下 `:`，接著輸入 `wq`，最後按下 `Enter`。
- 如果想要了解更多關於 `config.json` 的設定，可以參考 [這裡](https://www.freqtrade.io/en/latest/configuration/)。


#### 下載歷史K線資料

  1. `freqtrade download-data -h`，並且按下 Enter。
  2. 會出現下方圖片的樣子，可以看到可用的參數。

![freqtrade download-data -h](https://media.discordapp.net/attachments/868759966431973416/1036191985616289813/unknown.png?width=982&height=658)
  
  3. `freqtrade download-data --days 30 -t 1m 5m 15m`，並且按下 Enter。(下載30天的1分鐘、5分鐘、15分鐘的K線資料，品種可以到`config.json`裡面修改)
  4. 會出現下方圖片的樣子，表示下載完成。

![freqtrade download-data --days 30 -t 1m 5m 15m](https://media.discordapp.net/attachments/868759966431973416/1036264886017208402/unknown.png?width=843&height=658)

#### 開始回測

  1. `freqtrade backtesting -h`，並且按下 Enter。
  2. 會出現下方圖片的樣子，可以看到可用的參數。

![freqtrade backtesting -h](https://media.discordapp.net/attachments/868759966431973416/1036265287969931336/unknown.png?width=921&height=658)

  3. `freqtrade backtesting -i 15m --fee 0.0004 -s SampleStrategy`，並且按下 Enter。(回測15分鐘的K線資料，手續費0.04%，策略是`SampleStrategy`，品種可以到`config.json`裡面修改)
  4. 會出現下方文字檔的樣子，表示回測完成。

```text
============================================================ BACKTESTING REPORT ============================================================
|     Pair |   Entries |   Avg Profit % |   Cum Profit % |   Tot Profit USDT |   Tot Profit % |     Avg Duration |   Win  Draw  Loss  Win% |
|----------+-----------+----------------+----------------+-------------------+----------------+------------------+-------------------------|
| BTC/USDT |         7 |           1.10 |           7.71 |            12.057 |           1.21 | 2 days, 11:51:00 |     7     0     0   100 |
|    TOTAL |         7 |           1.10 |           7.71 |            12.057 |           1.21 | 2 days, 11:51:00 |     7     0     0   100 |
============================================================ ENTER TAG STATS ============================================================
|   TAG |   Entries |   Avg Profit % |   Cum Profit % |   Tot Profit USDT |   Tot Profit % |     Avg Duration |   Win  Draw  Loss  Win% |
|-------+-----------+----------------+----------------+-------------------+----------------+------------------+-------------------------|
| TOTAL |         7 |           1.10 |           7.71 |            12.057 |           1.21 | 2 days, 11:51:00 |     7     0     0   100 |
===================================================== EXIT REASON STATS =====================================================
|   Exit Reason |   Exits |   Win  Draws  Loss  Win% |   Avg Profit % |   Cum Profit % |   Tot Profit USDT |   Tot Profit % |
|---------------+---------+--------------------------+----------------+----------------+-------------------+----------------|
|           roi |       7 |      7     0     0   100 |            1.1 |           7.71 |            12.057 |           7.71 |
======================================================= LEFT OPEN TRADES REPORT ========================================================
|   Pair |   Entries |   Avg Profit % |   Cum Profit % |   Tot Profit USDT |   Tot Profit % |   Avg Duration |   Win  Draw  Loss  Win% |
|--------+-----------+----------------+----------------+-------------------+----------------+----------------+-------------------------|
|  TOTAL |         0 |           0.00 |           0.00 |             0.000 |           0.00 |           0:00 |     0     0     0     0 |
===================== SUMMARY METRICS =====================
| Metric                      | Value                     |
|-----------------------------+---------------------------|
| Backtesting from            | 2022-09-30 07:30:00       |
| Backtesting to              | 2022-10-30 12:45:00       |
| Max open trades             | 1                         |
|                             |                           |
| Total/Daily Avg Trades      | 7 / 0.23                  |
| Starting balance            | 1000 USDT                 |
| Final balance               | 1012.057 USDT             |
| Absolute profit             | 12.057 USDT               |
| Total profit %              | 1.21%                     |
| CAGR %                      | 15.70%                    |
| Profit factor               | 0.00                      |
| Trades per day              | 0.23                      |
| Avg. daily profit %         | 0.04%                     |
| Avg. stake amount           | 156.612 USDT              |
| Total trade volume          | 1096.287 USDT             |
|                             |                           |
| Long / Short                | 6 / 1                     |
| Total profit Long %         | 1.05%                     |
| Total profit Short %        | 0.16%                     |
| Absolute profit Long        | 10.471 USDT               |
| Absolute profit Short       | 1.586 USDT                |
|                             |                           |
| Best Pair                   | BTC/USDT 7.71%            |
| Worst Pair                  | BTC/USDT 7.71%            |
| Best trade                  | BTC/USDT 2.00%            |
| Worst trade                 | BTC/USDT 0.87%            |
| Best day                    | 3.094 USDT                |
| Worst day                   | 0 USDT                    |
| Days win/draw/lose          | 6 / 23 / 0                |
| Avg. Duration Winners       | 2 days, 11:51:00          |
| Avg. Duration Loser         | 0:00:00                   |
| Rejected Entry signals      | 0                         |
| Entry/Exit Timeouts         | 0 / 0                     |
|                             |                           |
| Min balance                 | 0 USDT                    |
| Max balance                 | 0 USDT                    |
| Max % of account underwater | 0.00%                     |
| Absolute Drawdown (Account) | 0.00%                     |
| Absolute Drawdown           | 0 USDT                    |
| Drawdown high               | 0 USDT                    |
| Drawdown low                | 0 USDT                    |
| Drawdown Start              | 1970-01-01 00:00:00+00:00 |
| Drawdown End                | 1970-01-01 00:00:00+00:00 |
| Market change               | 6.07%                     |
===========================================================
```

#### 回測結果

  1. 回測結果會在`user_data/backtest_results`資料夾裡面，檔名會是`backtest-result-2021-10-30_12-45-00.json`。
  2. 用`freqtrade plot-profit -s SampleStrategy -i 15m`可以看到回測結果的圖表。

![img](https://media.discordapp.net/attachments/868759966431973416/1036267891311521935/unknown.png?width=1195&height=633)

  3. 下載產生的html檔案，用瀏覽器開啟，可以看到更詳細的回測結果。

> 可以使用 `scp` 指令將檔案下載到本機端，或是使用 `wget` 指令下載檔案。(wget 要更改防火牆設定)

```bash
# scp
scp -P 22 root@ip:/root/freqtrade/user_data/backtest_results/backtest-result-2021-10-30_12-45-00.html .
# wget
wget http://ip:8080/user_data/backtest_results/backtest-result-2021-10-30_12-45-00.html
#每個人的ip和結果會不一樣，請自行更改。
```

#### 部屬(dry-run)

  1. 輸入 `freqtrade trade -s SampleStrategy --dry-run --fee 0.0004`，開始部屬(dry-run)。(如果要讓他在背景執行就在最前面加入nohup，例如`nohup freqtrade trade -s SampleStrategy --dry-run --fee 0.0004`)
  2. 然後就可以到`http://ip:8080`看到部屬的結果了。 (ip和port要自行更改)
  3. 同時也可以在telegram上看到部屬的結果，如下圖。

![img](https://media.discordapp.net/attachments/868759966431973416/1036278648426221629/unknown.png)

#### 部屬(real)

  1. 先到`config.json`裡面，將`dry_run`改成`false`，並且把 `api_key` 和 `api_secret` 填上去。
  2. 輸入 `freqtrade trade -s SampleStrategy --fee 0.0004`，開始部屬(real)。
  3. 然後就可以到`http://ip:8080`看到部屬的結果了。 (ip和port要自行更改)
  4. 同時也可以在telegram上看到部屬的結果。

## 4. 策略

### 4.1 說明

請參考[官方文件](https://www.freqtrade.io/en/2019.9/strategy-customization/)。

### 4.2 範例

#### 4.2.1 範例1

```python
"""
author      = "Kevin Ossenbrück"
copyright   = "Free For Use"
credits     = ["Bloom Trading, Mohsen Hassan"]
license     = "MIT"
version     = "1.0"
maintainer  = "Kevin Ossenbrück"
email       = "kevin.ossenbrueck@pm.de"
status      = "Live"
"""

from freqtrade.strategy import IStrategy
from freqtrade.strategy import IntParameter
from functools import reduce
from pandas import DataFrame

import talib.abstract as ta
import freqtrade.vendor.qtpylib.indicators as qtpylib
import numpy


#這裡是策略使用的參數，可以自行調整。
# CCI timerperiods and values
cciBuyTP = 72
cciBuyVal = -175
cciSellTP = 66
cciSellVal = -106

# RSI timeperiods and values
rsiBuyTP = 36
rsiBuyVal = 90
rsiSellTP = 45
rsiSellVal = 88

#class 名稱要和檔案名稱一樣，並且繼承IStrategy。
class SwingHighToSky(IStrategy):
    INTERFACE_VERSION = 3 #這個不用改。

    timeframe = '15m' #這個是策略的時間區間。

    stoploss = -0.34338 #這個是策略的停損。

    minimal_roi = {"0": 0.27058, "33": 0.0853, "64": 0.04093, "244": 0} #這個是策略的ROI，可以隨著時間更改。

    #這是讓策略可以自動調整的參數，可以自行調整。--[start]--
    buy_cci = IntParameter(low=-200, high=200, default=100, space='buy', optimize=True)
    buy_cciTime = IntParameter(low=10, high=80, default=20, space='buy', optimize=True)
    buy_rsi = IntParameter(low=10, high=90, default=30, space='buy', optimize=True)
    buy_rsiTime = IntParameter(low=10, high=80, default=26, space='buy', optimize=True)

    sell_cci = IntParameter(low=-200, high=200, default=100, space='sell', optimize=True)
    sell_cciTime = IntParameter(low=10, high=80, default=20, space='sell', optimize=True)
    sell_rsi = IntParameter(low=10, high=90, default=30, space='sell', optimize=True)
    sell_rsiTime = IntParameter(low=10, high=80, default=26, space='sell', optimize=True)

    # Buy hyperspace params:
    buy_params = {
        "buy_cci": -175,
        "buy_cciTime": 72,
        "buy_rsi": 90,
        "buy_rsiTime": 36,
    }

    # Sell hyperspace params:
    sell_params = {
        "sell_cci": -106,
        "sell_cciTime": 66,
        "sell_rsi": 88,
        "sell_rsiTime": 45,
    }
    #這是讓策略可以自動調整的參數，可以自行調整。--[end]--

    def informative_pairs(self):
        return []

    def populate_indicators(self, dataframe: DataFrame, metadata: dict) -> DataFrame:#這個是計算指標的地方。

        for val in self.buy_cciTime.range:
            dataframe[f'cci-{val}'] = ta.CCI(dataframe, timeperiod=val)

        for val in self.sell_cciTime.range:
            dataframe[f'cci-sell-{val}'] = ta.CCI(dataframe, timeperiod=val)

        for val in self.buy_rsiTime.range:
            dataframe[f'rsi-{val}'] = ta.RSI(dataframe, timeperiod=val)

        for val in self.sell_rsiTime.range:
            dataframe[f'rsi-sell-{val}'] = ta.RSI(dataframe, timeperiod=val)

        return dataframe

    def populate_entry_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:#這個是計算買進的地方。

        dataframe.loc[
            (
                (dataframe[f'cci-{self.buy_cciTime.value}'] < self.buy_cci.value) &
                (dataframe[f'rsi-{self.buy_rsiTime.value}'] < self.buy_rsi.value)
            ),
            'enter_long'] = 1

        return dataframe

    def populate_exit_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:#這個是計算賣出的地方。

        dataframe.loc[
            (
                (dataframe[f'cci-sell-{self.sell_cciTime.value}'] > self.sell_cci.value) &
                (dataframe[f'rsi-sell-{self.sell_rsiTime.value}'] > self.sell_rsi.value)
            ),
            'exit_long'] = 1

        return dataframe
```

## 5. 策略優化

### 5.1 說明

請參考[官方文件](https://www.freqtrade.io/en/latest/hyperopt/)。</br>
由於策略優化需要大量的計算資源，所以建議加大虛擬機的資源，或是在本地端執行。</br>

### 5.2 執行

```bash
freqtrade hyperopt --hyperopt-loss SharpeHyperOptLoss --spaces buy sell --strategy SwingHighToSky --timerange 20210101-20210131
```

#### 5.2.1 說明

`--hyperopt-loss`：這裡是設定優化的損失函數，可以自行調整。</br>
`--spaces`：這裡是設定優化的參數，可以自行調整。</br>
`--strategy`：這裡是設定優化的策略，可以自行調整。</br>
`--timerange`：這裡是設定優化的時間範圍，可以自行調整。</br>

## 6. 總結

在這篇文章中，我們介紹了如何使用Freqtrade來進行策略的開發與優化，希望能夠幫助到大家。</br>
如果有任何問題，歡迎在下方留言，我會盡快回覆。</br>
如果覺得文章對你有幫助，歡迎餵食我一顆星星。</br>

## 7. 參考資料

[![frqtrade](https://img.shields.io/badge/freqtrade--44A833?style=plastic&logo=github)](https://github.com/freqtrade/freqtrade)</br>
[官方文件](https://www.freqtrade.io/en/latest/)</br>
[策略範例](https://github.com/freqtrade/freqtrade-strategies/blob/main/user_data/strategies/SwingHighToSky.py)</br>
