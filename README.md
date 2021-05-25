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

### 1

Поиск URL в реестре фишинговых доменов. Возвращает True, если домен обнаружен в реестре.

    search(url_in: str)
Сам реестр расположен в открытом доступе в репозитории https://github.com/mitchellkrogza/Phishing.Database, откуда может быть подгружен с помощью

    refresh_db()

### 2

С помощью сервиса WHOIS реализован поиск компании-владельца домена. Если у домена не отображается владелец, то домен считается подозрительным. Иначе, название компании выводится на экран, и у пользователя есть возможность проанализировать его. 

    check_owner(url_in: str)

### 3

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

### 4

Генерация доменного имени, которое менее всего подвержено фишингу.

    generate_domain_name(<list_of_keywords>[, <str_toplevel_domain>][, <str_delimiter>])

Для заданных ключевых слов генерируются синонимы, из синонимов составляются все возможные комбинации, они склеиваются через опционально задаваемый разделитель, к получившейся строке прибавляется домен верхнего уровня, который также можно задать.

Получившиеся доменные имена проверяются на доступность с помощью сервиса whois.

Пример для ключевых слов signal, quest:

    names, values = generate_domain_name(['signal', 'quest'])
    for i in range(len(names)):
        print("{:.2f}".format(values[i]) + " | " + str(names[i]))

Вывод (первый столбец - оценка подверженности фишингу, второй - доменные имена и их доступность для регистрации):

    1.21 | [('signalise-seeking.com', True), ('seeking-signalise.com', True)]
    1.26 | [('bespeak-seeking.com', True), ('seeking-bespeak.com', True)]
    1.26 | [('point-seeking.com', True), ('seeking-point.com', True)]
    1.26 | [('sign-seeking.com', True), ('seeking-sign.com', True)]
    1.26 | [('signal-seeking.com', True), ('seeking-signal.com', True)]
    1.26 | [('signalize-seeking.com', True), ('seeking-signalize.com', True)]
    1.32 | [('betoken-seeking.com', True), ('seeking-betoken.com', True)]
    1.33 | [('signalise-pursuance.com', True), ('pursuance-signalise.com', True)]
    1.38 | [('signalise-bay.com', True), ('bay-signalise.com', True)]
    1.38 | [('signalise-bespeak.com', True), ('bespeak-signalise.com', True)]
    1.38 | [('signalise-pursuit.com', True), ('pursuit-signalise.com', True)]
    1.38 | [('signalise-request.com', True), ('request-signalise.com', True)]
    1.39 | [('bespeak-pursuance.com', True), ('pursuance-bespeak.com', True)]
    1.39 | [('point-pursuance.com', True), ('pursuance-point.com', True)]
    1.39 | [('sign-pursuance.com', True), ('pursuance-sign.com', True)]
    1.39 | [('signal-pursuance.com', True), ('pursuance-signal.com', True)]
    1.39 | [('signalize-pursuance.com', True), ('pursuance-signalize.com', True)]
    1.43 | [('indicate-seeking.com', True), ('seeking-indicate.com', True)]
    1.43 | [('signaling-seeking.com', True), ('seeking-signaling.com', True)]
    1.43 | [('bespeak-bay.com', True), ('bay-bespeak.com', True)]
    1.43 | [('bespeak-bespeak.com', True), ('bespeak-bespeak.com', True)]
    1.43 | [('bespeak-pursuit.com', True), ('pursuit-bespeak.com', True)]
    1.43 | [('bespeak-request.com', True), ('request-bespeak.com', True)]
    1.43 | [('point-bay.com', True), ('bay-point.com', False)]
    1.43 | [('point-bespeak.com', True), ('bespeak-point.com', True)]
    1.43 | [('point-pursuit.com', True), ('pursuit-point.com', True)]
    1.43 | [('point-request.com', True), ('request-point.com', True)]
    1.43 | [('sign-bay.com', True), ('bay-sign.com', True)]
    1.43 | [('sign-bespeak.com', True), ('bespeak-sign.com', True)]
    1.43 | [('sign-pursuit.com', True), ('pursuit-sign.com', True)]
    1.43 | [('sign-request.com', False), ('request-sign.com', True)]
    1.43 | [('signal-bay.com', True), ('bay-signal.com', True)]
    1.43 | [('signal-bespeak.com', True), ('bespeak-signal.com', True)]
    1.43 | [('signal-pursuit.com', True), ('pursuit-signal.com', True)]
    1.43 | [('signal-request.com', True), ('request-signal.com', True)]
    1.43 | [('signalize-bay.com', True), ('bay-signalize.com', True)]
    1.43 | [('signalize-bespeak.com', True), ('bespeak-signalize.com', True)]
    1.43 | [('signalize-pursuit.com', True), ('pursuit-signalize.com', True)]
    1.43 | [('signalize-request.com', True), ('request-signalize.com', True)]
    1.44 | [('betoken-pursuance.com', True), ('pursuance-betoken.com', True)]
    1.49 | [('betoken-bay.com', True), ('bay-betoken.com', True)]
    1.49 | [('betoken-bespeak.com', True), ('bespeak-betoken.com', True)]
    1.49 | [('betoken-pursuit.com', True), ('pursuit-betoken.com', True)]
    1.49 | [('betoken-request.com', True), ('request-betoken.com', True)]
    1.56 | [('indicate-pursuance.com', True), ('pursuance-indicate.com', True)]
    1.56 | [('signaling-pursuance.com', True), ('pursuance-signaling.com', True)]
    1.60 | [('indicate-bay.com', True), ('bay-indicate.com', True)]
    1.60 | [('indicate-bespeak.com', True), ('bespeak-indicate.com', True)]
    1.60 | [('indicate-pursuit.com', True), ('pursuit-indicate.com', True)]
    1.60 | [('indicate-request.com', True), ('request-indicate.com', True)]
    1.60 | [('signaling-bay.com', True), ('bay-signaling.com', True)]
    1.60 | [('signaling-bespeak.com', True), ('bespeak-signaling.com', True)]
    1.60 | [('signaling-pursuit.com', True), ('pursuit-signaling.com', True)]
    1.60 | [('signaling-request.com', True), ('request-signaling.com', True)]
    1.63 | [('signalise-quest.com', True), ('quest-signalise.com', True)]
    1.69 | [('bespeak-quest.com', True), ('quest-bespeak.com', True)]
    1.69 | [('point-quest.com', False), ('quest-point.com', True)]
    1.69 | [('sign-quest.com', False), ('quest-sign.com', True)]
    1.69 | [('signal-quest.com', False), ('quest-signal.com', True)]
    1.69 | [('signalize-quest.com', True), ('quest-signalize.com', True)]
    1.75 | [('betoken-quest.com', True), ('quest-betoken.com', True)]
    1.86 | [('indicate-quest.com', True), ('quest-indicate.com', True)]
    1.86 | [('signaling-quest.com', True), ('quest-signaling.com', True)]



