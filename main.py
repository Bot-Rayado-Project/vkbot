from entry import InitializeComponent
import routers
from utils.terminal_codes import print_info

print_info("Waiting for application startup.")
bot = InitializeComponent()
bot.dispatcher.add_router(routers.schedule_router)
bot.dispatcher.add_router(routers.joke_router)
bot.dispatcher.add_router(routers.easter_egg_router)
bot.dispatcher.add_router(routers.geobot_router)
bot.dispatcher.add_router(routers.help_router)
bot.dispatcher.add_router(routers.menu_router)
print_info("Application startup complete.")
print_info("Started listening for messages...")

bot.run_forever()
