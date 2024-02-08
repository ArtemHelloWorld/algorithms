from typing import List, Dict


def solution(url: str, params: Dict[str, str]) -> str:
    params_str = []
    for param in params:
        params_str.append(f'{param}={params[param]}')
    p = '&'.join(sorted(params_str))
    if p:
        return f'{url}?{p}'
    return f'{url}'