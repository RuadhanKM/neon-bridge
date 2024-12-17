try:
    from pyscript import window
except ImportError:
    pass

class neon:
    def draw_pixel(color, x, y):
        window.js_pixel(color, x, y)