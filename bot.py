import discord
from discord.ext import commands
from transformers import pipeline
from config import TOKEN

# Initialize the Discord bot
bot = commands.Bot(command_prefix="!")

# Initialize the AI model (using a pre-trained Hugging Face model)
chatbot = pipeline("text-generation", model="gpt2")

@bot.event
async def on_ready():
    print(f'Bot is ready. Logged in as {bot.user}')

@bot.command(name='chat')
async def chat(ctx, *, message: str):
    response = chatbot(message, max_length=50)
    await ctx.send(response[0]['generated_text'])

# Run the bot
bot.run(TOKEN)
