from PIL import Image

def add_white_background(input_path, output_path):
    img = Image.open(input_path)
    img = img.convert("RGBA")  # 转换为RGBA模式
    width, height = img.size
    new_img = Image.new("RGBA", (width, height), (255, 255, 255))  # 创建白色背景图
    new_img.paste(img, (0, 0), mask=img)  # 将原图粘贴到白色背景上
    new_img.save(output_path, "png")

# 批量处理示例
import os

input_folder = "./images"
output_folder = "./images"

for filename in os.listdir(input_folder):
    if filename.lower().endswith(".png"):
        print(filename)
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)
        add_white_background(input_path, output_path)