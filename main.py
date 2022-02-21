import entry
import logging
import routers
from utils.settings import settings

logging.basicConfig(filename="logs.log", level=logging.ERROR)

bot = entry.InitializeComponent(settings.GET_ALL_VARIABLES())

print("\nAdding routers to dispatcher...")

bot.dispatcher.add_router(routers.schedule_router)
bot.dispatcher.add_router(routers.joke_router)
bot.dispatcher.add_router(routers.easter_egg_router)
bot.dispatcher.add_router(routers.geobot_router)
bot.dispatcher.add_router(routers.help_router)
bot.dispatcher.add_router(routers.menu_router)

print("\nRouters added. Initialization successful.")

bot.run_forever()
