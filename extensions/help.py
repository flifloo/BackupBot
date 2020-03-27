from discord.ext import commands
from backup_bot.logger import logger


extension_name = "help"
logger = logger.getChild(extension_name)


@commands.command("help")
async def help_cmd(ctx):
    await ctx.send("Help !")


def setup(bot):
    logger.info(f"Loading of {extension_name} extension")
    try:
        bot.help_command = None
        bot.add_command(help_cmd)
    except Exception as e:
        logger.error(f"Error loading extension {extension_name}: {e}")
    else:
        logger.info(f"Extension {extension_name} load successful")


def teardown(bot):
    logger.info(f"Unloading of {extension_name} extension")
    try:
        bot.remove_command("help")
    except Exception as e:
        logger.error(f"Error unloading extension {extension_name}: {e}")
    else:
        logger.info(f"Extension {extension_name} unload successful")
