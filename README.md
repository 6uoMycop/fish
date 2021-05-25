# fish
Поиск фишинговых сайтов по домену -- **ВАРИАНТ 2**

## deps:

### python-whois

https://github.com/richardpenman/whois

    $ pip install python-whois

### NLTK

http://nltk.org

    $ pip install nltk

## Использование
Поиск URL в реестре фишинговых доменов. Возвращает True, если домен обнаружен в реестре.

    search(url_in: str)
Сам реестр расположен в открытом доступе в репозитории https://github.com/mitchellkrogza/Phishing.Database, откуда может быть подгружен с помощью

    refresh_db()

С помощью сервиса WHOIS реализован поиск компании-владельца домена. Если у домена не отображается владелец, то домен считается подозрительным. Иначе, название компании выводится на экран, и у пользователя есть возможность проанализировать его. 

    check_owner(url_in: str)

Реализована возможность генерации похожих доменных имен (с помощью замены похожих символов)

    generate(url_in: str, number=10)

Пример результата для google.com:

    g0oglc.o0m
    g0oglc.ocm
    g0oglc.oem
    g0ogle.e0m
    g0ogle.o0m
    gc0q1c.ecm
    gccp1c.eom
    gccqle.cem
    gceple.ecm
    gcogle.ocm
    gcoq1e.cem
    ge0q1e.com


