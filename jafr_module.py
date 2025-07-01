
def name_to_number(name):
    return sum(ord(c) for c in name if c.isalpha())

def get_jafr_insight(name_value, mother_value):
    return {
        "Name Numeric Value": name_value,
        "Mother Name Value": mother_value,
        "Interpretation": "This combination suggests a divine affinity toward spiritual insight and ancestral influence."
    }
