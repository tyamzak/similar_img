def similar_check(productimg:str, similarimg:str):
    import imgsim
    import cv2
    img0 = cv2.imread(productimg)
    img1 = cv2.imread(similarimg)

    vtr = imgsim.Vectorizer()
    vec0 = vtr.vectorize(img0)
    vec1 = vtr.vectorize(img1)

    dist = imgsim.distance(vec0, vec1)

    # print("distance =", dist)
    return dist

def similar_search():
    import glob
    files = glob.glob("images/*")
    dists = dict()
    for file in files:
        dists[file] = similar_check("similar.png",file)

    similarimg = min(dists,key=dists.get)

    print(f"最も似ている画像は{similarimg}です")
    return dists