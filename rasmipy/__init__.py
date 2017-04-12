import re

def rasmify(arabic_string):
    
    # List of unicode characters that should be removed
    # '\u0615', '\u0617', '\u0618', '\u0619', '\u061A', '\u061E',
    # '\u0621',
    # '\u0640
    # '\u064B', '\u064C', '\u064D', '\u064F', '\u0650', '\u0651', '\u0652', '\u0653', '\u0654', '\u0655
    # '\u0656',
    # '\u0670',
    # '\u0674',
    # '\u06D6', '\u06D7', '\u06D8', '\u06D9', '\u06DA', '\u06DB', '\u06DC',
    # '\06DF', \u06E1', '\u06E2', '\u06E3', '\u06E4', '\u06E5', '\u06E6'
    # '\u06ED',
    """
    Reduce an arabic string to its rasm
    :param arabic_string: 
    :return: rasm_string
    """
    remove_characters = "[\u0615-\u061e\u0621\u0640\u064b-\u0655\u0656\u0670\u0674\u06d6-\u06dc\u06df\u06e1-\u06e6\u06ed]"

    rasm_string = re.sub(remove_characters, "", arabic_string)

    # Replace arabic letter alef wasla (\u0671) with arabic letter alef (\u0627)
    rasm_string = re.sub("\u0671", "\u0627", rasm_string)

    # Replace arabic letter teh (\u062A) with arabic letter dotless beh (\u066E)
    rasm_string = re.sub("\u062A", "\u066E", rasm_string)

    # Replace arabic letter teh marbuta (\u0629) with arabic letter heh (\u0647)
    rasm_string = re.sub("\u0629", "\u0647", rasm_string)

    # Replace arabic letter feh (\u0641) with arabic letter dotless feh (\u06A1)
    rasm_string = re.sub("\u0641", "\u06A1", rasm_string)

    # Replace arabic letter beh (\u0628) with arabic letter dotless beh (\u066E)
    rasm_string = re.sub("\u0628", "\u066E", rasm_string)

    # Replace arabic letter yeh (\u064A) with arabic letter alef maksura (\u0649)
    rasm_string = re.sub("\u064A", "\u0649", rasm_string)

    # Replace arabic letter kaf (\u0643) with arabic letter keheh (\u06A9)
    rasm_string = re.sub("\u0643", "\u06A9", rasm_string)

    # Replace arabic letter alef with hamza below (\u0625) with arabic letter alef (\u0627)
    rasm_string = re.sub("\u0625", "\u0627", rasm_string)

    # Replace arabic letter qaf (\u0642) with arabic letter dotless qaf (\u066F)
    rasm_string = re.sub("\u0642", "\u066F", rasm_string)

    # Replace arabic letter thal (\u0630) with arabic letter dal (\u062F)
    rasm_string = re.sub("\u0630", "\u062F", rasm_string)

    # Replace arabic letter alef with hamza above (\u0623) with arabic letter alef (\u0627)
    rasm_string = re.sub("\u0623", "\u0627", rasm_string)

    # Replace arabic letter ghain (\u063A) with arabic letter ain (\u0639)
    rasm_string = re.sub("\u063A", "\u0639", rasm_string)

    # Replace arabic letter dad (\u0636) with arabic letter sad (\u0635)
    rasm_string = re.sub("\u0636", "\u0635", rasm_string)

    # Replace arabic letter alef with madda above (\u0622) with arabic letter alef (\u0627)
    rasm_string = re.sub("\u0622", "\u0627", rasm_string)

    # Replace arabic letter sheen (\u0634) with arabic letter seen (\u0633)
    rasm_string = re.sub("\u0634", "\u0633", rasm_string)

    # Replace arabic letter jeem (\u062C) with arabic letter hah (\u062D)
    rasm_string = re.sub("\u062C", "\u062D", rasm_string)

    # Replace arabic letter zain (\u0632) with arabic letter reh (\u0631)
    rasm_string = re.sub("\u0632", "\u0631", rasm_string)

    # Replace arabic letter khah (\u062E) with arabic letter hah (\u062D)
    rasm_string = re.sub("\u062E", "\u062D", rasm_string)

    # Replace arabic letter theh (\u062B) with arabic letter dotless beh (\u066E)
    rasm_string = re.sub("\u062B", "\u066E", rasm_string)

    # Replace arabic letter zah (\u0638) with arabic letter tah (\u0637)
    rasm_string = re.sub("\u0638", "\u0637", rasm_string)

    # Replace arabic letter waw with hamza above (\u0624) with arabic letter waw (\u0648)
    rasm_string = re.sub("\u0624", "\u0648", rasm_string)

    # Replace arabic letter yeh with hamza above (\u0626) with arabic letter dotless beh (\u066E)
    rasm_string = re.sub("\u0626", "\u066E", rasm_string)

    # Replace arabic letter noon (\u0646) with arabic letter noon ghunna (\u06BA)
    rasm_string = re.sub("\u0646", "\u06BA", rasm_string)

    # Replace arabic letter farsi yeh (\u06CC) with arabic letter alef maksura (\u0649)
    rasm_string = re.sub("\u06CC", "\u0649", rasm_string)

    # Insert zero-width-joiner (\u200D) into lam lam ha to avoid wrong ligatures
    rasm_string = re.sub("\u0644\u0644\u0647", "\u0644\u0644\u200D\u0647", rasm_string)

    return rasm_string.strip()