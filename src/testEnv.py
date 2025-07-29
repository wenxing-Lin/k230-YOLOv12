from ultralytics import YOLO

# 将所有执行代码放在这个条件块里
if __name__ == '__main__':
    model = YOLO('yolov12n.pt')
    model.val(data=r'D:\projects\py\yolov12\ultralytics\cfg\datasets\coco.yaml', save_json=True)