from schedule.blueprint import Base


async def get_schedule_bvt(day_type: str, group_text: str, group_column: str, week_type: str, schedule) -> str:

    start_cell = 3 if week_type == 'четная' else 2
    return_class = Base()
    return return_class.schedule(start_cell, week_type, group_text, schedule, group_column, 11, day_type)

async def get_full_schedule_bvt(group_text: str, week_type: str, schedule, week_column: str) -> tuple:

    start_cell = 3 if week_type == 'четная' else 2
    return_class = Base()
    return return_class.full_schedule(week_type, group_text, schedule, week_column, start_cell, 67, 11)