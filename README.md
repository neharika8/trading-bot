# Binance Futures Testnet Trading Bot

## Overview

A Python-based CLI trading bot for Binance Futures Testnet (USDT-M).

This application allows users to place:

- MARKET orders
- LIMIT orders

Supports:

- BUY orders
- SELL orders

Includes:

- CLI input validation
- Logging of requests and responses
- Error handling
- Modular code structure

---

## Project Structure

trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   └── logging_config.py
│
├── logs/
│   └── trading_bot.log
│
├── cli.py
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md

---

## Requirements

- Python 3.x
- Binance Futures Testnet account
- API Key and Secret from Binance Futures Testnet

---

## Setup Steps

### 1. Clone Repository

```bash
git clone https://github.com/neharika8/trading-bot.git
cd trading-bot
```

---

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Create Environment File

Create a `.env` file in the root folder.

Add:

```env
BINANCE_API_KEY=your_api_key
BINANCE_API_SECRET=your_api_secret
```

---

### 4. Register on Binance Futures Testnet

Visit:

https://testnet.binancefuture.com

Steps:

- Create account
- Generate API credentials
- Add test balance

---

## How to Run

### MARKET BUY Order

```bash
python cli.py --symbol ETHUSDT --side BUY --type MARKET --quantity 0.1
```

---

### MARKET SELL Order

```bash
python cli.py --symbol ETHUSDT --side SELL --type MARKET --quantity 0.1
```

---

### LIMIT BUY Order

```bash
python cli.py --symbol ETHUSDT --side BUY --type LIMIT --quantity 0.1 --price 2500
```

---

### LIMIT SELL Order

```bash
python cli.py --symbol ETHUSDT --side SELL --type LIMIT --quantity 0.1 --price 2500
```

---

## Features Implemented

### Order Types

- MARKET
- LIMIT

---

### Sides Supported

- BUY
- SELL

---

### Validation

Validates:

- Symbol input
- BUY / SELL side
- MARKET / LIMIT type
- Quantity > 0
- Price required for LIMIT orders

---

### Logging

Logs are stored in:

logs/trading_bot.log

Includes:

- API request logs
- API response logs
- Error logs

---

### Exception Handling

Handles:

- Invalid CLI input
- Binance API errors
- Network failures
- Unexpected runtime exceptions

---

## Assumptions

- User has valid Binance Futures Testnet account
- Testnet balance is available
- Binance Testnet execution behavior may differ from live exchange
- Internet connection is available

---

## Sample Output

### MARKET Order

- Order request summary
- Order response details
- Success / failure message

---

### LIMIT Order

- Order request summary
- Order response details
- Success / failure message

---

## Log File Submission

Repository includes log entries for:

- One MARKET order
- One LIMIT order
