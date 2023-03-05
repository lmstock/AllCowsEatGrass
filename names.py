import random

import archive_tests.logthis as logthis


# this is an old name generator that I made several years back and could use tidied up.

def generate_regional_sounds():
    logthis.logger.debug("generate_regional_sounds")
    big_list_of_sounds = [
        'ab', 'eb', 'ib', 'ob', 'ub', 'ba', 'be', 'be', 'bo', 'bu',
        'ad', 'ed', 'id', 'od', 'ud', 'da', 'de', 'de', 'do', 'du',
        'af', 'ef', 'if', 'of', 'uf', 'fa', 'fe', 'fe', 'fo', 'fu',
        'ag', 'eg', 'ig', 'og', 'ug', 'ga', 'ge', 'ge', 'go', 'gu',
        'ah', 'eh', 'ih', 'oh', 'uh', 'ha', 'he', 'he', 'ho', 'hu',
        'ak', 'ek', 'ik', 'ok', 'uk', 'ka', 'ke', 'ke', 'ko', 'ku',
        'al', 'el', 'il', 'ol', 'ul', 'la', 'le', 'le', 'lo', 'lu',
        'am', 'em', 'im', 'om', 'um', 'ma', 'me', 'me', 'mo', 'mu',
        'an', 'en', 'in', 'on', 'un', 'na', 'ne', 'ne', 'no', 'nu',
        'ap', 'ep', 'ip', 'op', 'up', 'pa', 'pe', 'pe', 'po', 'pu',
        'ar', 'er', 'ir', 'or', 'ur', 'ra', 're', 're', 'ro', 'ru',
        'as', 'es', 'is', 'os', 'us', 'sa', 'se', 'se', 'so', 'su',
        'at', 'et', 'it', 'ot', 'ut', 'ta', 'te', 'te', 'to', 'tu',
        'av', 'ev', 'iv', 'ov', 'uv', 'va', 've', 've', 'vo', 'vu',
        'aw', 'ew', 'iw', 'ow', 'uw', 'wa', 'we', 'we', 'wo', 'wu',
        'ax', 'ex', 'ix', 'ox', 'ux', 'xa', 'xe', 'xe', 'xo', 'xu',
        'ay', 'ey', 'iy', 'oy', 'uy', 'ya', 'ye', 'ye', 'yo', 'yu',
        'az', 'ez', 'iz', 'oz', 'uz', 'za', 'ze', 'ze', 'zo', 'zu'
                      ]

    regional_syllables_list = []
    for i in range(20):
        syllable = random.choice.__call__(big_list_of_sounds)
        regional_syllables_list.append(syllable)

    return regional_syllables_list


def generate_name():
    logthis.logger.debug("generate_name")
    
    regional_sound = generate_regional_sounds() 
    
    name = []
    new_name = []
    length = random.randint(1,4)   
    for i in range(length):
        syllable = random.choice.__call__(regional_sound)
        name.append(syllable)
    new_name = ''.join(str(x) for x in name)

    return new_name


