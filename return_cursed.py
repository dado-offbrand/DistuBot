# -- <<< Imports >>> -- #
import random

# -- <<< Variables >>> -- #
cursed_facts = [
  "People who are allergic to cockroaches are also allergic to pre-ground coffee... There is no mistake here...", 
  "In most cases, everybody is an atheist until they clog the toilet in someone else's house.", 
  "A pigeon once shat it's own portrait on a leaf. Did Bob Ross come back as a bird?", 
  "Adult culture is spending your paycheck on the items your parents refused to buy for you as a kid",
  "Thanos couldn't snap with a metal glove on so he did the motion and then made the noise by clapping his ass at the same time",
  "A company that is called \"Eternal Reefs\" takes the corpses of humans and then turns them into coral",
  "Breathing is done automatically, but now that I mentioned this you have to do it manually for ~5 minutes."]

cursed_images = [
  "https://media.discordapp.net/attachments/809612785675272218/853371051647696896/image0.png?width=595&height=677",
  "https://media.discordapp.net/attachments/809612785675272218/853371066633027584/image0.png",
  "https://media.discordapp.net/attachments/809612785675272218/853371103254806548/image0.png",
  "https://media.discordapp.net/attachments/809612785675272218/853371146859053067/image0.png?width=566&height=676",
  "https://media.discordapp.net/attachments/809612785675272218/853371383630921778/image0.jpg",
  "https://media.discordapp.net/attachments/809612785675272218/853371337716138015/image0.png?width=610&height=677",
  "https://media.discordapp.net/attachments/809612785675272218/853371524236705802/image0.jpg"]

# -- <<< Function >>> -- #
def return_cursed_img():
  return random.choice(cursed_images)

def return_cursed_fact():
  return random.choice(cursed_facts)