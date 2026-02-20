"""CawdBot: a tiny local assistant helper.

The bot can be imported as `MoltBot` or `CawdBot`.
"""

from dataclasses import dataclass


@dataclass
class CawdBot:
    """Small bot with a branded response style."""

    name: str = "cawdbot"
    vibe: str = "molt"

    def reply(self, message: str) -> str:
        cleaned = " ".join(message.strip().split())
        if not cleaned:
            return f"{self.name}: caw?"
        return f"{self.name} [{self.vibe}]: caw! {cleaned}"


MoltBot = CawdBot


if __name__ == "__main__":
    import sys

    prompt = " ".join(sys.argv[1:])
    bot = CawdBot()
    print(bot.reply(prompt))
