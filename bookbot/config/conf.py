from dataclasses import dataclass
from environs import Env


@dataclass
class TgBot:
    token: str


@dataclass
class Config:
    tg_bot: TgBot


def load_conf(path: str | None = None) -> Config:
    env = Env()
    env.read_env(path)
    return Config(
        TgBot(
            env.str("BOT_TOKEN")
        )
    )
