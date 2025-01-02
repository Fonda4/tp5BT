from machine import Pin, I2C # import Pin and I2C classes
import ssd1306 # import ssd1306 module
# setup the I2C communication
# create I2C object from Pin0 and Pin1
i2c = I2C(0, sda=Pin(20), scl=Pin(21))
display = ssd1306.SSD1306_I2C(128, 64, i2c) # create SSD1306 object
# The following part changes according to what you want to display
display.text('Hello,', 0, 0) # write "Hello," at coordinates (0, 0)
# write "peppe8o.com" at coordinates (0, 16)
display.text('peppe8o.com', 0, 16)
display.text('readers!', 0, 32) # write "readers!" at coordinates (0, 32)
display.invert(1) # invert the display
# display.rotate(1) # rotate the display
# The following line sends what to show to the display
display.show() # show the display