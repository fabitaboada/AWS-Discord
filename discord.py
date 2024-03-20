# importamos las librerias necesarias
from discord_webhook import DiscordWebhook, DiscordEmbed
import json
import requests

# Creamos el webhook y el embed, sustituyendo el enlace al webhook por el que hayamos creado en Discord
webhook = DiscordWebhook(url="https://discord.com/channels/846382262165569607/846382262610296862")

# Creamos el embed
embed = DiscordEmbed(
    # titulo, descripcion y color del embed
    title="RUST",
    description="RUST",
    color="03b2f8")

# Añadimos la imagen 
embed.set_image(url="https://files.facepunch.com/lewis/1b2411b1/og-image.jpg")
# Añadimos el embed al webhook
webhook.add_embed(embed)
# Ejecutamos el webhook, enviando el mensaje a Discord
webhook.execute()



def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Discord Lambda!')
    }