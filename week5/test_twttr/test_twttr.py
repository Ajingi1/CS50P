from twttr import shorten


def test_upper():
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("AHMAD") == "HMD"



def test_lower():
    assert shorten("twitter") == "twttr"
    assert shorten("ahmad") == "hmd"
    assert shorten("myname") == "mynm"
    assert shorten("mekukace") == "mkkc"

def test_numbers():
    assert shorten("aham124") == "hm124"

def test_characters():
    assert shorten("ahma,.talle") == "hm,.tll"

