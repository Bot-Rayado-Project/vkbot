from entry import InitializeComponent
import routers
from utils.terminal_codes import print_info

routers_list: list = [routers.schedule_router, routers.joke_router,
                      routers.easter_egg_router, routers.geobot_router,
                      routers.help_router, routers.menu_router, routers.aliases_router]

print_info("Waiting for application startup.")
bot = InitializeComponent()

for router in routers_list:
    bot.dispatcher.add_router(router)
print_info("Application startup complete.")
print_info("Started listening for messages...")

bot.run_forever()
