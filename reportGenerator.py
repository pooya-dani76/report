import os
import datetime
import jdatetime
from zipfile import ZipFile
import shutil

name = 'Pooya Danandeh'
projectName = 'flutter_application_1'
filesPathes = [f'{projectName}/lib',
               f'{projectName}/pubspec.yaml', f'{projectName}/assets']


def get_all_file_paths(directory):
    file_paths = []
    for root, directories, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)
    return file_paths


filesPathes = get_all_file_paths(f'{projectName}/lib') + [
    f'{projectName}/pubspec.yaml'] + get_all_file_paths(f'{projectName}/assets')

if os.path.isdir(f'{name} {str(jdatetime.datetime.now()).split(" ")[0]}') == False:
    os.mkdir(f'{name} {str(jdatetime.datetime.now()).split(" ")[0]}')

outfile = open(
    f'{name} {str(jdatetime.datetime.now()).split(" ")[0]}.txt', '+a')
outfile.write(
    f'Tasks Done on {str(datetime.datetime.now()).split(" ")[0]}: \n')
inFile = open('doneWorks.txt')
worksStrings = inFile.readlines()

for work in worksStrings:
    outfile.write(f'{work}')


with ZipFile(f'{projectName}.zip', 'w') as zip:
    for file in filesPathes:
        zip.write(file)

webReleasePathes = get_all_file_paths(f'{projectName}/build/web')
with ZipFile(f'web{str(jdatetime.datetime.now()).split(" ")[0]}.zip', 'w') as zip:
    for file in webReleasePathes:
        zip.write(file)

outfile.close()


os.replace(f'{name} {str(jdatetime.datetime.now()).split(" ")[0]}.txt',
           f'{name} {str(jdatetime.datetime.now()).split(" ")[0]}/report.txt')
os.replace(f'web{str(jdatetime.datetime.now()).split(" ")[0]}.zip',
           f'{name} {str(jdatetime.datetime.now()).split(" ")[0]}/web{str(jdatetime.datetime.now()).split(" ")[0]}.zip')
os.replace(f'{projectName}.zip',
           f'{name} {str(jdatetime.datetime.now()).split(" ")[0]}/{projectName}.zip')
