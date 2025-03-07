#imports
import discord
import random
import time

#redbot
from redbot.core import commands


class TroutSlap(commands.Cog):
    """Slaps user about with a large trout like it's 1995"""

    def get_users(self, bot, slapper, target):
        return {'id': bot.id, 'nick':bot.display_name, 'formatted': bot.mention}, {'id': slapper.id, 'nick': slapper.display_name, 'formatted':"<@{}>".format(slapper.id)}, {'id': target.id, 'nick': target.display_name, 'formatted': target.mention}


    @commands.command()
    async def troutslap(self, ctx, *, user: discord.Member):
        """Slaps targeted user about with a large trout"""

        bot, slapper, target = self.get_users(ctx.bot.user,
                                               ctx.message.author, user)

        diceroll = random.randint(0, 100)

        if target['id'] == bot['id']:

            first_message = '{} slaps {} around a bit with a large trout 🐟💥'.format(slapper['nick'], bot['nick'])
            second_message = 'Cmon {}, what did I do to you?'.format(slapper['nick']) #no, no, no don't slap the bot

        elif slapper['id'] == target['id']:

            first_message = '{} slaps themselves around a bit with a large trout 🐟💥'.format(slapper['formatted'])

            if diceroll > 89:
                second_message = '{}, are you ok? Why did you slap yourself?'.format(slapper['formatted'])

            elif diceroll >10:
                second_message = '{} stop hitting yourself!'.format(slapper['formatted'])

            else:
                second_message = '{} stop wasting good slappin fish!'.format(slapper['formatted'])

        else:

            first_message = '{} slaps {} around a bit with a large trout 🐟💥'.format(slapper['formatted'], target['formatted'])

            if diceroll > 89:
                second_message = '{} with the home run!, {} is outta there!'.format(slapper['formatted'], target['formatted'])

            elif diceroll > 10:
                second_message = '{} with the animal cruelty, and {} with the broken nose!!'.format(slapper['formatted'], target['formatted'])

            else:
                second_message = '{}, excuse me, this is a ✝️Christian Server✝️! No Violence!'.format(slapper['formatted'])

        await ctx.send(first_message)
        time.sleep(1)
        await ctx.send(second_message)
