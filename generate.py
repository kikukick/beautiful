#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
from vocab import TEMPLATES, load_vocab

def generate_sentence(vocab: dict) -> str:
    """
    vocab の各カテゴリからランダムに選んで、TEMPLATES から詩文を生成
    """
    template = random.choice(TEMPLATES)
    return template.format(
        place=random.choice(vocab["place"]),
        time=random.choice(vocab["time"]),
        emotion=random.choice(vocab["emotion"]),
        emotion2=random.choice(vocab["emotion2"]),
        noun=random.choice(vocab["noun"]),
        color=random.choice(vocab["color"]),
        verb=random.choice(vocab["verb"]),
    )

def main():
    vocab = load_vocab()
    sentence = generate_sentence(vocab)
    print("▶ 生成文:", sentence)

if __name__ == "__main__":
    main()
