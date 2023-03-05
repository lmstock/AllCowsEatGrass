from PIL import Image

# change a 30X30 image to various sizes for image pools of different sized creatures
# add 30x30 pngs to the filenames in img_pool
# click go, hope for the best!
# make sure you are in game_imgs directory
# make sure to create all in pool

img_pool = [
    "cret1.png",
    "cret2.png",
    "cret3.png",
    "cret4.png",
    "cret5.png",
    "cret6.png",
    "cret7.png"
]

flor_pool = [
    "flor1.png",
    "flor2.png",
    "flor3.png",
    "flor4.png",
    "flor5.png",
    "flor6.png",
    "flor7.png"
]

sizes = {
    "tiny": 5,
    "small": 10,
    "medium": 15,
    "large": 20,
    "very_large": 25,
    "mega": 30
}

for file in flor_pool:
    for k,v in sizes.items():

        namestring = file.split(".")
        fname = namestring[0] + "_" + k + ".png"

        img = Image.open(file)
        r_img = img.resize((v,v))

        r_img.save(fname)


