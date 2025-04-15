import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

# Token & Webhook
TOKEN = "8086056766:AAHts4apA7AUx4MatyTQfQnCLoYBOgWvHdA"
WEBHOOK_PATH = f"/webhook/{TOKEN}"
WEBHOOK_URL = f"https://bahi-bots-bot.onrender.com{WEBHOOK_PATH}"

# Logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

# Bot Commands
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"أهلًا {update.effective_user.first_name}! 👋\nمرحبًا بك في لعبة BAHI BOTS ⚙️")

async def click(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ نقرتك تم تسجيلها!")

# Main function
async def main():
    app = ApplicationBuilder().token(TOKEN).build()

    # Add command handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("click", click))

    # Set webhook
    await app.bot.set_webhook(WEBHOOK_URL)

    # Run webhook listener
    await app.start()
    await app.updater.start_webhook(
        listen="0.0.0.0",
        port=int(os.environ.get("PORT", 10000)),
        webhook_path=WEBHOOK_PATH,
    )

    print("🚀 Bahi Bots bot is live on Render!")
    await app.updater.idle()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
