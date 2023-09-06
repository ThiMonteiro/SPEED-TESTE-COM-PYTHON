# SPEED TESTE COM PYTHON 

Código criado em Python para medir a velocidade da internet.


**Bibliotecas usadas:**

* math
* speedtest


**Como eu consigo fazer isso em Python?**

Primeiro, vamos baixar e importar duas bibliotecas:

* Terminal:

```python
pip install speedtest-cli
```

* Código:

```python
import math
import speedtest
```


Segundo, precisamos instanciar a nossa classe speedtest em uma variavel:

```python
st = speedtest.Speedtest()
```

Terceiro, agora vamos chamar os métodos "download()" e "upload()" que é dada pela classe:

```python
download = st.download()
upload = st.upload()
```

Quarto, finalizamos fazendo um método que converte Bytes para Mega Bytes:


```python
def bytes_para_mb(tamanho_bytes):
    i = int(math.floor(math.log(tamanho_bytes, 1024)))
    potencia = math.pow(1024, i)
    tamanho = round(tamanho_bytes / potencia, 2)

    return f"{tamanho} Mpbs"
```

(obs: quando chamamos esses métodos sem esse conversor, ele nos retorna o valor em bytes)


**Código final:**

```python
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

```
