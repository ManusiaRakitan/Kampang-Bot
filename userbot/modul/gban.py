# Fixed by:koala @mixiologist
# Lord Userbot

from userbot import ALIVE_NAME, CMD_HELP
from telethon.tl.functions.contacts import BlockRequest, UnblockRequest
from userbot.events import register
from telethon.tl.types import MessageEntityMentionName


async def get_full_user(event):
    args = event.pattern_match.group(1).split(':', 1)
    extra = None
    if event.reply_to_msg_id and not len(args) == 2:
        previous_message = await event.get_reply_message()
        user_obj = await event.client.get_entity(previous_message.sender_id)
        extra = event.pattern_match.group(1)
    elif len(args[0]) > 0:
        user = args[0]
        if len(args) == 2:
            extra = args[1]
        if user.isnumeric():
            user = int(user)
        if not user:
            await event.edit("`Gabisa Tolol, Tanpa ID`")
            return
        if event.message.entities is not None:
            probable_user_mention_entity = event.message.entities[0]
            if isinstance(probable_user_mention_entity,
                          MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                user_obj = await event.client.get_entity(user_id)
                return user_obj
        try:
            user_obj = await event.client.get_entity(user)
        except Exception as err:
            return await event.edit("`Wahh Ngebug Anjing... Mohon Lapor Ke Koala` @mixiologist", str(err))
    return user_obj, extra


async def get_user_from_id(user, event):
    if isinstance(user, str):
        user = int(user)
    try:
        user_obj = await event.client.get_entity(user)
    except (TypeError, ValueError) as err:
        await event.edit(str(err))
        return None
    return user_obj


@register(outgoing=True, pattern="^.gban(?: |$)(.*)")
async def gben(userbot):
    dc = userbot
    sender = await dc.get_sender()
    me = await dc.client.get_me()
    if not sender.id == me.id:
        dark = await dc.reply("`Kamu Harus Di Global Banned, Karena Kamu Jelek!`")
    else:
        dark = await dc.edit("`✒ Global Banned Jamet Segera Di Proses`")
    me = await userbot.client.get_me()
    await dark.edit(f"`✒ Terdeteksi Jamet, Rasakan Dibanned Secara Global Karena Lu Jamet Pantek`")
    my_mention = "[{}](tg://user?id={})".format(me.first_name, me.id)
    f"@{me.username}" if me.username else my_mention
    await userbot.get_chat()
    a = b = 0
    if userbot.is_private:
        user = userbot.chat
        reason = userbot.pattern_match.group(1)
    else:
        userbot.chat.title
    try:
        user, reason = await get_full_user(userbot)
    except BaseException:
        pass
    try:
        if not reason:
            reason = "Private"
    except BaseException:
        return await dark.edit(f"`Wah Ngebug Syalan 🔥`")
    if user:
        if user.id == 1073848376:
            return await dark.edit(
                f"`Lu Ga Bisa Gban Gua Sat, Makanya Harus Ganteng ⛔️`"
            )
        try:
            from userbot.modules.sql_helper.gmute_sql import gmute
        except BaseException:
            pass
        try:
            await userbot.client(BlockRequest(user))
        except BaseException:
            pass
        testuserbot = [
            d.entity.id
            for d in await userbot.client.get_dialogs()
            if (d.is_group or d.is_channel)
        ]
        for i in testuserbot:
            try:
                await userbot.client.edit_permissions(i, user, view_messages=False)
                a += 1
                await dark.edit(f"`✒ Global Banned Menyala Ganteng 🚫`")
            except BaseException:
                b += 1
    else:
        await dark.edit(f"`Balas Ke Pesan Ganteng`")
    try:
        if gmute(user.id) is False:
            return await dark.edit(f"**Syntax Error! Itu Pantek Udah Lu Gban Ganteng.**")
    except BaseException:
        pass
    return await dark.edit(
        f"** 🕵️ ANCIENT:** `{ALIVE_NAME}`\n**❂ Username:** [{user.first_name}](tg://user?id={user.id})\n**❂ Punishment:** `Global Banned`"
    )


@register(outgoing=True, pattern="^.ungban(?: |$)(.*)")
async def gunben(userbot):
    dc = userbot
    sender = await dc.get_sender()
    me = await dc.client.get_me()
    if not sender.id == me.id:
        dark = await dc.reply("`✒ Mengampuni Si Tolol Yang Meresahkan`")
    else:
        dark = await dc.edit("`✒ Mencabut Hukuman Sedang Di Proses`")
    me = await userbot.client.get_me()
    await dark.edit(f"`Pendosa Telah Di Ampuni, Lain Kali Jangan Sok Keras Ya PANTEKKK...`")
    my_mention = "[{}](tg://user?id={})".format(me.first_name, me.id)
    f"@{me.username}" if me.username else my_mention
    await userbot.get_chat()
    a = b = 0
    if userbot.is_private:
        user = userbot.chat
        reason = userbot.pattern_match.group(1)
    else:
        userbot.chat.title
    try:
        user, reason = await get_full_user(userbot)
    except BaseException:
        pass
    try:
        if not reason:
            reason = "Private"
    except BaseException:
        return await dark.edit("`Syntax Error Ganteng 🚫`")
    if user:
        if user.id == 1073848376:
            return await dark.edit("**Gua Kebal Kok, Makanya Ganteng Sayang...**")
        try:
            from userbot.modules.sql_helper.gmute_sql import ungmute
        except BaseException:
            pass
        try:
            await userbot.client(UnblockRequest(user))
        except BaseException:
            pass
        testuserbot = [
            d.entity.id
            for d in await userbot.client.get_dialogs()
            if (d.is_group or d.is_channel)
        ]
        for i in testuserbot:
            try:
                await userbot.client.edit_permissions(i, user, send_messages=True)
                a += 1
                await dark.edit(f"`✒ Pengampunan Buat Pendosa... Please Wait... `")
            except BaseException:
                b += 1
    else:
        await dark.edit("`Balas Pesannya GANTENG`")
    try:
        if ungmute(user.id) is False:
            return await dark.edit("**Sarap Lu? Diakan Ga Pernah Elu GBAN GANTENG.**")
    except BaseException:
        pass
    return await dark.edit(
        f"** 🕵️ ANCIENT:** `{ALIVE_NAME}`\n**❂ Username:** [{user.first_name}](tg://user?id={user.id})\n**❂ Pengampunan:** `Membatalkan Global Banned`"
    )


CMD_HELP.update({
    "gban": "\
`.gban`\
\nUsage: ✒ Melakukan Global Banned Untuk Jamet Tele Yang Mereshahkan.\
\n\n`.ungban`\
\nUsage: ✒ Mengampuni Jamet Pendosa"
})
