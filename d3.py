import cv2

print("Choose :")
print("1 for Kakashi")
print("2 for Itachi")
print("3 for Minato")
print("4 for Jiraiya")
print("5 for Naruto")
print("6 for Sasuke")

n = int(input("Enter Number"))

if n==1:
    image = cv2.imread("day3/kakashi.jpg")
elif n==2:
    image = cv2.imread("day3/2.jpg")
elif n==3:
    image = cv2.imread("day3/3.jpg")
elif n==4:
    image = cv2.imread("day3/4.jpg")
elif n==5:
    image = cv2.imread("day3/5.jpg")
elif n==6:
    image = cv2.imread("day3/6.jpg")

cap = cv2.VideoCapture(0)

while True:
    flag, frame = cap.read()
    if not flag:
        print("Can't open Camera")
        break
    image = cv2.resize(image, (frame.shape[1], frame.shape[0]))
    blende_image = cv2.addWeighted(frame, 0.8, image, 0.5, 0)
    cv2.imshow("Blended image", blende_image)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

