import logging
from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject

logger = logging.getLogger(__name__)


class FirstInnerMiddleware(BaseMiddleware):

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any],
    ) -> Any:

        logger.debug(
            "Entered middleware %s, event type %s",
            __class__.__name__,
            event.__class__.__name__,
        )

        result = await handler(event, data)

        logger.debug("Exiting middleware %s", __class__.__name__)

        return result


class SecondInnerMiddleware(BaseMiddleware):

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any],
    ) -> Any:

        logger.debug(
            "Entered middleware %s, event type %s",
            __class__.__name__,
            event.__class__.__name__,
        )

        result = await handler(event, data)

        logger.debug("Exiting middleware %s", __class__.__name__)

        return result


class ThirdInnerMiddleware(BaseMiddleware):

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any],
    ) -> Any:

        logger.debug(
            "Entered middleware %s, event type %s",
            __class__.__name__,
            event.__class__.__name__,
        )

        result = await handler(event, data)

        logger.debug("Exiting middleware %s", __class__.__name__)

        return result
