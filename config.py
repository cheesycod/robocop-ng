import hashlib
import datetime

# Basic bot config, insert your token here, update description if you want
prefixes = ["robo:"]
token = "token-goes-here"
bot_description = "Robocop-NG, the moderation bot of SecureChat"

# If you forked robocop-ng, put your repo here
source_url = "https://github.com/cheesycod/robocop-ng"
rules_url = "https://reswitched.team/discord/#rules"

# The bot description to be used in .robocop embed
embed_desc = (
    "Robocop-NG is developed by [Ave](https://github.com/aveao)"
    " and [tomGER](https://github.com/tumGER), and is a rewrite "
    "of Robocop.\nRobocop is based on Kurisu by 916253 and ihaveamac."
)


# The cogs the bot will load on startup.
initial_cogs = [
    "cogs.common",
    "cogs.admin",
    "cogs.verification",
    "cogs.mod",
    "cogs.mod_note",
    "cogs.mod_reacts",
    "cogs.mod_userlog",
    "cogs.mod_timed",
    "cogs.mod_watch",
    "cogs.basic",
    "cogs.logs",
    "cogs.err",
    "cogs.lockdown",
    "cogs.legacy",
    "cogs.remind",
    "cogs.robocronp",
    "cogs.meme",
    "cogs.invites",
    "cogs.pin"
]

# The following cogs are also available but aren't loaded by default:
# cogs.imagemanip - Adds a meme command called .cox.
# Requires Pillow to be installed with pip.
# cogs.lists - Allows managing list channels (rules, FAQ) easily through the bot


# Minimum account age required to join the guild
# If user's account creation is shorter than the time delta given here
# then user will be kicked and informed
min_age = datetime.timedelta(minutes=5)

# The bot will only work in these guilds
guild_whitelist = [718563359179669587]  # SecureChat discord

# Named roles to be used with .approve and .revoke
# Example: .approve User hacker
named_roles = {
    "god": 719797799381762049,
    "immortal god": 719798012938944572,
}

# The bot manager and staff roles
# Bot manager can run eval, exit and other destructive commands
# Staff can run administrative commands
bot_manager_role_id = 721074861203783801 # Bot management role in SecureChat (Owner)
staff_role_ids = [
    718564387362701352,  # Co-owner role in SecureChat
    721074861203783801,  # Bot management role in SecureChat
    360138163156549632,  # Admin role in SecureChat
]

# Various log channels used to log bot and guild's activity
# You can use same channel for multiple log types
# Spylog channel logs suspicious messages or messages by members under watch
# Invites created with .invite will direct to the welcome channel.
log_channel = 721077211075182623  # server-logs in ReSwitched
botlog_channel = 721077032909275137  # bot-logs channel in ReSwitched
modlog_channel = 721077128988196954  # mod-logs channel in ReSwitched
spylog_channel = 721076594440929392  # spy channel in ReSwitched
welcome_channel = 718742612688896021  # welcome channel in ReSwitched
general_channels = []
community_channels = []
# Controls which roles are blocked during lockdown
# Mute role is applied to users when they're muted
# As we no longer have mute role on ReSwitched, I set it to 0 here
mute_role = 718587078455197696  # Mute role in ReSwitched

# Channels that will be cleaned every minute/hour.
# This feature isn't very good rn.
# See https://github.com/reswitched/robocop-ng/issues/23
minutely_clean_channels = []
hourly_clean_channels = []

# Edited and deletes messages in these channels will be logged
spy_channels = general_channels

# All lower case, no spaces, nothing non-alphanumeric
suspect_words = [
    "marijuana" # Illegal
    "porn" # NSFW
    "pornography" # NSFW
    "child porn" # NSFW
    "child pornography" # NSFW
]

# List of words that will be ignored if they match one of the
# suspect_words (This is used to remove false positives)
suspect_ignored_words = [
]

