import html
import os

CONTACT = "appdev8661@gmail.com"
UPDATED = {"en": "October 5, 2026", "ru": "5 октября 2026", "uk": "5 жовтня 2026", "de": "5. Oktober 2026"}
EULA = "https://www.apple.com/legal/internet-services/itunes/dev/stdeula/"
ROOT = os.path.dirname(os.path.abspath(__file__))
LANGS = ["en", "de", "uk", "ru"]
LANG_NAMES = {"en": "EN", "de": "DE", "uk": "UA", "ru": "RU"}

UI = {
    "en": {"privacy": "Privacy Policy", "terms": "Terms of Use", "updated": "Last updated", "tagline": "A calm logbook for your car: refuels, service plans and reminders.", "privacy_hint": "What Stint stores and where", "terms_hint": "Subscriptions, estimates and liability", "contact": "Contact"},
    "ru": {"privacy": "Политика конфиденциальности", "terms": "Условия использования", "updated": "Обновлено", "tagline": "Спокойный журнал машины: заправки, планы обслуживания и напоминания.", "privacy_hint": "Что Stint хранит и где", "terms_hint": "Подписки, расчёты и ответственность", "contact": "Связь"},
    "de": {"privacy": "Datenschutzerklärung", "terms": "Nutzungsbedingungen", "updated": "Stand", "tagline": "Ein ruhiges Logbuch für dein Auto: Tanken, Wartungspläne und Erinnerungen.", "privacy_hint": "Was Stint speichert und wo", "terms_hint": "Abos, Berechnungen und Haftung", "contact": "Kontakt"},
    "uk": {"privacy": "Політика конфіденційності", "terms": "Умови використання", "updated": "Оновлено", "tagline": "Спокійний журнал авто: заправки, плани обслуговування й нагадування.", "privacy_hint": "Що Stint зберігає і де", "terms_hint": "Підписки, розрахунки та відповідальність", "contact": "Звʼязок"},
}

