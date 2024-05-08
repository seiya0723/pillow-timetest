import time
from PIL import Image, ImageDraw, ImageFont

start = time.time()

image_A = Image.open("image_A.jpg")

# 画像Aにテキストを書き込むためのDrawオブジェクトを作成します。
draw        = ImageDraw.Draw(image_A)
text        = "Hello, World!"

# 合否判定と結果を書き込み
font = ImageFont.truetype("NotoSansJP-Medium.ttf", 36)
for i in range(40):
    draw.text((0,i*36), text, fill="white", font=font)


# 撮像した画像をリサイズして貼り付け
image_B         = Image.open("image_B.jpg")
resized_image_B = image_B.resize((500, 500))
image_A.paste(resized_image_B, (100, 100))


# 保存
image_A.save("output_image.jpg")

diff    = time.time() - start

print("かかった時間")
print(diff)


