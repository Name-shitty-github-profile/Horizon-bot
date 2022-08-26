from nextcord.ext import commands
from data import staff
class Secu(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.Cog.listener('on_message')
  async def antipub(self, message):
    if message.author.id in staff: return
    if any(word in str(', '.join([str(p[0]).replace("_", " ").title() for p in message.author.guild_permissions if p[1]])).lower() for word in ['admin']): return
    if any(word in message.content.lower() for word in ['discord.gg/']) is False: return
    await message.delete()
    await message.author.send("Tu as essayer de faire ta pub sas autorisation !\nMessage\n```\n{message.content}\n```")

def setup(bot):
  bot.add_cog(Secu(bot))
