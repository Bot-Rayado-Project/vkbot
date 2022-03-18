from vkwave.types.bot_events import get_event_object
from vkwave.types.bot_events import MessageNewObject, MessagesMessage
from vkwave.types.objects import BaseBoolInt

event = get_event_object({'type': 'message_new',
                          'group_id': 210676188,
                          'object': MessageNewObject(
                              message=MessagesMessage(
                                  action=None,
                                  admin_author_id=None,
                                  attachments=[],
                                  conversation_message_id=2306,
                                  date=1647617617,
                                  deleted=None,
                                  from_id=210481885,
                                  fwd_messages=[],
                                  geo=None, id=3471,
                                  important=False,
                                  is_hidden=False,
                                  is_cropped=None,
                                  keyboard=None,
                                  members_count=None,
                                  out=BaseBoolInt.NO,
                                  payload=None,
                                  peer_id=210481885,
                                  random_id=0,
                                  ref=None,
                                  ref_source=None,
                                  reply_message=None,
                                  text="дима",
                                  update_time=None,
                                  was_listened=None,
                                  pinned_at=None
                              )
                          )
                          })
print(event)
