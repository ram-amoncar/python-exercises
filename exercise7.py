import os

demo_folder = "./res/exercise7/demo"
out_folder = "./res/exercise7/out"

try:
    os.mkdir(out_folder)
except:
    pass

def rename_files(ext: str):
    list_of_files = [(file) for file in os.listdir(demo_folder) if os.path.splitext(file)[1] == '.' + ext]
    for i, file in enumerate(list_of_files):
        complete_path = os.path.normpath(os.path.join(demo_folder, file))
        rename_path = os.path.normpath(
            os.path.join(out_folder, str(i + 1) + os.path.splitext(file)[1])
        )
        os.replace(complete_path, rename_path)
        os.system(f'cp {rename_path} {complete_path}')

rename_files('jpg')