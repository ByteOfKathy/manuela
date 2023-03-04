import cv2

minNeighbors = 25
confidence = 1.1


def detectSmile(image: cv2.imread) -> list | None:
    """
    Detects smile in image
    parameters
    ----------
    image: image to detect smile in
    returns
    -------
    list of coordinates of smile
    """
    smileCascade = cv2.CascadeClassifier("cascades/smile.xml")
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = smileCascade.detectMultiScale(gray, confidence, minNeighbors)
    return faces


if __name__ == "__main__":
    image = cv2.imread("images/nice-man-smiling.jpg")
    faces = detectSmile(image)
    for x, y, w, h in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_color = image[y : y + h, x : x + w]
    cv2.imshow("image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
