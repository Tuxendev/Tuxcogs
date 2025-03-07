from .troutslap import TroutSlap


async def setup(bot):
    await bot.add_cog(TroutSlap())