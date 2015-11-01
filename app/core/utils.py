import re
from datetime import datetime

from xpinyin import Pinyin

def name2slug(name):
    '''
        1. chinese to pinyin.
        2. to lower.
        3. remove special character. (except: '-',' ')
        4. to convert ' ' into '-'
        5. fix special case of slug.
            I.  multi '-', eg: 'GlaDOS's block' ---> 'gladoss--blog'
            II. ...
    '''
    name = Pinyin().get_pinyin(name)
    pattern = re.compile(r'[^a-zA-z0-9\-]')
    slug = re.sub(pattern, '', name.lower().replace(' ', '-'))
    slug = re.sub('-+', '-', slug)
    return slug
