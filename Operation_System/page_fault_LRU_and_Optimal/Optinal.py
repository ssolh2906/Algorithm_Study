import Config

MAX_LEN = Config.MAX_PAGE_NUM
NUM_FRAMES = Config.NUM_FRAMES


def myOptimal(page_rf):
    frames = [-1, ] * NUM_FRAMES
    count = 0

    for i in range(len(page_rf)):
        page = page_rf[i]
        if page_fault_optimal(frames,page_rf, page, i):
            #print("current page :", page)
            #print("current frames :", frames)
            count += 1

    return count


def page_fault_optimal(frames,pages, page, curr):
    page_fault = True
    for i in range(len(frames)):
        if frames[i] == page:
            page_fault = False
            idx = i
            return page_fault
    # 존재하지 않을 시 가장 늦게 나오는 참조로 교체


    if page_fault:
        # empty frame
        for i in range(len(frames)):
            if frames[i] == -1:
                frames[i] = page
                return page_fault
        # no empty frame
        latest = find_latest(frames,pages, curr)
        update(frames, page, latest)
        return page_fault


def find_latest(frames,pages, curr):
    loc = [MAX_LEN, ] * NUM_FRAMES
    for i_frame in range(len(frames)) :
        for i_page in range(len(pages))[curr:]:
            if frames[i_frame] == pages[i_page]:
                loc[i_frame] = i_page
                break


    max_idx = find_max_idx(loc)
    return max_idx



def find_max_idx(l):
    max_idx = 0
    max_val = 0
    for i in range(len(l)) :
        if l[i] > max_val:
            max_idx = i
            max_val = l[i]
    return max_idx

def update(frames, page, idx):
    frames[idx] = page
