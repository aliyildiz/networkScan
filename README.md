# networkScan

## ENGLISH

## Required Libraries

For the run of the project, install `scapy` and `configparser` libraries.

```
pip install scapy
```
```
pip install configparser
```

## Execute The Project

For the execute of the project, run the `network.py` file with `root` permission.

```
sudo python network.py
```
On first run it scans the network and saves MAC and IP on the 'config.conf' file.
`firsttime` variable in the `config.conf` file will make 1.
On the second run will compare MAC and IP in the `config.conf` file and MAC and IP of the new value.

If MAC adresses are the same, will look IP adresses.
If MAC adresses are the same and IP adresses are not the same will ask to the user if they want add.

If MAC adresses are not the same it is a new device and will ask to the user if they want add.

Note : In the `config.conf` file subnet is `192.168.2.0/24`. If your subnet is different please change the subnet value.


## TÜRKÇE

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
MAC adresi ayni IP adresi farkliysa guncellemek isteyip istemedigini kullaniciya sorar.

MAC adresleri farkliysa yeni bir cihaz aga katilmistir ve bunu da eklemek isteyip istemedigini kullaniciya sorar.

Not : `config.conf` dosyası içinde subnet 192.168.2.0/24 belirtilmiştir. Kendi subnetiniz bu değilse `config.conf` dosyasından bu değeri değiştirmeniz gerekmektedir.
