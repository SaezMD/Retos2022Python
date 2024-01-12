#6 ASPECT RATIO DE UNA IMAGEN
"""
Crea un programa que se encargue de calcular el aspect ratio de una imagen a partir de una url.
 * - Url de ejemplo: https://raw.githubusercontent.com/mouredevmouredev/master/mouredev_github_profile.png
 * - Por ratio hacemos referencia por ejemplo a los "16:9" de una imagen de 1920*1080px.
"""

def aspectRatioURL(URLimage:str) -> str:
    """function to get the aspect ratio from any image in the web"""
    import requests, os
    from PIL import Image

    data = requests.get(URLimage).content 

    tempImage = "img.jpg"
    f = open(tempImage,'wb') 
    f.write(data)
    # loading the image
    img = Image.open(tempImage)
    # fetching the dimensions
    wid, hgt = img.size
    img.close()
    f.close()

    #remove the file
    if os.path.exists(tempImage):
        os.unlink(tempImage)
    else:
        print("The file does not exist")

    # displaying the dimensions
    print(str(wid) + "x" + str(hgt))

    def maxDivisor(a, b):
        """get the maximun common divisor for 2 numbers"""
        temporal = 0
        while b != 0:
            temporal = b
            b = a % b
            a = temporal
        return a

    divisor = maxDivisor(wid, hgt)

    return print(f"Ratio is: {int(wid/divisor)}:{int(hgt/divisor)}")

aspectRatioURL("https://saezmd.vercel.app/logos/logo.jfif")
aspectRatioURL("https://www.w3schools.com/images/img_program_up_dataanalytics_300.png")

