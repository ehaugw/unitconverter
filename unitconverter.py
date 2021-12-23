# re is needed for regular expression matching
import re


# these are the metric units that we wish to convert to imperial units
si_to_imp = {
    "m":    ("ft",  3.28084),
    "g":    ("lbs", 0.00220462)
}

# these are the unit prefixes that we wish to be able to handle
prefixes = {
    "k":    1e3,
    "h":    1e2,
    "d":    1e-1,
    "c":    1e-2,
    "m":    1e-3
}

# this is the string that is should be converted to use imperial units
text_to_convert = "The baby was 59.1cm tall and weighted 4kg at birth. The mother was 1.71m and 71.22kg before birth and 67.22kg after birth."

# the candidate must implement this function
def convert_text(text):
    old_text = ""
    while old_text != text:
        old_text = text

        match = re.match(r".*[^0-9\.]([0-9]+(\.[0-9]+)?)(([%s])?([%s])).*" % ("".join(prefixes.keys()), "".join(si_to_imp.keys())), text)
        if match:
            groups = match.groups()

            prefix = 1 if groups[3] is None else prefixes[groups[3]]
            unit_info = si_to_imp[groups[4]]

            scalar = float(groups[0]) * prefix * unit_info[1]
            
            if unit_info[0] != "ft":
                new_str = "%.2f%s" % (scalar, unit_info[0])
            else:
                new_str = "%.0f'%.0f\"" % (int(scalar), (scalar - int(scalar)) * 12)

            text = text.replace("%s%s" % (groups[0], groups[2]), new_str)

    return text


if __name__ == "__main__":
    #  assert convert_text(text_to_convert) == ""
    print(convert_text(text_to_convert))