PRIVACY = {
    "de": [
        (None, "Stint erhebt keine personenbezogenen Daten. Es gibt kein Konto, keine Anmeldung, keine Analyse, keine Werbung und kein Tracking. Wir betreiben keine Server, die deine Daten empfangen."),
        ("Was auf deinem Gerät bleibt", "Deine Autos, Tankvorgänge und anderen Einträge, Kilometerstände, Wartungspläne, Erinnerungen und Belegfotos werden im privaten Speicher der App auf deinem iPhone gespeichert. Sie sind gemäß deinen iCloud- oder Computer-Einstellungen in den Gerätebackups enthalten. Wir haben keinen Zugriff darauf."),
        ("Kamera und Fotos", "Stint nutzt die Kamera oder die Fotoauswahl nur, wenn du ein Belegfoto hinzufügst. Über die Fotoauswahl erhält die App nur Zugriff auf die Fotos, die du auswählst. Fotos werden komprimiert und zusammen mit dem Eintrag auf deinem Gerät gespeichert."),
        ("Mitteilungen", "Erinnerungen werden lokal auf deinem iPhone geplant. Es werden keine Push-Server verwendet."),
        ("Widgets, Siri und Kurzbefehle", "Widgets lesen eine kurze Zusammenfassung, die die App in einen Container schreibt, den nur Stint und seine Widgets auf deinem Gerät teilen. Anfragen an Siri und Kurzbefehle verarbeitet Apple gemäß der Datenschutzrichtlinie von Apple; Stint erhält nur die Werte aus deiner Anfrage, etwa einen Betrag oder einen Kilometerstand."),
        ("Käufe", "Abos werden von Apple abgewickelt. Wir erhalten keine Zahlungsdaten. Die App prüft den Abo-Status über StoreKit auf dem Gerät."),
        ("Exporte", "CSV- und PDF-Dateien werden auf deinem Gerät erstellt und nur dorthin geteilt, wohin du sie selbst sendest."),
        ("Daten löschen", "Einträge und Autos kannst du in der App löschen. Wenn du die App löschst, werden alle ihre Daten von deinem Gerät entfernt."),
        ("Kinder", "Stint richtet sich nicht an Kinder unter 13 Jahren und erhebt wissentlich keine Informationen über sie."),
        ("Änderungen", "Ändert sich diese Erklärung, aktualisieren wir diese Seite und das Datum oben."),
    ],
    "en": [
        (None, "Stint does not collect personal data. There is no account, no sign-in, no analytics, no advertising and no tracking. We do not run servers that receive your data."),
        ("What stays on your device", "Your cars, refuels and other entries, odometer readings, service plans, reminders and receipt photos are stored in the app’s private storage on your iPhone. They are included in your device backups according to your iCloud or computer backup settings. We cannot access them."),
        ("Camera and photos", "Stint uses the camera or the photo picker only when you add a receipt photo. The photo picker gives the app access only to the photos you choose. Photos are compressed and kept on your device together with the entry."),
        ("Notifications", "Reminders are scheduled locally on your iPhone. No push servers are involved."),
        ("Widgets, Siri and Shortcuts", "Widgets read a short summary that the app writes to a container shared only between Stint and its widgets on your device. Siri and Shortcuts requests are processed by Apple under Apple’s privacy policy; Stint receives only the values from your request, such as an amount or an odometer reading."),
        ("Purchases", "Subscriptions are processed by Apple. We do not receive your payment details. The app checks your subscription status through Apple’s StoreKit on the device."),
        ("Exports", "CSV and PDF files are created on your device and are shared only where you choose to send them."),
        ("Deleting your data", "You can delete entries and cars in the app. Deleting the app removes all of its data from your device."),
        ("Children", "Stint is not directed at children under 13 and does not knowingly collect any information from them."),
        ("Changes", "If this policy changes, we will update this page and the date above."),
    ],
    "ru": [
        (None, "Stint не собирает персональные данные. Нет аккаунта, входа, аналитики, рекламы и трекинга. У нас нет серверов, которые получают ваши данные."),
        ("Что остаётся на устройстве", "Машины, заправки и другие записи, пробег, планы обслуживания, напоминания и фото чеков хранятся в закрытом хранилище приложения на вашем iPhone. Они попадают в резервные копии устройства в соответствии с вашими настройками iCloud или компьютера. У нас к ним доступа нет."),
        ("Камера и фото", "Stint использует камеру или выбор фото, только когда вы добавляете фото чека. Через выбор фото приложение получает доступ лишь к тем снимкам, которые вы выбрали. Фото сжимаются и хранятся на устройстве вместе с записью."),
        ("Уведомления", "Напоминания планируются локально на iPhone. Push-серверы не используются."),
        ("Виджеты, Siri и Быстрые команды", "Виджеты читают короткую сводку, которую приложение записывает в контейнер, общий только для Stint и его виджетов на вашем устройстве. Запросы Siri и Быстрых команд обрабатывает Apple по своей политике конфиденциальности; Stint получает только значения из запроса — например, сумму или пробег."),
        ("Покупки", "Подписки обрабатывает Apple. Мы не получаем ваши платёжные данные. Приложение проверяет статус подписки через StoreKit на устройстве."),
        ("Экспорт", "Файлы CSV и PDF создаются на устройстве и отправляются только туда, куда вы их отправите сами."),
        ("Удаление данных", "Записи и машины можно удалить в приложении. Удаление приложения стирает все его данные с устройства."),
        ("Дети", "Stint не предназначен для детей младше 13 лет и сознательно не собирает о них никакой информации."),
        ("Изменения", "Если политика изменится, мы обновим эту страницу и дату выше."),
    ],
    "uk": [
        (None, "Stint не збирає персональні дані. Немає акаунта, входу, аналітики, реклами й трекінгу. У нас немає серверів, які отримують ваші дані."),
        ("Що залишається на пристрої", "Авто, заправки та інші записи, пробіг, плани обслуговування, нагадування й фото чеків зберігаються в закритому сховищі застосунку на вашому iPhone. Вони потрапляють до резервних копій пристрою відповідно до ваших налаштувань iCloud або компʼютера. Ми не маємо до них доступу."),
        ("Камера і фото", "Stint використовує камеру або вибір фото лише тоді, коли ви додаєте фото чека. Через вибір фото застосунок отримує доступ тільки до знімків, які ви обрали. Фото стискаються й зберігаються на пристрої разом із записом."),
        ("Сповіщення", "Нагадування плануються локально на iPhone. Push-сервери не використовуються."),
        ("Віджети, Siri та Швидкі команди", "Віджети читають коротке зведення, яке застосунок записує в контейнер, спільний лише для Stint і його віджетів на вашому пристрої. Запити Siri та Швидких команд обробляє Apple згідно зі своєю політикою конфіденційності; Stint отримує лише значення із запиту — наприклад, суму чи пробіг."),
        ("Покупки", "Підписки обробляє Apple. Ми не отримуємо ваших платіжних даних. Застосунок перевіряє статус підписки через StoreKit на пристрої."),
        ("Експорт", "Файли CSV і PDF створюються на пристрої та надсилаються лише туди, куди ви їх надішлете самі."),
        ("Видалення даних", "Записи й авто можна видалити в застосунку. Видалення застосунку стирає всі його дані з пристрою."),
        ("Діти", "Stint не призначений для дітей до 13 років і свідомо не збирає про них жодної інформації."),
        ("Зміни", "Якщо політика зміниться, ми оновимо цю сторінку й дату вище."),
    ],
}

