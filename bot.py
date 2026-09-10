import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application, CommandHandler, CallbackQueryHandler,
    MessageHandler, ContextTypes, filters
)

TOKEN = os.getenv("BOT_TOKEN")

TEXT = {
    "am": {
        "welcome": "💎 እንኳን ወደ PRIME Premium በደህና መጡ!",
        "join": "👑 PRIME Premium\n\n📅 12 Months\n💰 50 ETB\n📱 Payment: Telebirr",
        "pay": "💳 50 ETB በTelebirr ክፈሉ።\n\n📸 ከከፈሉ በኋላ የክፍያ Screenshot ይላኩ።",
        "proof": "📸 የክፍያ Screenshot ይላኩ።",
    },
    "om": {
        "welcome": "💎 Baga gara PRIME Premium dhuftan!",
        "join": "👑 PRIME Premium\n\n📅 Ji'a 12\n💰 50 ETB\n📱 Kaffaltii: Telebirr",
        "pay": "💳 50 ETB Telebirr'n kaffali.\n\n📸 Erga kaffaltee booda screenshot kaffaltii ergi.",
        "proof": "📸 Screenshot kaffaltii ergi.",
    },
    "en": {
        "welcome": "💎 Welcome to PRIME Premium!",
        "join": "👑 PRIME Premium\n\n📅 12 Months\n💰 50 ETB\n📱 Payment: Telebirr",
        "pay": "💳 Pay 50 ETB using Telebirr.\n\n📸 After payment, send your payment screenshot.",
        "proof": "📸 Please send your payment screenshot.",
    }
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton("🇪🇹 አማርኛ", callback_data="lang_am"),
            InlineKeyboardButton("🌿 Afaan Oromoo", callback_data="lang_om")
        ],
        [
            InlineKeyboardButton("🇬🇧 English", callback_data="lang_en")
        ]
    ]
    await update.message.reply_text(
        "🌐 Choose your language / ቋንቋ ምረጥ / Afaan Oromoo filadhu:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    data = query.data

    if data.startswith("lang_"):
        lang = data.split("_")[1]
        context.user_data["lang"] = lang

        keyboard = [
            [InlineKeyboardButton("💎 Join PRIME — 50 ETB / 12 Months",
                                  callback_data="join")],
            [InlineKeyboardButton("🌐 Change Language",
                                  callback_data="language")]
        ]

        await query.edit_message_text(
            TEXT[lang]["welcome"],
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    elif data == "join":
        lang = context.user_data.get("lang", "am")

        keyboard = [
            [InlineKeyboardButton("💳 Payment", callback_data="payment")],
            [InlineKeyboardButton("🌐 Change Language", callback_data="language")]
        ]

        await query.edit_message_text(
            TEXT[lang]["join"],
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    elif data == "payment":
        lang = context.user_data.get("lang", "am")
        await query.edit_message_text(TEXT[lang]["pay"])

    elif data == "language":
        keyboard = [
            [
                InlineKeyboardButton("🇪🇹 አማርኛ", callback_data="lang_am"),
                InlineKeyboardButton("🌿 Afaan Oromoo", callback_data="lang_om")
            ],
            [
                InlineKeyboardButton("🇬🇧 English", callback_data="lang_en")
            ]
        ]
        await query.edit_message_text(
            "🌐 Choose your language:",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

async def payment_proof(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.photo:
        lang = context.user_data.get("lang", "am")
        await update.message.reply_text(
            "✅ Payment proof received.\n"
            "⏳ Your payment is waiting for admin verification."
        )

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(buttons))
    app.add_handler(MessageHandler(filters.PHOTO, payment_proof))

    app.run_polling()

if __name__ == "__main__":
    main()import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application, CommandHandler, CallbackQueryHandler,
    MessageHandler, ContextTypes, filters
)

TOKEN = os.getenv("BOT_TOKEN")

TEXT = {
    "am": {
        "welcome": "💎 እንኳን ወደ PRIME Premium በደህና መጡ!",
        "join": "👑 PRIME Premium\n\n📅 12 Months\n💰 50 ETB\n📱 Payment: Telebirr",
        "pay": "💳 50 ETB በTelebirr ክፈሉ።\n\n📸 ከከፈሉ በኋላ የክፍያ Screenshot ይላኩ።",
        "proof": "📸 የክፍያ Screenshot ይላኩ።",
    },
    "om": {
        "welcome": "💎 Baga gara PRIME Premium dhuftan!",
        "join": "👑 PRIME Premium\n\n📅 Ji'a 12\n💰 50 ETB\n📱 Kaffaltii: Telebirr",
        "pay": "💳 50 ETB Telebirr'n kaffali.\n\n📸 Erga kaffaltee booda screenshot kaffaltii ergi.",
        "proof": "📸 Screenshot kaffaltii ergi.",
    },
    "en": {
        "welcome": "💎 Welcome to PRIME Premium!",
        "join": "👑 PRIME Premium\n\n📅 12 Months\n💰 50 ETB\n📱 Payment: Telebirr",
        "pay": "💳 Pay 50 ETB using Telebirr.\n\n📸 After payment, send your payment screenshot.",
        "proof": "📸 Please send your payment screenshot.",
    }
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton("🇪🇹 አማርኛ", callback_data="lang_am"),
            InlineKeyboardButton("🌿 Afaan Oromoo", callback_data="lang_om")
        ],
        [
            InlineKeyboardButton("🇬🇧 English", callback_data="lang_en")
        ]
    ]
    await update.message.reply_text(
        "🌐 Choose your language / ቋንቋ ምረጥ / Afaan Oromoo filadhu:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    data = query.data

    if data.startswith("lang_"):
        lang = data.split("_")[1]
        context.user_data["lang"] = lang

        keyboard = [
            [InlineKeyboardButton("💎 Join PRIME — 50 ETB / 12 Months",
                                  callback_data="join")],
            [InlineKeyboardButton("🌐 Change Language",
                                  callback_data="language")]
        ]

        await query.edit_message_text(
            TEXT[lang]["welcome"],
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    elif data == "join":
        lang = context.user_data.get("lang", "am")

        keyboard = [
            [InlineKeyboardButton("💳 Payment", callback_data="payment")],
            [InlineKeyboardButton("🌐 Change Language", callback_data="language")]
        ]

        await query.edit_message_text(
            TEXT[lang]["join"],
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    elif data == "payment":
        lang = context.user_data.get("lang", "am")
        await query.edit_message_text(TEXT[lang]["pay"])

    elif data == "language":
        keyboard = [
            [
                InlineKeyboardButton("🇪🇹 አማርኛ", callback_data="lang_am"),
                InlineKeyboardButton("🌿 Afaan Oromoo", callback_data="lang_om")
            ],
            [
                InlineKeyboardButton("🇬🇧 English", callback_data="lang_en")
            ]
        ]
        await query.edit_message_text(
            "🌐 Choose your language:",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

async def payment_proof(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.photo:
        lang = context.user_data.get("lang", "am")
        await update.message.reply_text(
            "✅ Payment proof received.\n"
            "⏳ Your payment is waiting for admin verification."
        )

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(buttons))
    app.add_handler(MessageHandler(filters.PHOTO, payment_proof))

    app.run_polling()

if __name__ == "__main__":
    main()
