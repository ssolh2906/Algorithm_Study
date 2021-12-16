import Config

NUM_FRAMES = Config.NUM_FRAMES


def myLRU(page_rf):
    # 빈프레임을 -1로 표현
    frames = [-1, ] * NUM_FRAMES
    age = [0, ] * NUM_FRAMES
    count = 0

    for page in page_rf:
        #print("check if they have page #" ,page)
        if page_fault_lru(frames, age, page):
            count += 1
    return count


def page_fault_lru(frames, age, page):
    # 1. frame 에서 해당 page 존재여부확인
    page_fault = True
    for i in range(len(frames)):
        if frames[i] == page:
            page_fault = False
            idx = i
            update(frames, age, page, idx)
            return page_fault
    # 2. 존재하지 않을 시 가장 오래 된 참조로 교체
    if page_fault:
        oldest = find_oldest(age)
        update(frames, age, page, oldest)
        return page_fault


def find_oldest(age):
    oldest = 0
    max_age = 0
    for i in range(len(age)):
        if age[i] > max_age:
            max_age = age[i]
            oldest = i
    return oldest


def update(frames, age, page, idx):
    frames[idx] = page
    for i in range(NUM_FRAMES):
        if i == idx:
            age[i] = 0
        else:
            age[i] += 1

