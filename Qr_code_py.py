import qrcode
img = qrcode.make('https://andpan3.github.io/Praesentation.1.wk.ende.RZG.2026/')
type(img)  # qrcode.image.pil.PilImage
img.save("qrcode.png")