TERMS = {
    "de": [
        (None, f"Mit der Nutzung von Stint stimmst du diesen Bedingungen und Apples <a href=\"{EULA}\">Endbenutzer-Lizenzvertrag für lizenzierte Apps</a> zu."),
        ("Kostenlos und Premium", "Die kostenlose Version umfasst ein aktives Auto, bis zu drei Wartungspläne, den vollständigen Verlauf und den CSV-Export. Stint Premium hebt die Grenzen auf und ergänzt Berichte zu den Kosten pro Kilometer, den PDF-Verlauf und zusätzliche Widgets."),
        ("Abos", "<ul><li>Stint Premium wird als automatisch verlängerbares Wochen-, Monats- und Jahresabo angeboten. Die Preise werden vor dem Kauf in der App angezeigt.</li><li>Das Jahresabo kann einen kostenlosen Testzeitraum enthalten. Ein ungenutzter Teil des Testzeitraums verfällt mit dem Kauf eines Abos.</li><li>Die Zahlung wird bei Bestätigung des Kaufs deinem Apple Account belastet.</li><li>Das Abo verlängert sich automatisch, wenn es nicht mindestens 24 Stunden vor Ende des aktuellen Zeitraums gekündigt wird. Die Verlängerung wird innerhalb von 24 Stunden vor Ende des Zeitraums berechnet.</li><li>Abos verwaltest und kündigst du unter Einstellungen → Apple Account → Abonnements. Erstattungen wickelt Apple ab.</li></ul>"),
        ("Berechnungen, keine Beratung", "Verbrauch, Kosten pro Kilometer, Laufleistungsprognosen und Erinnerungen werden aus deinen Eingaben berechnet und können ungenau sein. Halte dich immer an den Wartungsplan des Herstellers und an gesetzliche Fristen wie Versicherung und Hauptuntersuchung. Wir haften nicht für versäumte Wartung, Bußgelder oder Schäden."),
        ("Deine Daten", "Deine Daten werden auf deinem Gerät gespeichert. Für Backups bist du selbst verantwortlich."),
        ("Die App", "Stint wird „wie besehen“ bereitgestellt. Wir können Funktionen ändern oder entfernen. Soweit gesetzlich zulässig, haften wir nicht für indirekte oder Folgeschäden aus der Nutzung der App."),
        ("Änderungen", "Ändern sich diese Bedingungen, aktualisieren wir diese Seite und das Datum oben. Wenn du Stint weiter nutzt, akzeptierst du die aktualisierten Bedingungen."),
    ],
    "en": [
        (None, f"By using Stint you agree to these Terms and to Apple’s <a href=\"{EULA}\">Licensed Application End User License Agreement</a>."),
        ("Free and Premium", "The free version includes one active car, up to three service plans, the full history and CSV export. Stint Premium removes the limits and adds cost-per-kilometre reports, the PDF history and additional widgets."),
        ("Subscriptions", "<ul><li>Stint Premium is offered as weekly, monthly and yearly auto-renewable subscriptions. Prices are shown in the app before purchase.</li><li>The yearly plan may include a free trial. Any unused part of a trial is forfeited when you buy a subscription.</li><li>Payment is charged to your Apple Account at confirmation of purchase.</li><li>A subscription renews automatically unless it is turned off at least 24 hours before the end of the current period. Your account is charged for renewal within 24 hours before the end of the period.</li><li>You can manage or cancel subscriptions in Settings → Apple Account → Subscriptions. Refunds are handled by Apple.</li></ul>"),
        ("Estimates, not advice", "Fuel economy, cost per kilometre, mileage forecasts and reminders are calculated from the data you enter and may be inaccurate. Always follow your vehicle manufacturer’s maintenance schedule and legal deadlines such as insurance and inspection. We are not responsible for missed maintenance, fines or damage."),
        ("Your data", "Your data is stored on your device. You are responsible for keeping backups."),
        ("The app", "Stint is provided “as is”. We may change or remove features. To the maximum extent permitted by law, we are not liable for indirect or consequential damages arising from the use of the app."),
        ("Changes", "If these Terms change, we will update this page and the date above. Continuing to use Stint means you accept the updated Terms."),
    ],
    "ru": [
        (None, f"Пользуясь Stint, вы соглашаетесь с этими условиями и со <a href=\"{EULA}\">стандартным лицензионным соглашением Apple</a> (Licensed Application EULA)."),
        ("Бесплатно и Premium", "Бесплатная версия включает одну активную машину, до трёх планов обслуживания, полную историю и экспорт CSV. Stint Premium снимает ограничения и добавляет отчёты о стоимости километра, PDF-историю и дополнительные виджеты."),
        ("Подписки", "<ul><li>Stint Premium доступен как автопродлеваемая подписка на неделю, месяц и год. Цены показываются в приложении до покупки.</li><li>Годовой план может включать бесплатный пробный период. Неиспользованная часть пробного периода сгорает при покупке подписки.</li><li>Оплата списывается с вашего Apple Account при подтверждении покупки.</li><li>Подписка продлевается автоматически, если не отключить её не позднее чем за 24 часа до конца текущего периода. Плата за продление списывается в течение 24 часов до конца периода.</li><li>Управлять подпиской и отменить её можно в Настройках → Apple Account → Подписки. Возвраты обрабатывает Apple.</li></ul>"),
        ("Расчёты, а не рекомендации", "Расход, стоимость километра, прогноз пробега и напоминания считаются по данным, которые вы вводите, и могут быть неточными. Всегда следуйте регламенту производителя машины и юридическим срокам — страховки, техосмотра. Мы не отвечаем за пропущенное обслуживание, штрафы или ущерб."),
        ("Ваши данные", "Данные хранятся на вашем устройстве. За резервные копии отвечаете вы."),
        ("Приложение", "Stint предоставляется «как есть». Мы можем менять или убирать функции. В максимальной степени, допустимой законом, мы не несём ответственности за косвенный ущерб от использования приложения."),
        ("Изменения", "Если условия изменятся, мы обновим эту страницу и дату выше. Продолжая пользоваться Stint, вы принимаете обновлённые условия."),
    ],
    "uk": [
        (None, f"Користуючись Stint, ви погоджуєтеся з цими умовами та зі <a href=\"{EULA}\">стандартною ліцензійною угодою Apple</a> (Licensed Application EULA)."),
        ("Безкоштовно і Premium", "Безкоштовна версія включає одне активне авто, до трьох планів обслуговування, повну історію та експорт CSV. Stint Premium знімає обмеження й додає звіти про вартість кілометра, PDF-історію та додаткові віджети."),
        ("Підписки", "<ul><li>Stint Premium доступний як автоподовжувана підписка на тиждень, місяць і рік. Ціни показуються в застосунку до покупки.</li><li>Річний план може містити безкоштовний пробний період. Невикористана частина пробного періоду згорає під час покупки підписки.</li><li>Оплата списується з вашого Apple Account під час підтвердження покупки.</li><li>Підписка подовжується автоматично, якщо не вимкнути її щонайменше за 24 години до кінця поточного періоду. Плата за подовження списується протягом 24 годин до кінця періоду.</li><li>Керувати підпискою та скасувати її можна в Параметрах → Apple Account → Підписки. Повернення коштів обробляє Apple.</li></ul>"),
        ("Розрахунки, а не поради", "Витрата пального, вартість кілометра, прогноз пробігу й нагадування розраховуються за даними, які ви вводите, і можуть бути неточними. Завжди дотримуйтеся регламенту виробника авто та юридичних строків — страховки, техогляду. Ми не відповідаємо за пропущене обслуговування, штрафи чи шкоду."),
        ("Ваші дані", "Дані зберігаються на вашому пристрої. За резервні копії відповідаєте ви."),
        ("Застосунок", "Stint надається «як є». Ми можемо змінювати або прибирати функції. У максимальному обсязі, дозволеному законом, ми не несемо відповідальності за непрямі збитки від використання застосунку."),
        ("Зміни", "Якщо умови зміняться, ми оновимо цю сторінку й дату вище. Продовжуючи користуватися Stint, ви приймаєте оновлені умови."),
    ],
}


