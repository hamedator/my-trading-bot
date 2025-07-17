# 🧠 My Trading Bot

A high-performance automated cryptocurrency trading bot built with Python.  
Designed for real-time trading on Binance with strategy modularity and scalability in mind.

---

## 🚀 Features

- ✅ Real-time market data via WebSockets
- ✅ Modular trading strategies (EMA, RSI, etc.)
- ✅ Auto logging system (`logger.py`)
- ✅ Configurable risk management
- ✅ Ready for backtesting and live trading

---

## ⚙️ Requirements

- Python 3.10+
- `requests`, `websockets`, `pandas`, `numpy`, etc.

To install:
```bash
pip install -r requirements.txt

📂 Project Structure

my-trading-bot/
│
├── main.py              # Entry point
├── logger.py            # Logging module
├── strategies/          # All trading strategies
├── utils/               # Helper functions
├── config.json          # API keys and configs
└── README.md            # Project documentation

🧪 How to Run

python main.py

(You’ll need to fill in your Binance API keys inside config.json.)
👨‍💻 Author

Made with 💻 by Hamed Ibrahim
📜 License

MIT License – free to use, modify, and distribute.
