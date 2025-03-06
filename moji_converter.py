# MojiCune - An Emoji Alphabet Converter

moji_dict = {
    "A": "🔺",  # Triangle
    "B": "🅱",  # B emoji
    "C": "🌙",  # Crescent moon
    "D": "↩",  # Return arrow
    "E": "🎀",  # Ribbon emoji
    "F": "🚩",  # Flag emoji
    "G": "🌀",  # Swirl vortex
    "H": "♓",  # Pisces
    "I": "ℹ",  # Info symbol
    "J": "🎷",  # Saxophone
    "K": "🎍",  # Bamboo
    "L": "🕓",  # Clock 3
    "M": "♏",  # Scorpio
    "N": "♑",  # Capricorn
    "O": "⭕",  # Circle
    "P": "🅿",  # Parking sign
    "Q": "🎯",  # Target
    "R": "®",  # Registered
    "S": "💲",  # Dollar sign
    "T": "✝",  # Cross
    "U": "⛎",  # Ophiuchus
    "V": "♈",  # Aries
    "W": "🔱",  # Trident
    "X": "❌",  # Cross mark
    "Y": "🍸",  # Martini glass
    "Z": "⚡",  # Lightning bolt
}

def text_to_mojicune(text):
    """Convert plain text into MojiCune symbols."""
    return "".join(moji_dict.get(char.upper(), char) for char in text)

if __name__ == "__main__":
    user_input = input("Enter text: ")
    print("MojiCune Output:", text_to_mojicune(user_input))
