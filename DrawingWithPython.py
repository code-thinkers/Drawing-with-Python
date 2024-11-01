from turtle import *
import colorsys

speed(0)  # Tăng tốc độ vẽ 🚀
bgcolor('black')  # Đặt màu nền là đen 🖤
h = 0  # Khởi tạo giá trị màu sắc 🌈

# Vòng lặp ngoài để tạo nhiều hình 🌟
for i in range(16):
    # Vòng lặp trong để vẽ từng phần của hình 🌐
    for j in range(18):
        c = colorsys.hsv_to_rgb(h, 1, 1)  # Chuyển đổi màu từ HSV sang RGB 🎨
        color(c)  # Đặt màu vẽ hiện tại 🌈
        h += 0.005  # Thay đổi giá trị màu sắc cho lần vẽ tiếp theo 🔄
        rt(90)  # Quay phải 90 độ ↩️
        circle(150 - j * 6, 90)  # Vẽ cung tròn với bán kính giảm dần 🔵
        lt(90)  # Quay trái 90 độ ↪️
        circle(150 - j * 6, 90)  # Vẽ cung tròn với bán kính giảm dần 🔵
        rt(180)  # Quay phải 180 độ 🔄
    circle(40, 24)  # Vẽ cung tròn nhỏ để di chuyển tới vị trí mới 🔄

done()  # Hoàn tất vẽ 🎉
