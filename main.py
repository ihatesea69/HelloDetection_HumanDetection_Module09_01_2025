import cv2 
import mediapipe as mp 
import time

mp_drawing_util = mp.solutions.drawing_utils
mp_hand = mp.solutions.hands
mp_pose = mp.solutions.pose

hands = mp_hand.Hands(
    model_complexity=0,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5,
)

pose = mp_pose.Pose(
    static_image_mode=False,
    model_complexity=1,
    enable_segmentation=False,
    min_detection_confidence=0.5
)

cap = cv2.VideoCapture(1)
cv2.namedWindow("Camera with Overlay", cv2.WINDOW_NORMAL)

prev_time = 0
fps = 10
interval = 1 / fps

while cap.isOpened():
    current_time = time.time()
    if current_time - prev_time >= interval:
        success, img = cap.read()
        if not success:
            break

        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        hand_results = hands.process(img)
        pose_results = pose.process(img)
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

        hand_detected = False
        waving_hand = False

        # Vẽ nhận diện bàn tay
        if hand_results.multi_hand_landmarks:
            for hand in hand_results.multi_hand_landmarks:
                mp_drawing_util.draw_landmarks(img, hand, mp_hand.HAND_CONNECTIONS)

                # Kiểm tra điều kiện dơ tay chào (giả sử ngón cái và ngón trỏ mở rộng)
                landmarks = hand.landmark
                if landmarks[4].x > landmarks[3].x and landmarks[8].y < landmarks[6].y:
                    waving_hand = True

        # Vẽ nhận diện cơ thể
        if pose_results.pose_landmarks:
            mp_drawing_util.draw_landmarks(
                img, pose_results.pose_landmarks, mp_pose.POSE_CONNECTIONS
            )

            # Kiểm tra nếu có người trong khung hình
            if pose_results.pose_landmarks.landmark:
                hand_detected = True

        # In "Hello World" nếu phát hiện người và dơ tay chào
        if hand_detected and waving_hand:
            print("Xin Chào Bạn")

        cv2.imshow("Camera with Overlay", img)
        prev_time = current_time

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
