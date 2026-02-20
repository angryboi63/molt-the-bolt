from cawdbot import CawdBot, MoltBot


def test_reply_with_text():
    bot = CawdBot()
    assert bot.reply("hello world") == "cawdbot [molt]: caw! hello world"


def test_reply_with_blank_text():
    bot = CawdBot()
    assert bot.reply("   ") == "cawdbot: caw?"


def test_alias_points_to_same_type():
    assert MoltBot is CawdBot
