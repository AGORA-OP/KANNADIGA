from telethon import functions
from telethon.errors import ChatSendInlineForbiddenError as noin
from telethon.errors.rpcerrorlist import BotInlineDisabledError as noinline
from telethon.errors.rpcerrorlist import BotMethodInvalidError as dedbot
from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot import CMD_LIST, bot
from userbot.Config import Config
from userbot.utils import admin_cmd, sudo_cmd

from . import *

mybot = Config.BOT_USERNAME
if mybot.startswith("@"):
    botname = mybot
else:
    botname = f"@{mybot}"

msg = f"""
**â đģđđđđđđđđĸ đ°đ đģđđđđđđąđđ â**

  âĸ        [âĨī¸ đđđđ âĨī¸](https://github.com/PROBOY-OP/LegendBot)
  âĸ        [âĻī¸ Deploy âĻī¸](https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2FPROBOY-OP%2FPRO-LEGENDBOT&template=https%3A%2F%2Fgithub.com%2FPROBOY-OP%2FPRO-LEGENDBOT)

  âĸ  ÂŠī¸ {Legend_channel} âĸ
"""


@bot.on(admin_cmd(pattern="repo$"))
@bot.on(sudo_cmd(pattern="repo$", allow_sudo=True))
async def repo(event):
    try:
        legend = await bot.inline_query(botname, "repo")
        await legend[0].click(event.chat_id)
        if event.sender_id == Pro_Userboy:
            await event.delete()
    except (noin, dedbot):
        await eor(event, msg)


@bot.on(admin_cmd(pattern="help ?(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="help ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    tgbotusername = botname
    chat = "@Botfather"
    if tgbotusername is not None:
        try:
            results = await event.client.inline_query(tgbotusername, "LEGENDBOT_help")
            await results[0].click(
                event.chat_id, reply_to=event.reply_to_msg_id, hide_via=True
            )
            await event.delete()
        except noinline:
            legend = await eor(
                event,
                "**Inline Mode is disabled.** \n__Turning it on, please wait for a minute...__",
            )
            async with bot.conversation(chat) as conv:
                try:
                    first = await conv.send_message("/setinline")
                    second = await conv.get_response()
                    third = await conv.send_message(tgbotusername)
                    fourth = await conv.get_response()
                    fifth = await conv.send_message(perf)
                    sixth = await conv.get_response()
                    await bot.send_read_acknowledge(conv.chat_id)
                except YouBlockedUserError:
                    return await legend.edit("Unblock @Botfather first.")
                await legend.edit(
                    f"**Turned On Inline Mode Successfully.** \n\nDo `{l1}op` again to get the help menu."
                )
            await bot.delete_messages(
                conv.chat_id,
                [first.id, second.id, third.id, fourth.id, fifth.id, sixth.id],
            )
    else:
        await eor(
            event,
            "**â ī¸ đ´đđđžđ !!** \nđŋđđđđđ đđ-đ˛đđđđ BOT_TOKEN & BOT_USERNAME on Heroku.",
        )


@bot.on(admin_cmd(pattern="op ?(.*)", outgoing=True))
async def yardim(event):
    if event.fwd_from:
        return
    tgbotusername = botname
    input_str = event.pattern_match.group(1)
    if tgbotusername is not None or LEGEND_input == "text":
        results = await event.client.inline_query(tgbotusername, "PRO-LEGENDBOT_help")
        await results[0].click(
            event.chat_id, reply_to=event.reply_to_msg_id, hide_via=True
        )
        await event.delete()
    else:
        await eor(event, "**Check Bot Token And Bot Username In Reveal Var*")

        if input_str in CMD_LIST:
            string = "Commands found in {}:\n".format(input_str)
            for i in CMD_LIST[input_str]:
                string += "  " + i
                string += "\n"
            await event.edit(string)
        else:
            await event.edit(input_str + " is not a valid plugin!")


@bot.on(admin_cmd(pattern="ihelp(?: |$)(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="ihelp(?: |$)(.*)", allow_sudo=True))
async def LEGENDBOTt(event):
    if event.fwd_from:
        return
    args = event.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await eor(event, str(CMD_HELP[args]))
        else:
            await eor(event, "**â ī¸Sorry !** \nPlugin đđđđ đđ đđđđ  đđđđđđ đđđđ")
    else:
        string = ""
        sayfa = [
            sorted(list(CMD_HELP))[i : i + 5]
            for i in range(0, len(sorted(list(CMD_HELP))), 5)
        ]

        for i in sayfa:
            string += f"`đ`"
            for sira, a in enumerate(i):
                string += "`" + str(a)
                if sira == i.index(i[-1]):
                    string += "`"
                else:
                    string += "`, "
            string += "\n"
        await eor(
            event,
            "Please Specify A Module Name Of Which You Want Info" + "\n\n" + string,
        )


@borg.on(admin_cmd(pattern="config"))  # pylint:disable=E0602
async def _(event):

    if event.fwd_from:

        return

    result = await borg(functions.help.GetConfigRequest())  # pylint:disable=E0602

    result = result.stringify()

    logger.info(result)  # pylint:disable=E0602

    await event.edit("ŅŅâŅŅĐŊĪÎˇ  Đ˛ÎąŅŅâ ĪŅŅŅĐ˛ĪŅ ĪĪĪŅŅŅâ Đ˛Ņ **LÃĒÉ ÃĒÉŗĖdáēÃ¸â ** Đ˛ĪŅ")


CmdHelp("helper").add_command("repo", None, "To Get Repo And Repl Link").add_command(
    "help", None, "To Get Help Menu"
).add_command(
    "op", "<plugin name>", "To Get Detail About Plugin", "op alive"
).add_command(
    "ihelp", "<Pluggin Name>", "To get detail about any plugin"
).add()
