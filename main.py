from pytube import YouTube

storage = r'your folder path'
url = input('Enter video URL: ')
yt = YouTube(url)

mp4_files = yt.streams.filter(file_extension='mp4')
mp4_720p_files = mp4_files.get_by_resolution("720p")
mp4_720p_files.download(storage)
print(f"Downloaded succesfully into {storage}")

a = input("Do you want to download another video? (Yes/No): ").lower()

while a != 'no':
    url = input('Enter video URL: ')
    yt = YouTube(url)

    mp4_files = yt.streams.filter(file_extension='mp4')
    mp4_720p_files = mp4_files.get_by_resolution("720p")
    mp4_720p_files.download(storage)
    print("Downloaded succesfully")
if a == 'no':
    print('Program finished, thanks for using')
