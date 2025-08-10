# Telegram ChatGPT Bot 🤖💬

A context-aware Telegram chatbot built using **Python** and **Aiogram**, integrated with **OpenAI's GPT-3.5 API**.  
The bot can hold natural conversations, remember previous responses during a session, and supports custom commands like `/start`, `/help`, and `/clear`.

---

## ✨ Features

- **Context memory** between messages using a simple in-memory store.
- `/clear` command to reset the conversation.
- Uses **ChatGPT 3.5** for realistic, context-aware replies.
- Built with **async/await** for fast, non-blocking I/O.
- Lightweight and easy to customize.

---

## 🛠 Tech Stack

- **Python 3.7**
- [aiogram](https://docs.aiogram.dev/) — Async Telegram Bot API framework
- [OpenAI API](https://platform.openai.com/)
- [python-dotenv](https://pypi.org/project/python-dotenv/) — Load environment variables from `.env`

---

## 📦 Installation

1. **Clone the repository**

git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>

2. **Install dependencies**

pip install -r requirements.txt

3. **Create a `.env` file**  
In the root folder, create a `.env` file with the following:


TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here
OPENAI_API_KEY=your_openai_api_key_here

🔑 **Where to get keys:**
- **Telegram Bot Token:** Create a bot using [@BotFather](https://t.me/BotFather) on Telegram.
- **OpenAI API Key:** Sign up at [OpenAI](https://platform.openai.com/) and generate an API key.

4. **Run the Bot  
- python main.py

## 💬 Usage

- Open Telegram and search for your bot (e.g. `@tele_1997_bot`).
- Start the conversation by typing `/start`.
- Use `/help` to see available commands.
- Type anything, and the bot will reply using ChatGPT 3.5.
- Use `/clear` to reset the chat memory.

---

## 📜 Commands

| Command   | Description          |
|-----------|----------------------|
| `/start`  | Start the bot         |
| `/help`   | Show help message     |
| `/clear`  | Clear chat history    |

---

## ⚠ Important Notes

- **API Keys:** Never commit your `.env` file to GitHub — add `.env` to `.gitignore`.
- **Billing:** Using the OpenAI API consumes your credits. For public deployment, restrict access or require users to bring their own API key.

---

## 🚀 Deployment (Optional)

This bot can be deployed to cloud services like:
- [Railway](https://railway.app/)
- [Render](https://render.com/)
- AWS EC2, Google Cloud Run, or Azure App Service

For production, you can:
- Switch to **webhooks** instead of polling for faster, more scalable operation.
- Restrict usage to specific Telegram IDs to prevent abuse.

---

## 🗺 Future Improvements

- Per-user conversation history
- Integration with image generation APIs
- Multi-language support
- Database storage for persistent memory

---

## 📄 License

This project is open source under the [MIT License](LICENSE).

---

## 🙌 Credits

- [Aiogram](https://docs.aiogram.dev/) — Telegram Bot API Framework
- [OpenAI API](https://platform.openai.com/) — GPT models