# == For cogs.links ==
links_guide_text = """**Generic starter guides:**
Nintendo Homebrew's Guide: <https://nh-server.github.io/switch-guide/>

**Specific guides:**
Manually Updating/Downgrading (with HOS): <https://switch.homebrew.guide/usingcfw/manualupgrade>
Manually Repairing/Downgrading (without HOS): <https://switch.homebrew.guide/usingcfw/manualchoiupgrade>
How to set up a Homebrew development environment: <https://devkitpro.org/wiki/Getting_Started>
Getting full RAM in homebrew without NSPs: As of Atmosphere 0.8.6, hold R while opening any game.
Check if a switch is vulnerable to RCM through serial: <https://akdm.github.io/ssnc/checker/>
"""

# == For cogs.verification ==
# ReSwitched verification system is rather unique.
# You might want to reimplement it.
# If you do, use a different name for easier upstream merge.

# https://docs.python.org/3.7/library/hashlib.html#shake-variable-length-digests
_welcome_blacklisted_hashes = {"shake_128", "shake_256"}

# List of hashes that are to be used during verification
welcome_hashes = tuple(hashlib.algorithms_guaranteed - _welcome_blacklisted_hashes)

# Header before rules in #newcomers - https://elixi.re/i/opviq90y.png
welcome_header = """
    Hi there. This server is protected by Robocop. Please either verify or DM an admin to consent please!
    """

# Rules in #newcomers - https://elixi.re/i/dp3enq5i.png
welcome_rules = (
    """
    As we all know, every server has rules and this one does too:
    Ignorance of the rules does not justify breaking them
    1) No being annoying in general. Breaking this may result in getting the Duck role. If you have the duck role, you are liable to extra punishment
    2) Follow Discord ToS. Note that discussion of piracy is allowed however sharing of pirated content is not allowed whatsoever
    3) No off topic conversation
    4) Ask questions about the rules to a mod please
    If you agree to the rules, type "I consent" in #consent and we will let you in
    Remember to respect each others opinions
    Also about rp: You may only do one rp per day. Once your character has died, it is dead forever. You may only kill 3 cats per day. No mass killings are allowed without the mods permission. You are liable to be muted for breaking these rules. All roleplays are continuous. You may be in only one rp at one time. Contact an admin/co-owner/owner (me) if you want to start a roleplay. 
    NOTE: By one rp, I mean you can only join one rp per day
    The following things are considered NSFW and are not allowed
    > Porn
    > Gore (includes suicide, but not someone needing support, just photos of someone killing themself)
    > Anything that's overly cursed like what makes you unable to sleep for a week
    That's about it.
    Everything else is cool. Just ignore the old NSFW rules
    It is not allowed to advertise discord servers unless it is in #invite. Once again, please DM me if you want the role
    NOTE: If you get 20 warnings over a period of 2 days, you will be muted
    If you do not like someone, do not be rude about them
    Homophobic/anti-LGBTQ+/other sorts of comments is not allowed here whatsoever
    Please be polite to other people and don't use a lot of slurs
    No drama whatsoever. Keep that to private groups and DM's. Failing to follow this will result in a warn, mute, kick or even a permanent ban
    NSFW is NOT permitted
    """
)


# Footer after rules in #newcomers - https://elixi.re/i/uhfiecib.png
welcome_footer = (
    """
    **Note: This channel is completely automated (aside from responding to questions about the rules). If your message didn't give you access to the other channels, you failed the test. Feel free to try again or DM an admin/staff**
    """,
)

# Line to be hidden in rules
hidden_term_line = ' • When you have finished reading all of the rules, send a message in this channel that includes the {0} hex digest of your discord "name#discriminator", and bot will automatically grant you access to the other channels. You can find your "name#discriminator" (your username followed by a ‘#’ and four numbers) under the discord channel list. Look up hex digest online for more info or ask a mod to verify you!'

# == Only if you want to use cogs.pin ==
# Used for the pinboard. Leave empty if you don't wish for a gist pinboard.
github_oauth_token = ""

# Channels and roles where users can pin messages
allowed_pin_channels = []
allowed_pin_roles = []

# Channel to upload text files while editing list items. (They are cleaned up.)
list_files_channel = 0

# == Only if you want to use cogs.lists ==
# Channels that are lists that are controlled by the lists cog.
list_channels = []

# == Only if you want to use cogs.sar ==
self_assignable_roles = {
}
