import logging
import logging.handlers
from botrayado.utils.constants import DEBUG, EADRESS, EPASSWORD

log_format = '%(asctime)s.%(msecs)03d %(filename)s:%(lineno)d %(levelname)s %(message)s'


def get_file_handler() -> logging.FileHandler:
    file_handler = logging.FileHandler("logs.log", encoding='UTF-8')
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(logging.Formatter(log_format))
    return file_handler


def get_smtp_handler() -> logging.handlers.SMTPHandler:
    smtp_handler = logging.handlers.SMTPHandler(mailhost=("smtp.gmail.com", 587),
                                                fromaddr=str(EADRESS),
                                                toaddrs=str(EADRESS),
                                                subject=u"VKbot error!",
                                                credentials=(str(EADRESS), str(EPASSWORD)),
                                                secure=())
    smtp_handler.setLevel(logging.ERROR)
    smtp_handler.setFormatter(logging.Formatter(log_format))
    return smtp_handler


def get_stream_handler() -> logging.StreamHandler:
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    stream_handler.setFormatter(logging.Formatter(log_format))
    return stream_handler


def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    if not DEBUG:
        logger.addHandler(get_smtp_handler())
    logger.addHandler(get_file_handler())
    logger.addHandler(get_stream_handler())
    return logger
