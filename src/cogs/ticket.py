async def namesend(bot, content: str, channel):
  webook = await channel.create_webhook(name='Name')
  name = await bot.fetch_user(884220029867003916)
  await webook.send(content, avatar_url=name.avatar.url)
  await webook.delete()

import nextcord
class ticket_buttons(nextcord.ui.View):
  def __init__(self):
    super().__init__(timeout = None)
    self.value = None

  @nextcord.ui.button(label="ticket", style = nextcord.ButtonStyle.green)
  async def confirm(self, button : nextcord.ui.Button, interaction : nextcord.Interaction):
    view = cbtn()
    await interaction.response.send_message('Es-tu sure de vouloir faire cela?', view=view, ephemeral=True)
    await view.wait()

class cbtn(nextcord.ui.View):
  def __init__(self):
    super().__init__(timeout = None)
    self.value = None

  @nextcord.ui.button(label="Oui", style = nextcord.ButtonStyle.green)
  async def Oui(self, button : nextcord.ui.Button, interaction : nextcord.Interaction):
    for channel in interaction.guild.channels:
      if channel.name == f'ticket-{interaction.user.id}':
        await interaction.response.send_message(f'Tu as déja un ticket.\n{channel.mention}', ephemeral=True)
        return
    from data import category
    channel = await interaction.guild.create_text_channel(f'ticket-{interaction.user.id}', category=interaction.guild.get_channel(category[interaction.guild.id]))
    await channel.set_permissions(interaction.user, send_messages=True, read_messages=True)
    await interaction.response.edit_message(content=f'{channel.mention}', view=None)
    msg = await channel.send('@everyone')
    await msg.delete()
    await channel.send(embed=nextcord.Embed(title=f'Le staff sera bientot la {interaction.user.name} !', color = 0x2ecc71))

  @nextcord.ui.button(label="Non", style = nextcord.ButtonStyle.red)
  async def Non(self, button : nextcord.ui.Button, interaction : nextcord.Interaction):
    await interaction.response.edit_message(content="Demande annulée!", view=None)


async def ticket_send(s, channel_id: int):
  channel = s.get_channel(channel_id)
  await channel.purge(limit=2)
  view = ticket_buttons()
  await channel.send(embed=nextcord.Embed(title="Ticket", description='Veuillez cliquer sur le boutton "ticket" pour créer un ticket', color=0x3498db), view=view)
  await namesend(s, 'Veuillez prendre note que tout ticket inutile sera sanctionné.', channel)
  await view.wait()

from nextcord.ext import commands
import asyncio
class Ticket(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.Cog.listener('on_ready')
  async def Readye(self):
    from data import ticket
    task: list = []
    for i in ticket:
      task.append(asyncio.create_task(ticket_send(self.bot, i)))
    await task[0]

def setup(bot):
  bot.add_cog(Ticket(bot))
