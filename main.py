import math
import speedtest


def bytes_para_mb(tamanho_bytes):
    i = int(math.floor(math.log(tamanho_bytes, 1024)))
    potencia = math.pow(1024, i)
    tamanho = round(tamanho_bytes / potencia, 2)

    return f"{tamanho} Mpbs"


st = speedtest.Speedtest()

print("Carregando...")

download = st.download()
upload = st.upload()


print()
print(f"Resultados: \nDowload: {bytes_para_mb(download)} \nUpload: {bytes_para_mb(upload)}")