def prefix(lang):
    return "" if lang == "en" else f"{lang}/"


def depth(lang):
    return "" if lang == "en" else "../"


def lang_nav(lang, page):
    links = []
    for other in LANGS:
        href = f"{depth(lang)}{prefix(other)}{page}"
        current = ' aria-current="page"' if other == lang else ""
        links.append(f'<a href="{href}" lang="{other}"{current}>{LANG_NAMES[other]}</a>')
    return '<nav class="lang">' + "".join(links) + "</nav>"


def page(lang, name, title, body):
    root = depth(lang)
    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)} · Stint</title>
<link rel="icon" href="{root}icon.png">
<link rel="stylesheet" href="{root}style.css">
</head>
<body>
<main>
<header>
<a class="brand" href="{root}{prefix(lang)}index.html"><img src="{root}icon.png" alt="">Stint</a>
{lang_nav(lang, name)}
</header>
{body}
<footer>© 2026 Stint · <a href="mailto:{CONTACT}">{CONTACT}</a></footer>
</main>
</body>
</html>
"""


def document(lang, title, sections):
    ui = UI[lang]
    parts = [f"<h1>{html.escape(title)}</h1>", f'<p class="updated">{ui["updated"]}: {UPDATED[lang]}</p>']
    for heading, text in sections:
        if heading:
            parts.append(f"<h2>{html.escape(heading)}</h2>")
        parts.append(text if text.startswith("<ul>") else f"<p>{text}</p>")
    parts.append(f"<h2>{ui['contact']}</h2>")
    parts.append(f'<p><a href="mailto:{CONTACT}">{CONTACT}</a></p>')
    return "\n".join(parts)


def index(lang):
    ui = UI[lang]
    return f"""<h1>Stint</h1>
<p class="updated">{ui["tagline"]}</p>
<div class="links">
<a href="privacy.html">{ui["privacy"]}<span>{ui["privacy_hint"]}</span></a>
<a href="terms.html">{ui["terms"]}<span>{ui["terms_hint"]}</span></a>
</div>"""


def write(lang, name, content):
    folder = os.path.join(ROOT, prefix(lang))
    os.makedirs(folder, exist_ok=True)
    with open(os.path.join(folder, name), "w", encoding="utf-8") as file:
        file.write(content)


for lang in LANGS:
    ui = UI[lang]
    write(lang, "index.html", page(lang, "index.html", "Stint", index(lang)))
    write(lang, "privacy.html", page(lang, "privacy.html", ui["privacy"], document(lang, ui["privacy"], PRIVACY[lang])))
    write(lang, "terms.html", page(lang, "terms.html", ui["terms"], document(lang, ui["terms"], TERMS[lang])))
