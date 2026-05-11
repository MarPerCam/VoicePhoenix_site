from PIL import Image
try:
    img1 = Image.open('assets/images/impactos1.png')
    img2 = Image.open('assets/images/impactos2.png')
    # Resize img2 to match img1 height if necessary
    h1 = img1.height
    w1 = img1.width
    h2 = img2.height
    w2 = img2.width
    if h1 != h2:
        new_w2 = int((h1 / h2) * w2)
        img2 = img2.resize((new_w2, h1))
        w2 = new_w2
    
    new_w = w1 + w2 + 20 # 20px gap
    new_img = Image.new('RGB', (new_w, h1), (255, 255, 255))
    new_img.paste(img1, (0, 0))
    new_img.paste(img2, (w1 + 20, 0))
    new_img.save('assets/images/impactos_sociais.png')
    print('Merged successfully')
except Exception as e:
    print('Error:', e)
