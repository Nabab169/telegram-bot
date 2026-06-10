
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes
import os

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🎬 Watch Now", url="https://afterwardenthusiasmexclusive.com/kxqidvw1?key=49623694992f9f5a6513c05e64fe6d1d")],
        [InlineKeyboardButton("📢 Join Channel", url="https://t.me/new_viral_video12_2")]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "🔥 Welcome to Viral Video Zone\n\n🎥 Latest Viral Videos Available",
        reply_markup=reply_markup
    )

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

app.run_polling()
