import telebot
import requests
import json


token = "TOKEN"


bot = telebot.TeleBot(token)


@bot.message_handler(["start"])
def start(message):
    bot.reply_to(
        message,
        """Welcome ! 🤖
        To get started, simply type a command or ask a question, and I'll do my best to assist you. If you're not sure what to do, you can type '/help' to see a list of available commands.
        Feel free to explore and have a great time using our bot! If you have any questions or encounter any issues, don't hesitate to ask.""",
    )


@bot.message_handler(["help"])
def start(message):
    bot.reply_to(
        message,
        """Need assistance? You've come to the right place! 🆘
            Here are some things I can help you with:
            /start: Know About
            /help: Assistant
            /caci:calculator
            /advice: free advice
            /joke: random jokes

            To use any of these commands, simply type the command name in the chat, and I'll provide you with the information or perform the action you need.
            If you have specific questions or need further assistance, feel free to ask, and I'll be happy to help!""",
    )


@bot.message_handler(["photo"])
def msg4(message):
    bot.reply_to(
        message,
        "https://unsplash.com/photos/the-sun-is-setting-over-a-mountain-range-T8c1yRB6dc0",
    )


@bot.message_handler(["joke"])
def msg4(message):
    url = "https://v2.jokeapi.dev/joke/Programming?format=txt"
    response = requests.get(url)
    if response.status_code == 200:
        bot.reply_to(message, response.text)
    else:
        bot.reply_to(
            message, f"Failed to retrieve the joke. Status code:{response.status_code}"
        )


@bot.message_handler(["advice"])
def msg4(message):
    url = "	https://api.adviceslip.com/advice"
    response = requests.get(url)
    data = json.loads(response.text)
    # print(data["slip"]["advice"])
    bot.reply_to(message, data["slip"]["advice"])


@bot.message_handler(["calci"])
def Welcome(pm):
    sent_msg = bot.send_message(
        pm.chat.id, "Welcome to Calculator. Enter the expression"
    )
    bot.register_next_step_handler(
        sent_msg, calculate
    )  # Next message will call the name_handler function


def calculate(pm):
    exp = pm.text
    ans = str(eval(exp))
    bot.send_message(pm.chat.id, f"{exp} = {ans}")


@bot.message_handler()
def greet(message):
    pattern = ["hello", "hi", "Good"]
    msg = (message.text.strip()).lower()
    t = 0
    for i in pattern:
        if i in msg:
            t = 1

    if t == 1:
        bot.reply_to(message, "Namaste 😊😊😊🙏")
    else:
        bot.reply_to(
            message, "https://apimeme.com/meme?meme=10-Guy&top=sorry&bottom=man"
        )


bot.polling()
