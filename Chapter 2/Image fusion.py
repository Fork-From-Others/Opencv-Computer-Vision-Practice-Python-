import cv2
img_cat = cv2.imread('cat.jpg')
img_dog = cv2.imread('dog.jpg')
print('img_cat size',img_cat.shape)
print('img_dog size', img_dog.shape)
img_dog_resize = cv2.resize(img_dog, (550, 366))
print('img_dog_resize', img_dog_resize.shape)
res = cv2.addWeighted(img_cat, 0.3, img_dog_resize, 0.9, 0)
cv2.imshow('366*550',res)
cv2.waitKey(0)
cv2.destroyAllWindows()