import nuke
import renderFinished

print "renderFinished menu.py is loaded"
# All Nuke callback functions can be found on below address.
# https://www.thefoundry.co.uk/products/nuke/developers/90/pythondevguide/callbacks.html
nuke.addAfterRender(renderFinished.notify_user)