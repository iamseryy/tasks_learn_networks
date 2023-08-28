Урок 3. Технология Ethernet. Протокол IP.
---
Условие:
1. Усложняем сеть из предыдущего домашнего задания
Используя только статическую маршрутизацию связать сеть компов и сервера
2. Проверить работоспособность сети командой ping с компов до сервера и обратно

![](images/image1.png)

![](images/image2.png)

![](images/image3.png)

    2.1. * Попробовать настроить статику так, чтобы пинговались все интерфейсы отовсюду.

![](images/image4.png)

3. Изучить получившиеся таблицы маршрутизации

![](images/image5.png)

![](images/image6.png)

![](images/image7.png)

![](images/image8.png)

![](images/image9.png)

![](images/image10.png)


4. Попрактиковаться в использовании команды tracert

![](images/image11.png)


6.* Настроить loop back интерфейсы, статику до них и они тоже должны пинговаться

* lo0 - 172.16.0.1/16
* lo1 - 192.168.236.1/24

![](images/image12.png)

* lo0 - 172.20.243.164/16
* lo1 - 192.168.46.1/24
* lo3 - 172.31.0.1/16

![](images/image13.png)

* ping loop back интерфейсов

![](images/image14.png)

![](images/image15.png)

![](images/image16.png)

* получившиеся таблицы маршрутизации

![](images/image17.png)

![](images/image18.png)

![](images/image19.png)

![](images/image20.png)

![](images/image21.png)

![](images/image22.png)