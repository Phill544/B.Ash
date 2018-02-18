import pip

# This Module is used to import the modules that B.Ash needs in order to function

def install_Modules():
    pip.main(['install','pypiwin32'])
    pip.main(['install','numpy'])
    pip.main(['install','matplotlib'])
    pip.main(['install','Pillow'])
    pip.main(['install','opencv-python'])
    pip.main(['install','pynput'])
    
install_Modules()
