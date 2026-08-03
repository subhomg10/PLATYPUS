import discord
import discord_embeds as dce

class Buttons(discord.ui.View):
    def __init__(self, page1, page2, embedFxn, user, **embedArgs):
        super().__init__()
        self.page1 = page1
        self.page2 = page2
        self.embedFxn = embedFxn
        self.user = user
        self.embedArgs = embedArgs


    @discord.ui.button(label = "◀", style = discord.ButtonStyle.primary, disabled = True)
    async def previous(self, interaction: discord.Interaction, button: discord.ui.Button):
        if interaction.user != self.user:
            await interaction.response.send_message(
                "This pagination belongs to another user.",
                ephemeral=True
            )
            return
        args = self.embedArgs.copy()
        args['serial'] = 1
        embed = embed = self.embedFxn(self.page1, 1, 2, self.user, **args)

        for child in self.children:
            if child.label == "▶":
                child.disabled = False
            else:
                child.disabled = True

        await interaction.response.edit_message(embed = embed, view = self)

    @discord.ui.button(label = "▶", style = discord.ButtonStyle.primary, disabled = False)
    async def next(self, interaction: discord.Interaction, button: discord.ui.Button):
        if interaction.user != self.user:
            await interaction.response.send_message(
                "This pagination belongs to another user.",
                ephemeral=True
            )
            return
        args = self.embedArgs.copy()
        args['serial'] = 26
        embed = self.embedFxn(self.page2, 2, 2, self.user, **self.embedArgs)

        for child in self.children:
            if child.label == "◀":
                child.disabled = False
            else:
                child.disabled = True

        await interaction.response.edit_message(embed = embed, view = self)
        
class Ping(discord.ui.View):
    def __init__(self, latency):
        super().__init__()
        self.latency = latency
    @discord.ui.button(label = "Test Again", style = discord.ButtonStyle.primary)
    async def testAgain(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = dce.embed_ping(self.latency)
        await interaction.response.edit_message(embed = embed, view = self)
        