from vkwave.bots import SimpleBotEvent, PhotoUploader
from vkwave.bots.utils.uploaders import DocUploader


async def get_photo_from_link(event: SimpleBotEvent, *link: str) -> str:
    '''Скачивает картинку по ссылке '''
    if len(link) == 1:
        return await PhotoUploader(event.api_ctx).get_attachment_from_link(peer_id=event.object.object.message.peer_id, link=link[0])
    else:
        att = []
        for _ in range(len(*link)):
            att += [await PhotoUploader(event.api_ctx).get_attachment_from_link(peer_id=event.object.object.message.peer_id, link=link[_])]
        return tuple(att)


async def get_photo_from_path(event: SimpleBotEvent, *path: str) -> str:
    '''Скачивает картинку по пути '''
    if len(path) == 1:
        return await PhotoUploader(event.api_ctx).get_attachment_from_path(peer_id=event.object.object.message.peer_id, file_path=path[0])
    else:
        att = []
        for _ in range(len(path)):
            att += [await PhotoUploader(event.api_ctx).get_attachment_from_path(peer_id=event.object.object.message.peer_id, file_path=path[_])]
        return tuple(att)


async def get_file_from_path(event: SimpleBotEvent, file_name: str, *path: str) -> str:
    '''Прикрепляет файл по пути '''
    if len(path) == 1:
        return await DocUploader(event.api_ctx).get_attachment_from_path(peer_id=event.object.object.message.peer_id, file_path=path[0], title=file_name)
    else:
        att = []
        for _ in range(len(*path)):
            att += [await PhotoUploader(event.api_ctx).get_attachment_from_path(peer_id=event.object.object.message.peer_id, file_path=path[_], title=file_name)]
        return tuple(att)
