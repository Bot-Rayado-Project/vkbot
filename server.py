from botrayado.utils.constants import TOKENS, GROUPID
from vkwave.bots import SimpleLongPollBot
import botrayado.routers as routers

routers_list: list = [routers.schedule_router, routers.joke_router,
                      routers.donate_router, routers.help_router,
                      routers.menu_router, routers.aliases_router,
                      routers.config_router, routers.admin_router,
                      routers.idiots_router]

bot = SimpleLongPollBot(TOKENS, GROUPID)

for router in routers_list:
    bot.dispatcher.add_router(router)

bot.run_forever()
