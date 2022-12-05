import discord
import secret
import os

class DisplayBot(discord.Client):
    async def on_ready(self):
        self.takingImages = True
        self.command = "led-image-viewer"
        self.imageIsBeingDisplayed = False
        print("ONLINE")

    async def on_message(self, message):
        """
        Handles message input
        """
        if message.content == "!stop":
            await client.close()

        if message.content == "!close":
            self.takingImages = False
            await message.channel.send("Image submissions are closed!")

        if message.content == "!open":
            self.takingImages = True
            await message.channel.send("Image submissions are open!")

        if message.content == "!clear":
            if self.imageIsBeingDisplayed:
                os.system(f"/bin/kill -2 $(pidof {self.command}")
                await message.channel.send("64x64 LED Matrix has been successfully cleared!")

            else:
                await message.channel.send("Nothing is being displayed on the 64x64 LED Matrix")
        

if __name__ == "__main__":
    client = DisplayBot()
    client.run(secret.TOKEN)
