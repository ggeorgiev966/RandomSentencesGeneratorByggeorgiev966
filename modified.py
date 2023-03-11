import random

nicknames = ["Patrona", "Kirchandes", "Svet", "Jenuty", "Popa", "Nikito",
             "Kapitana", "Stoio", "Dedi", "Koska"]
map_names = ["Coastline", "Oregon", "Villa", "Chalet", "Bank", "Border", "Clubhouse",
        "Favela", "Kafe Dostoyevsky", "Consulate", "Fortress", "Kanal", "Outback", "Skyscraper", "Theme Park"]
verbs = ["runs", "hides", "shoots", "breaches", "drones", "reinforces", "sets traps", "holds", "throws",
         "peeks", "dropshots", "clutches", "downs", "dies", "kills", "pushes", "rushes"]
nouns = ["bomb", "opponent", "opponents", "gun", "trap", "window", "hatch", "room", "wall", "camera", "a drone",
         "friendly", "round"]
adverbs = ["slowly", "diligently", "clumsily", "sadly", "rapidly"]


def get_random_word(words):
    return random.choice(words)


def generate_sentence(nickname, map_name, verb, noun, adverb):
    if verb in ["downs", "dropshots", "kills", "peeks", "shoots"]:
        noun = random.choice(["opponent", "a friendly"])
    if noun == "gun":
        verb = "reloads"
    if noun == "a drone":
        verb = random.choice(["destroys", "throws", "shoots at"])
    if verb == "clutches":
        noun = "the round"
    if verb in ["runs", "hides", "dies"]:
        noun = random.choice(["near the bomb", "near the window", "at the window", "at the door", "in the room",
                                      "on site"])
    if verb in ["reinforces", "breaches"]:
        noun = random.choice(["wall", "hatch"])
    if verb == "sets traps":
        noun = ""
    return f"{nickname} on {map_name} {adverb} {verb} {noun}"


while True:
    random_nickname = get_random_word(nicknames)
    random_map = get_random_word(map_names)
    random_verb = get_random_word(verbs)
    random_noun = get_random_word(nouns)
    random_adverb = get_random_word(adverbs)
    sentence = generate_sentence(random_nickname, random_map, random_verb, random_noun, random_adverb)
    print(sentence)
    input("Click [Enter] to generate a new one.")
