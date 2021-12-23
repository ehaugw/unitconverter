import re


si_to_imp = {
    "m":    ("ft",  3),
    "g":    ("lbs", 1/450)
}

prefixes = {
    "k":    1e3,
    "h":    1e2,
    "d":    1e-1,
    "c":    1e-2,
    "m":    1e-3
}

text_to_convert = "The baby was 50.1cm tall and weighted 3.5kg at birth. The mother was 1.71m and 71.22kg before birth and 67.72kg after birth."

def convert_text(text):
    old_text = ""
    while old_text != text:
        old_text = text

        match = re.match(r".*[^0-9\.]([0-9]+\.?[0-9]+)(([%s])?([%s])).*" % ("".join(prefixes.keys()), "".join(si_to_imp.keys())), text)
        if match:
            groups = match.groups()

            print(groups)

            prefix = 1 if groups[2] is None else prefixes[groups[2]]
            unit_info = si_to_imp[groups[3]]
            scalar = float(groups[0]) * prefix * unit_info[1]

            text = text.replace("%s%s" % (groups[0], groups[1]), "%.2f%s" % (scalar, unit_info[0]))

    return text

if __name__ == "__main__":
    print(convert_text(text_to_convert))

