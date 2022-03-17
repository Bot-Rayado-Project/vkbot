import pytest

from schedule import sheethandler
import schedule


@pytest.mark.asyncio
async def test_schedule():
    await sheethandler.print_schedule("сегодня", "бвт2103", "123", 'следущая неделя')
