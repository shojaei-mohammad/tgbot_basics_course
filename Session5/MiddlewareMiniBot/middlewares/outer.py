import logging
from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, User

logger = logging.getLogger(__name__)

baned_users = {"baned": [5977812305, 456]}


class FirstOuterMiddleware(BaseMiddleware):

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


class SecondOuterMiddleware(BaseMiddleware):

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


class ThirdOuterMiddleware(BaseMiddleware):

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


class ShadowBan(BaseMiddleware):

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any],
    ) -> Any:
        user: User = data["event_from_user"]
        if user.id in baned_users["baned"]:
            logger.info(f"User {user.id} has been shadow banned")
            return None
        return await handler(event, data)
