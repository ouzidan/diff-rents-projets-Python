# pyscreenshot to install ... pip install pyscreenshot
import pyscreenshot

screenshot = pyscreenshot.grab()
screenshot.save("screenshot image.png")
screenshot.show()
