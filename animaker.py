import matplotlib.pyplot as plt
import matplotlib.animation as animation
from PIL import Image as PILImage
import io

class AniMaker():
    def __init__(self):
        self.ims = []
    
    def make_snapshot(self, cont=False):
        buffer = io.BytesIO()        
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        im = PILImage.open(buffer)
        if cont==False:
            plt.close()
        self.ims.append(im)

        return im
    
    def make_gif(self, filename, dt=100):
        self.ims[0].save(filename, 
                         format='GIF',
                         append_images=self.ims[1:], 
                         save_all=True, duration=dt, loop=0)
