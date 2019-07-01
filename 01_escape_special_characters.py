
import re
import string
try:
    unichr
except NameError:
    unichr = chr


def escape_special_characters(s):
    '''Escape and filter out special characters and non printable characters
    to prevent errors when parsing strings.'''
    # from http://boodebr.org/main/python/all-about-python-and-unicode#UNI_XML
    '''
    s = s.replace('&', '&amp')
    s = s.replace('\'', '&quot')
    s = s.replace('\"', '&quot')
    s = s.replace('<', '&lt')
    s = s.replace('>', '&gt')
    '''
    RE_ILLEGAL = u'([\u0000-\u0008\u000b-\u000c\u000e-\u001f\ufffe-\uffff])' + \
        u'|' + \
        u'([%s-%s][^%s-%s])|([^%s-%s][%s-%s])|([%s-%s]$)|(^[%s-%s])' % \
        (unichr(0xd800), unichr(0xdbff), unichr(0xdc00), unichr(0xdfff),
         unichr(0xd800), unichr(0xdbff), unichr(0xdc00), unichr(0xdfff),
         unichr(0xd800), unichr(0xdbff), unichr(0xdc00), unichr(0xdfff))

    s = filter(lambda x: x in string.printable, s)
    s = re.sub(RE_ILLEGAL, '', s)
    return s
