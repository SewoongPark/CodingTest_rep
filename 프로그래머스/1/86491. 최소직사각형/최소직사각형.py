def solution(sizes):
    max_w, max_h = 0, 0
    
    for s in sizes:
        w, h = s[0], s[1]
        if h > w:
            w, h = h, w
        max_w = max(max_w, w)
        max_h = max(max_h, h)

    return max_w * max_h
