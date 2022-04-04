from schedule.blueprint import get_full_schedule, get_schedule


async def get_schedule_bin(day_type: str, group_text: str, group_column: str, week_type: str, schedule) -> str:

    start_cell = 4 if week_type == 'четная' else 3
    return await get_schedule(start_cell, week_type, group_text, schedule, group_column, 11, day_type)

async def get_full_schedule_bin(group_text: str, week_type: str, schedule, week_column: str) -> tuple:

    start_cell = 4 if week_type == 'четная' else 3
    return await get_full_schedule(week_type, group_text, schedule, week_column, start_cell, 67, 11)