""" from https://github.com/keithito/tacotron

Defines the set of symbols used in text input to the model.
"""

_pad = "_"
_punctuation = ";:,.!? "
_letters_ipa = [
    "a",
    "b",
    "d",
    "e",
    "f",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "s",
    "t",
    "u",
    "v",
    "w",
    "z",
    "æ",
    "ð",
    "ŋ",
    "ɑ",
    "ɔ",
    "ə",
    "ɚ",
    "ɛ",
    "ɡ",
    "ɪ",
    "ɹ",
    "ʃ",
    "ʊ",
    "ʌ",
    "ʒ",
    "ˈ",
    "ˌ",
    "͡",
    "θ",
]


# Export all symbols:
symbols = [_pad] + list(_punctuation) + _letters_ipa

# Special symbol ids
SPACE_ID = symbols.index(" ")
