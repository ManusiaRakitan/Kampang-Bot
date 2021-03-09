from time import sleep
from platform import uname
from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern='^kntl(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit(f"**LU KYK KONTOL**")
    sleep(3)
    await typew.edit("`KONTOL KONTOL LU KONTOL!!!`")
    sleep(3)
    await typew.edit("`DASAR LU KEPALA KONTOL!!!`")
# Owner @Si_Dian


@register(outgoing=True, pattern='^G(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit(f"**JAKA SEMBUNG BAWA GOLOK**")
    sleep(3)
    await typew.edit("`NIMBRUNG LAH GOBLOKK!!!`")
# Owner @Si_Dian


@register(outgoing=True, pattern='^.g(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit(f"**JAKA SEMBUNG BAWA GOLOK**")
    sleep(3)
    await typew.edit("`NIMBRUNG LAH GOBLOKK!!!`")
# Owner @Si_Dian


@register(outgoing=True, pattern='^P(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit(f"**Hallo PANTEK SAYA {DEFAULTUSER}**")
    sleep(2)
    await typew.edit("`LU KONTOLLL.....`")
# Owner @Si_Dian


@register(outgoing=True, pattern='^p(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit(f"**Hallo PANTEK SAYA {DEFAULTUSER}**")
    sleep(2)
    await typew.edit("`LU KONTOLLL.....`")
# Owner @Si_Dian


@register(outgoing=True, pattern='^L(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("`Astaghfirulloh kok anda berdosa sekali...`")
    sleep(1)
    await typew.edit("`Wa'allaikumussalam Sayang......`")
# Owner @Si_Dian


@register(outgoing=True, pattern='^l(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("`Astaghfirulloh kok anda berdosal sekali...`")
    sleep(1)
    await typew.edit("`Wa'allaikumussalam Sayang.....`")
# Owner @Si_Dian


CMD_HELP.update({
    "salam":
    "`P`\
\nUsage: Untuk Memberi Hujatan.\
\n\n`L`\
\nUsage: Untuk Menjawab Salam."
})
