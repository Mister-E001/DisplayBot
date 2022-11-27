import discord
import secret

class DisplayBot(discord.Client):
    async def on_ready(self):
        self.takingImages = True
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

        print(message.content)

        

if __name__ == "__main__":
    client = DisplayBot()
    client.run(secret.TOKEN)
