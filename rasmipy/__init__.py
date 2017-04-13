# https://en.wikipedia.org/wiki/Arabic_(Unicode_block)

# replacements
RASMIFY_TRANSLATION_TABLE = {
    '\N{ARABIC LETTER ALEF WITH MADDA ABOVE}': '\N{ARABIC LETTER ALEF}',
    '\N{ARABIC LETTER ALEF WITH HAMZA ABOVE}': '\N{ARABIC LETTER ALEF}',
    '\N{ARABIC LETTER WAW WITH HAMZA ABOVE}': '\N{ARABIC LETTER WAW}',
    '\N{ARABIC LETTER ALEF WITH HAMZA BELOW}': '\N{ARABIC LETTER ALEF}',
    '\N{ARABIC LETTER YEH WITH HAMZA ABOVE}': '\N{ARABIC LETTER DOTLESS BEH}',
    '\N{ARABIC LETTER BEH}': '\N{ARABIC LETTER DOTLESS BEH}',
    '\N{ARABIC LETTER TEH MARBUTA}': '\N{ARABIC LETTER HEH}',
    '\N{ARABIC LETTER TEH}': '\N{ARABIC LETTER DOTLESS BEH}',
    '\N{ARABIC LETTER THEH}': '\N{ARABIC LETTER DOTLESS BEH}',
    '\N{ARABIC LETTER JEEM}': '\N{ARABIC LETTER HAH}',
    '\N{ARABIC LETTER KHAH}': '\N{ARABIC LETTER HAH}',
    '\N{ARABIC LETTER THAL}': '\N{ARABIC LETTER DAL}',
    '\N{ARABIC LETTER ZAIN}': '\N{ARABIC LETTER REH}',
    '\N{ARABIC LETTER SHEEN}': '\N{ARABIC LETTER SEEN}',
    '\N{ARABIC LETTER DAD}': '\N{ARABIC LETTER SAD}',
    '\N{ARABIC LETTER ZAH}': '\N{ARABIC LETTER TAH}',
    '\N{ARABIC LETTER GHAIN}': '\N{ARABIC LETTER AIN}',
    '\N{ARABIC LETTER FEH}': '\N{ARABIC LETTER DOTLESS FEH}',
    '\N{ARABIC LETTER QAF}': '\N{ARABIC LETTER DOTLESS QAF}',
    '\N{ARABIC LETTER KAF}': '\N{ARABIC LETTER KEHEH}',
    '\N{ARABIC LETTER NOON}': '\u06BA',
    '\N{ARABIC LETTER YEH}': '\N{ARABIC LETTER ALEF MAKSURA}',
    '\N{ARABIC LETTER FARSI YEH}': '\N{ARABIC LETTER ALEF MAKSURA}',
    '\N{ARABIC LETTER ALEF WASLA}': '\N{ARABIC LETTER ALEF}',
}
# single removals
RASMIFY_TRANSLATION_TABLE.update({x: None for x in '\N{ARABIC LETTER HAMZA}'
                                                   '\N{ARABIC TATWEEL}'
                                                   '\N{ARABIC SUBSCRIPT ALEF}'
                                                   '\N{ARABIC LETTER SUPERSCRIPT ALEF}'
                                                   '\N{ARABIC LETTER HIGH HAMZA}'
                                                   '\N{ARABIC SMALL HIGH ROUNDED ZERO}'
                                                   '\N{ARABIC SMALL LOW MEEM}'})
# removal slices
for start, end in (('\N{ARABIC SMALL HIGH TAH}', '\N{ARABIC TRIPLE DOT PUNCTUATION MARK}'),
                   ('\N{ARABIC FATHATAN}', '\N{ARABIC HAMZA BELOW}'),
                   ('\N{ARABIC SMALL HIGH LIGATURE SAD WITH LAM WITH ALEF MAKSURA}',
                    '\N{ARABIC SMALL HIGH SEEN}'),
                   ('\N{ARABIC SMALL HIGH DOTLESS HEAD OF KHAH}', '\N{ARABIC SMALL YEH}')):
    pointer = ord(start)
    while pointer <= ord(end):
        RASMIFY_TRANSLATION_TABLE[pointer] = None
        pointer += 1
del start, end, pointer
RASMIFY_TRANSLATION_TABLE = str.maketrans(RASMIFY_TRANSLATION_TABLE)


def rasmify(text: str) -> str:
    """ Reduces an arabic string to its rasm. """
    result = text.translate(RASMIFY_TRANSLATION_TABLE)
    # Insert zero-width-joiner into lam lam ha to avoid wrong ligatures
    result = result.replace(
        '\N{ARABIC LETTER LAM}\N{ARABIC LETTER LAM}\N{ARABIC LETTER HEH}',
        '\N{ARABIC LETTER LAM}\N{ARABIC LETTER LAM}\N{ZERO WIDTH JOINER}\N{ARABIC LETTER HEH}')
    return result.strip()


__all__ = ['RASMIFY_TRANSLATION_TABLE', rasmify.__name__]
