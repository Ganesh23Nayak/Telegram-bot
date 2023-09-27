from typing import Final
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
)


TOKEN: Final = "Token_id"
BOT_USERNAME: Final = "@Bot_name"


# Creating a command for the startup
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        """Welcome ! 🤖

        To get started, simply type a command or ask a question, and I'll do my best to assist you. If you're not sure what to do, you can type '/help' to see a list of available commands.

        Feel free to explore and have a great time using our bot! If you have any questions or encounter any issues, don't hesitate to ask."""
    )


# Creating a command for Help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        """Need assistance? You've come to the right place! 🆘

            Here are some things I can help you with:

            /start: Know About

            /help: Assistant

            /custom: to be added

            /notes: Stay tuned

            To use any of these commands, simply type the command name in the chat, and I'll provide you with the information or perform the action you need.

            If you have specific questions or need further assistance, feel free to ask, and I'll be happy to help!"""
    )


# Creating a custom command
async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("This is a custom command")


async def notes(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Notes will be added soon")


# RESPONSES
def handle_response(text: str) -> str:
    processed: str = text.lower()

    if "hello" in processed:
        return "Hiii,cutie"

    if "i love you" in processed:
        return "I love you Too"

    if "Miss you" in processed:
        return "Miss you tooo"

    if "bye" in processed:
        return "Bye"

    return "I didnt get you"


# HANDLE MESSAGES
async def handle_msg(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg_type: str = update.message.chat.type  # identify group or private chat
    text: str = update.message.text  # the text recieve by the bot

    print(
        f'User({update.message.chat.id}) in {msg_type}: "{text}"'
    )  # this is used so that the bot does not unecessarilly respond in a group chat

    # check if the message is a group chat or no
    if msg_type == "group":
        if BOT_USERNAME in text:  # check if the bot exists in the group chat
            new_text: str = text.replace(
                BOT_USERNAME, ""
            ).strip()  # If bot exists then replace bot with empty string and strip is used to remove any extra white spaces
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)

    print("Bot:", response)
    await update.message.reply_text(response)


# HANDLE ERRORS
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"Update {update} caused error {context.error} ")


# Main function
if __name__ == "__main__":
    print("Initiating BOT...")
    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("custom", custom_command))
    app.add_handler(CommandHandler("notes", notes))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_msg))

    # Error handler
    app.add_error_handler(error)

    print("Polling...")
    app.run_polling(poll_interval=3)  # Checks every 3 seconds for new messages
