import qrcode
import argparse

# 创建解析器
parser = argparse.ArgumentParser(description="生成一致尺寸的二维码，无论网址长度")
parser.add_argument("url", help="输入要生成二维码的网址")

# 解析参数
args = parser.parse_args()
url = args.url

# 创建二维码并固定版本大小
qr = qrcode.QRCode(
    version=5,  # 固定版本大小，保证数据网格结构一致
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # 设置低容错率
    box_size=10,  # 设置单个方块的像素大小
    border=4      # 设置边框宽度
)
qr.add_data(url)
qr.make(fit=True)

# 生成图像并指定输出尺寸
img = qr.make_image(fill="black", back_color="white").resize((300, 300))  # 固定图片大小为300x300像素
img.save("website_qr_code.png")
print("二维码已生成并保存为 website_qr_code.png")
