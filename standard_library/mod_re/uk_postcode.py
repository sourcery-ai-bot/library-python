import re


def is_postcode_valid(postcode: str) ->bool:
    re_p1 = r'^([A-PR-UWYZ0-9][A-HK-Y0-9][AEHMNPRTVXY0-9]?[ABEHMNPRVWXY0-9]'
    re_p2 = r'? {1,2}[0-9][ABD-HJLN-UW-Z]{2}|GIR 0AA)$'
    pattern = f"{re_p1}{re_p2}"
    match = re.match(pattern, postcode)
    return bool(match)

chelsea_fc_postcode = 'SW6 1HS'
chelsea_fc_postcode_is_valid = is_postcode_valid(chelsea_fc_postcode)
print(f"{chelsea_fc_postcode_is_valid = }")

mars_fc_postcode = 'M1LKY W4Y'
mars_fc_postcode_is_valid = is_postcode_valid(mars_fc_postcode)
print(f"{mars_fc_postcode_is_valid = }")
