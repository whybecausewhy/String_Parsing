import re

def split_numeric_alpha_re(s):
    """
    Parses a measurement string to extract its components using regular expressions.

    Args:
        s (str): The measurement string (e.g., "+ 0.000gnM").

    Returns:
        dict: A dictionary containing 'sign', 'numeric_part', 'alpha_part', 'value_changing',
              or None if the string doesn't match the expected format.
    """
    # Optimized regex based on your examples.
    # It assumes the initial sign is part of the numeric representation,
    # or a standalone leading sign for the whole string.
    # We'll extract the first sign if present, then the numeric value.
    pattern = re.compile(r"^(?P<sign>[+-]?)\s*(?P<numeric>-?\d+\.?\d*)\s*(?P<alpha>gn|g|ct|oz)(?P<m_suffix>M?)\s*$")
    match = pattern.match(s.strip()) # .strip() to remove leading/trailing whitespace

    if match:
        data = match.groupdict()
        sign = data['sign'] if data['sign'] else '+' # Default to '+' if no sign
        numeric_str = data['numeric']

        # Determine the final numeric value, considering both leading sign and embedded sign
        try:
            numeric_part = float(numeric_str)
            # If there's an overall sign and it's different from the numeric part's sign,
            # this logic needs refinement based on specific rules for combined signs.
            # For your examples, the leading sign *is* the sign of the numeric value.
            # So, we just use the float conversion directly.
        except ValueError:
            return None # Should not happen with this regex if it matches

        alpha_part = data['alpha']
        value_changing = bool(data['m_suffix'])
        
        return {
            'sign': sign,
            'numeric_part': numeric_part,
            'alpha_part': alpha_part,
            'value_changing': value_changing
        }
    return None

# Your provided examples
measurement_strings = [
    "+ 0.000gn",     "+ 0.000g",    "+ 0.000ct",    "+ 0.00000oz",    "+ 0.802gnM",    "- 37.022gnM",    "- 39.167gnM",    "- 39.167gn",
    "- 2.538g",    "- 2.539gM",    "- 2.539gM",    "- 2.539gM",    "- 2.539g",    "- 12.695ct",    "- 0.08956oz",    "- 39.182gn",    "- 39.182gnM",
    "- 35.710gnM",    "+ 6.003gnM",    "+ 39.738gnM",    "+ 71.436gnM",    "+ 78.797gnM",    "+ 75.618gnM",    "+ 75.618gnM",    "+ 75.618gnM",    "+ 75.618gnM",    "+ 75.618gnM",    "+ 75.618gnM",
    "+ 75.618gn",    "+ 4.899g",    "+ 4.897gM",    "+ 4.897gM",    "+ 4.897gM",    "+ 4.897g",    "+ 24.475ctM",    "+ 24.475ctM",    "+ 24.475ctM",
    "+ 24.475ct",    "+ 24.475ct",    "+ 24.465ctM",    "+ 0.17259oz",    "+ 0.17252ozM",    "+ 75.479gn",
    "+ 75.479gn",    "+ 75.479gnM",    "+ 75.479gnM",    "+ 75.479gn",    "+ 75.479gn",    "+ 75.479gnM",    "+ 75.479gnM",    "+ 75.479gnM"
]

print("Parsing Results:")
for s in measurement_strings:
    parsed = split_numeric_alpha_re(s) # Function call updated
    if parsed:
        print(f"Original: '{s}' -> Parsed: {parsed}")
    else:
        print(f"Original: '{s}' -> FAILED TO PARSE")

print("\nTesting a non-matching string:")
non_matching_string = "invalid_string_123"
parsed_non_match = split_numeric_alpha_re(non_matching_string) # Function call updated
if parsed_non_match:
    print(f"Original: '{non_matching_string}' -> Parsed: {parsed_non_match}")
else:
    print(f"Original: '{non_matching_string}' -> FAILED TO PARSE")
