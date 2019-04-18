import cv2
import numpy as np
import resize
import detect_edge as de

def remove_bg(image):
    BLUR = 21
    MASK_DILATE_ITER = 10
    MASK_ERODE_ITER = 10

    img = cv2.imread(image)
    img = resize.image_resize(img)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    edges = de.detect_edge(gray)
    edges = cv2.dilate(edges, None)
    edges = cv2.erode(edges, None)

    contour_info = []
    contours, _ = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

    for c in contours:
        contour_info.append((
            c,
            cv2.isContourConvex(c),
            cv2.contourArea(c),
        ))
    contour_info = sorted(contour_info, key=lambda c: c[2], reverse=True)
    max_contour = contour_info[0]

    mask = np.zeros(edges.shape, dtype="uint8")
    cv2.fillConvexPoly(mask, max_contour[0], (255))

    mask = cv2.dilate(mask, None, iterations=MASK_DILATE_ITER)
    mask = cv2.erode(mask, None, iterations=MASK_ERODE_ITER)

    img_a = cv2.bitwise_and(img, img, mask=mask)

    return img_a
    