from typing import List, Dict

def solution(sentence: str) -> str:
    for i, word in enumerate(sentence.split()):
        if word == 'Nemo':
            return f'I found Nemo at {i+1}!'
    return "I can't find Nemo :("