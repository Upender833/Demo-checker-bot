import time
import random
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = 8353804215:AAF6i8DPAZD7LzsSEUrTrRCz9HUEmAg1thE

credits = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    uid = update.effective_user.id
    credits[uid] = 10
    await update.message.reply_text(
        "Ram Ram bhai 🙏\n"
        "Checker Bot ON ✅\n\n"
        "Use:\n/chk card|mm|yy|cvc\n\n"
        "Example:\n/chk 4242424242424242|12|26|123"
    )

async def chk(update: Update, context: ContextTypes.DEFAULT_TYPE):
    uid = update.effective_user.id
    if credits.get(uid, 0) <= 0:
        await update.message.reply_text("❌ Credits khatam ho gaye bhai")
        return

    start_time = time.time()
    credits[uid] -= 1
    elapsed = round(time.time() - start_time, 2)

    await update.message.reply_text(
        f"💳 CHECK RESULT\n\n"
        f"Status: Working ✅\n"
        f"Gate: Demo Tool\n"
        f"Elapsed: {elapsed}s\n"
        f"Credits Left: {credits[uid]}"
    )

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("chk", chk))
app.run_polling()
