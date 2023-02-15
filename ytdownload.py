from pytube import YouTube

def download(link):
    video = YouTube(link)
    video = video.streams.get_highest_resolution()
    try:
        video.download()
    except:
        print("Ocorreu um erro. Verifique o link utilizado.")
    print("Download concluído. Cheque a pasta do aplicativo para ver o seu vídeo.")

link = input("Insira a URL do vídeo que você deseja fazer o download: ")
download(link)
