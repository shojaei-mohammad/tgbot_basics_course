from dataclasses import dataclass

from environs import Env


@dataclass
class TgBot:
    token: str


@dataclass
class Config:
    tg_bot: TgBot


def laod_config(path: str | None = None):
    env: Env = Env()
    if path is not None:
        env.read_env(path)
    else:
        env.read_env()

    return Config(tg_bot=TgBot(token=env.str("TOKEN")))
