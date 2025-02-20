import re

def tokenize_gujarati(text):
    """
    Tokenizes Gujarati text, handling punctuations, dates, URLs, emails, numbers, and usernames.

    Args:
        text: The Gujarati text to tokenize.

    Returns:
        A list of tokens.
    """

    # Unicode range for Gujarati script
    gujarati_range = r"[\u0A80-\u0AFF]+"

    # Regular expression patterns
    patterns = [
        (r"\d{1,2}/\d{1,2}/\d{4}", "DATE"),  # Dates (DD/MM/YYYY)
        (r"\d{1,3}(?:,\d{3})*(?:\.\d+)?", "NUMBER"), # Numbers like 3,22,243 or 33.15
        (r"\d+(?:/\d+)+", "FRACTION"), # Numbers like 313/77
        (r"https?://\S+", "URL"),  # URLs
        (r"\S+@\S+\.\S+", "EMAIL"),  # Emails
        (r"@\w+", "USERNAME"),  # Social media usernames
        (r"[.,!?\"'()\[\]{}:;—–-]", "PUNCTUATION"),  # Punctuations
        (gujarati_range, "GUJARATI_WORD"), # Gujarati words
        (r"\s+", None),  # Whitespace (ignore)
        (r"\S+", "OTHER"), # catch all other tokens.
    ]

    tokens = []
    for pattern, tag in patterns:
        for match in re.finditer(pattern, text):
            if tag:
                tokens.append((match.group(0), tag))

    return tokens

# Example Usage
gujarati_text = """
આજે તારીખ 15/08/2023 છે. મારો નંબર 3,22,243 છે. જુઓ 33.15 અને 313/77. 
મારી વેબસાઈટ https://www.example.com છે. ઈમેલ me@example.com છે. @user123 જુઓ! 
આ વાક્યમાં કેટલાક વિરામચિહ્નો છે. જેમ કે, . , ! ? " ' ( ) [ ] { } : ; — – -
અને ગુજરાતી શબ્દો પણ છે. જેમ કે, ઘર, પાણી, જમવાનું.
"""

tokens = tokenize_gujarati(gujarati_text)
for token, tag in tokens:
    print(f"{token}: {tag}")

gujarati_text2 = "મારું નામ 1234567890 છે."
tokens2 = tokenize_gujarati(gujarati_text2)
for token, tag in tokens2:
    print(f"{token}: {tag}")
