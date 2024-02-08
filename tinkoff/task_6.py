spirits_count, question_count = list(map(int, input().split()))

bands = []
spirits_history = {}
for x in range(1, spirits_count+1):
    bands.append({x})
    spirits_history[x] = 1

for _ in range(question_count):
    question = tuple(map(int, input().split()))

    if question[0] == 1:
        band_a, band_b = None, None
        spirit_a, spirit_b = question[1], question[2]

        for band in bands:
            if spirit_a in band:
                band_a = band
            if spirit_b in band:
                band_b = band
            if band_a and band_b:
                break

        if band_a != band_b:
            band_a.update(band_b)
            bands.remove(band_b)

            for spirit in band_a:
                spirits_history[spirit] += 1

    if question[0] == 2:
        spirit_a, spirit_b = question[1], question[2]
        for band in bands:
            if spirit_a in band:
                print('YES' if spirit_b in band else 'NO')
                break
            if spirit_b in band:
                print('YES' if spirit_a in band else 'NO')
                break

    if question[0] == 3:
        spirit = question[1]
        print(spirits_history[spirit])

