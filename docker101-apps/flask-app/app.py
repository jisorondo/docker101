from flask import Flask, render_template
import random

app = Flask(__name__)

# list of cat images
images = [
  "https://github.com/jisorondo/docker101/raw/main/gifs/Cat-Combing-Itself.gif",
  "https://github.com/jisorondo/docker101/raw/main/gifs/Cat-Hug.gif",
  "https://github.com/jisorondo/docker101/raw/main/gifs/Cat-Playing-Basketball.gif",
  "https://github.com/jisorondo/docker101/raw/main/gifs/Cat-Playing-Ping-Pong.gif",
  "https://github.com/jisorondo/docker101/raw/main/gifs/Cat-Using-Chopsticks.gif",
  "https://github.com/jisorondo/docker101/raw/main/gifs/Cat-Using-Computer.gif",
  "https://github.com/jisorondo/docker101/raw/main/gifs/Cat-Wearing-Glasses.gif",
  "https://github.com/jisorondo/docker101/raw/main/gifs/Cat-With-Beer.jpg",
  "https://github.com/jisorondo/docker101/raw/main/gifs/Cat-With-Teddy-Bear.gif",
  "https://github.com/jisorondo/docker101/raw/main/gifs/Cats-Sitting-Like-Human.gif",
  "https://github.com/jisorondo/docker101/raw/main/gifs/Cats-Wearing-Party-Hats.gif",
  "https://github.com/jisorondo/docker101/raw/main/gifs/Cats-using-iPad.gif"
]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
