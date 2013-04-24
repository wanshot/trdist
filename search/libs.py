# -*- encoding: utf-8 -*-
import MeCab

def mecab_separate(text, separate_char=' ', ignores=None):
    if not isinstance(text, str):
        text = text.encode('utf-8')
    m = MeCab.Tagger("-Ochasen")
    if ignores == None:
        ignores = ('、', '。', '「', '」', '【','】', '(', '）', '！', '？', '!', '?','『', '』','・','　')
    items = []
    node = m.parseToNode( text )
    while node:
        if node.surface not in ignores:
            items.append(node.surface)
        node = node.next
    separated_text = separate_char.join(items)
    separated_text = separated_text.strip()
    #print(separated_text)
    return separated_text
