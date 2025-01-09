# HumanWaveDetector

Dự án này là một ứng dụng camera trực tiếp sử dụng Mediapipe để phát hiện tay và tư thế, và in ra "Hello World" khi một người vẫy tay.
Day la mot phan trong du an khac*

## Tính năng
- Phát hiện tay và tư thế với Mediapipe.
- Hiển thị luồng camera với lớp phủ cho tay và tư thế được phát hiện.
- In ra "Hello World" khi phát hiện người đang vẫy tay.

## Yêu cầu
- Python >= 3.7
- OpenCV
- Mediapipe

## Cài đặt

1. Clone repository này:
```bash
git clone https://github.com/ihatesea69/HumanWaveDetector
cd HelloDetection_HumanDetection_Module09_01_2025
```


1. Hoặc có thể cài đặt thông qua `setup.py`:
```bash
python setup.py install
```

## Sử dụng

Chạy script để khởi động ứng dụng:
```bash
python main.py
```

### Điều khiển
- Nhấn `q` để thoát ứng dụng.

## Tùy chỉnh

- Sửa đổi logic nhận diện vẫy tay trong code để phù hợp với nhu cầu phát hiện cử chỉ cụ thể của bạn:
```python
if landmarks[4].x > landmarks[3].x and landmarks[8].y < landmarks[6].y:
    waving_hand = True
```

## Giấy phép

Dự án thuoc nhom sinh vien HUFLIT, moi chi tiet xin vui long lien he facebook ben duoi

## Hỗ trợ

Đối với câu hỏi hoặc vấn đề, vui lòng lien he trên [Facebook](https://www.facebook.com/danhhoanghieunghi69/).

---

ể phân phối dự án, bạn có thể sử dụng các công cụ như `twine` để tải lên PyPI.
