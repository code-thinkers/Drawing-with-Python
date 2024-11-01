# Vẽ Hình Nghệ Thuật Với Turtle 🖌️🎨

Chào mừng bạn đến với dự án **Vẽ Hình Nghệ Thuật Với Turtle**! Trong dự án này, chúng ta sẽ sử dụng thư viện Turtle trong Python để tạo ra những hình ảnh đẹp mắt với nhiều màu sắc khác nhau. Đây là một hoạt động thú vị và tuyệt vời để làm quen với lập trình đồ họa!

## Mô Tả Dự Án 📝

Chương trình này sử dụng thư viện Turtle để vẽ các hình tròn màu sắc trong một vòng lặp, tạo ra hiệu ứng chuyển động mượt mà và rực rỡ. Màu sắc được thay đổi liên tục bằng cách sử dụng mô hình màu HSV.

## Cách Chạy Dự Án 🚀

1. **Cài đặt Python**: Đảm bảo bạn đã cài đặt Python trên máy tính của mình. Bạn có thể tải Python tại [python.org](https://www.python.org/downloads/).

2. **Cài đặt Thư Viện Turtle**: Thư viện Turtle thường được cài sẵn trong Python, nhưng nếu bạn gặp vấn đề, hãy cài đặt nó qua pip:
   ```bash
   pip install PythonTurtle
   ```

3. **Chạy Mã Nguồn**: Sao chép mã nguồn và mở tệp Python (.py) trong một trình soạn thảo mã. Sau đó, chạy chương trình:
   ```bash
   python DrawingWithPython.py
   ```

## Mã Nguồn 📄

Dưới đây là mã nguồn chính của dự án:

```python
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
```

## Ghi Chú 📌

- **Khám Phá Thêm**: Hãy thử thay đổi các tham số trong mã nguồn để tạo ra những hình ảnh độc đáo và thú vị hơn!
- **Chia Sẻ Sáng Tạo**: Nếu bạn tạo ra được một hình ảnh đẹp, đừng quên chia sẻ với bạn bè và cộng đồng nhé! 🌍

## Liên Hệ 🤝

Nếu bạn có bất kỳ câu hỏi nào hoặc cần hỗ trợ, hãy liên hệ với chúng tôi qua [Fanpage CodeThinkers](https://www.facebook.com/CodeThinkers).

---

Hãy cùng nhau khám phá và sáng tạo với lập trình nhé! 💖