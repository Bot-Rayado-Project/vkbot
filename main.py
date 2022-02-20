import entry
import routers
from utils.settings import settings

bot = entry.set_bot(settings.GET_API_TOKEN(), settings.GET_GROUP_ID())

bot.dispatcher.add_router(routers.schedule_router)
bot.dispatcher.add_router(routers.joke_router)
bot.dispatcher.add_router(routers.easter_egg_router)
bot.dispatcher.add_router(routers.geobot_router)
bot.dispatcher.add_router(routers.help_router)
bot.dispatcher.add_router(routers.menu_router)

bot.run_forever()
