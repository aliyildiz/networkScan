# networkScan

## Gerekli Kutuphaneler

Projenin çalışması için `scapy` ve `configparser` kutuphanelerinin kurulmasi gerekir.

```
pip install scapy
```
```
pip install configparser
```

## Projeyi Calistirma

Projeyi calistirmak icin `root` haklariyla `network.py` dosyasini çalistirmak gerekir.

```
sudo python network.py
```

Ilk calistirmada ag taramasi yapar ve `config.conf` dosyasina MAC ve IP adreslerini kaydeder.
`config.conf` icindeki `firsttime` degiskenini 1 yapar.
Ikinci calistirmada ise dosyadaki MAC ve IP adresleriyle yeni gelen MAC ve IP adreslerini karsilatirir.

MAC adresleri ayniysa IP adreslerine bakilir.
IP adresleri ayni degilse `config.conf` dosyasina ekler.
MAC adresi ayni IP adresi farkliysa guncellemek isteyip istemedigini kullaniciya sorar.

MAC adresleri farkliysa yeni bir cihaz aga katilmistir ve bunu da eklemek isteyip istemedigini kullaniciya sorar.

Not : `config.conf` dosyası içinde subnet 192.168.2.0/24 belirtilmiştir. Kendi subnetiniz bu değilse `config.conf` dosyasından bu değeri değiştirmeniz gerekmektedir.
