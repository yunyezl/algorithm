import re

def solution(m, musicinfos):
    mi = {}

    for i in musicinfos:
        start, end, title, code = i.split(',')
        code = code.replace('C#', 'c').replace('D#', 'd').replace('F#','f').replace('G#','g').replace('A#','a')
        start_h, start_m, end_h, end_m = map(int, start.split(':') + end.split(':'))
        playTime = 60*(end_h-start_h) + (end_m-start_m)
        if playTime > len(code):
            gap = playTime - len(code)
            playLine = code + code*(gap//len(code)) + code[:gap%len(code)]
        elif playTime < len(code):
            playLine = code[:playTime]
        else:
            playLine = code
        mi[title] = [''.join(playLine), playTime]

    candidate = []
    m = m.replace('C#', 'c').replace('D#', 'd').replace('F#','f').replace('G#','g').replace('A#','a')
    for title, info in mi.items():
        info[0] = info[0].replace('C#', 'c').replace('D#', 'd').replace('F#','f').replace('G#','g').replace('A#','a')
        if m in info[0]:
            candidate.append([title, mi[title][1]])

    if len(candidate) == 0:
        return "(None)"
    elif len(candidate) > 1:
        candidate.sort(key=lambda x:-x[1])

    return candidate[0][0]
