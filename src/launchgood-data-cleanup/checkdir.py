def checkdir(dir):
    import os
    os.makedirs(dir/'vip', exist_ok=True)
    os.makedirs(dir/'normal', exist_ok=True)