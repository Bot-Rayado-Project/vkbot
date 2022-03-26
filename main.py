import routers

from entry import InitializeComponent

routers_list: list = [routers.schedule_router, routers.joke_router,
                      routers.easter_egg_router, routers.geobot_router,
                      routers.help_router, routers.menu_router,
                      routers.aliases_router, routers.config_router,
                      routers.admin_router, routers.idiots_router]

bot = InitializeComponent(routers_list)
bot.run()
