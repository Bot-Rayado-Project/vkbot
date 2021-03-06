from bot import *

routers_list = [routers.priority_router, routers.help_router,
                routers.donate_router, routers.joke_router,
                routers.schedule_router, routers.edit_router,
                routers.edit_personal_router, routers.edit_headman_router,
                routers.blueprints_router, routers.menu_router]

bot = SimpleLongPollBot(TOKENS, GROUPID)

for router in routers_list:
    bot.dispatcher.add_router(router)

bot.run_forever()
