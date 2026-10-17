import html
import os

CONTACT = "appdev8661@gmail.com"
UPDATED = {"en": "October 15, 2026", "ru": "15 октября 2026", "uk": "15 жовтня 2026", "de": "15. Oktober 2026"}
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
        ("Was auf deinem Gerät bleibt", "Deine Autos, Tankvorgänge und anderen Einträge, Kilometerstände, Wartungspläne, Erinnerungen sowie Fotos von Autos und Belegen werden im privaten Speicher der App auf deinem iPhone gespeichert. Sie sind gemäß deinen iCloud- oder Computer-Einstellungen in den Gerätebackups enthalten. Wir haben keinen Zugriff darauf."),
        ("iCloud-Synchronisierung", "Wenn du bei iCloud angemeldet bist, speichert Stint eine Kopie deiner Daten in deiner privaten iCloud-Datenbank, damit sie auf all deinen Geräten erscheinen und eine Neuinstallation überstehen. Diese Kopie speichert Apple unter deinem Apple Account; wir haben keinen Zugriff darauf. Du kannst iCloud für Stint unter Einstellungen → Apple Account → iCloud ausschalten."),
        ("Kamera und Fotos", "Stint nutzt die Kamera oder die Fotoauswahl nur, wenn du ein Foto deines Autos oder eines Belegs hinzufügst. Über die Fotoauswahl erhält die App nur Zugriff auf die Fotos, die du auswählst. Fotos werden komprimiert, auf deinem Gerät gespeichert und bei aktivem iCloud mit deinen übrigen Daten in deiner privaten iCloud-Datenbank gesichert."),
        ("Mitteilungen", "Erinnerungen – auch die Erinnerung vor dem Ende eines kostenlosen Testzeitraums – werden lokal auf deinem iPhone geplant. Es werden keine Push-Server verwendet."),
        ("Widgets, Siri und Kurzbefehle", "Widgets lesen eine kurze Zusammenfassung, die die App in einen Container schreibt, den nur Stint und seine Widgets auf deinem Gerät teilen. Anfragen an Siri und Kurzbefehle verarbeitet Apple gemäß der Datenschutzrichtlinie von Apple; Stint erhält nur die Werte aus deiner Anfrage, etwa einen Betrag oder einen Kilometerstand."),
        ("Käufe", "Abos werden von Apple abgewickelt. Wir erhalten keine Zahlungsdaten. Die App prüft den Abo-Status über StoreKit auf dem Gerät."),
        ("Export und Import", "CSV- und PDF-Dateien werden auf deinem Gerät erstellt und nur dorthin geteilt, wohin du sie selbst sendest. Wenn du eine Datei importierst, liest Stint nur die Datei, die du auswählst, auf deinem Gerät, übernimmt die Einträge in dein Logbuch und speichert oder sendet die Datei selbst nicht."),
        ("Daten löschen", "Einträge und Autos kannst du in der App löschen. Wenn du die App löschst, werden alle ihre Daten von deinem Gerät entfernt; Daten in iCloud verschwinden, wenn du sie in der App oder in den iCloud-Speichereinstellungen löschst."),
        ("Kinder", "Stint richtet sich nicht an Kinder unter 13 Jahren und erhebt wissentlich keine Informationen über sie."),
        ("Änderungen", "Ändert sich diese Erklärung, aktualisieren wir diese Seite und das Datum oben."),
    ],
    "en": [
        (None, "Stint does not collect personal data. There is no account, no sign-in, no analytics, no advertising and no tracking. We do not run servers that receive your data."),
        ("What stays on your device", "Your cars, refuels and other entries, odometer readings, service plans, reminders and photos of cars and receipts are stored in the app’s private storage on your iPhone. They are included in your device backups according to your iCloud or computer backup settings. We cannot access them."),
        ("iCloud sync", "If you are signed in to iCloud, Stint keeps a copy of your data in your private iCloud database so it appears on all your devices and survives reinstalling the app. This copy is stored by Apple under your Apple Account and is protected by it; we have no access to it. You can turn off iCloud for Stint in Settings → Apple Account → iCloud."),
        ("Camera and photos", "Stint uses the camera or the photo picker only when you add a photo of your car or a receipt. The photo picker gives the app access only to the photos you choose. Photos are compressed, kept on your device and, when iCloud is on, synced with the rest of your data to your private iCloud database."),
        ("Notifications", "Reminders, including the reminder before a free trial ends, are scheduled locally on your iPhone. No push servers are involved."),
        ("Widgets, Siri and Shortcuts", "Widgets read a short summary that the app writes to a container shared only between Stint and its widgets on your device. Siri and Shortcuts requests are processed by Apple under Apple’s privacy policy; Stint receives only the values from your request, such as an amount or an odometer reading."),
        ("Purchases", "Subscriptions are processed by Apple. We do not receive your payment details. The app checks your subscription status through Apple’s StoreKit on the device."),
        ("Export and import", "CSV and PDF files are created on your device and are shared only where you choose to send them. When you import a file, Stint reads only the file you pick, on your device, adds its entries to your log and does not keep or send the file itself."),
        ("Deleting your data", "You can delete entries and cars in the app. Deleting the app removes all of its data from your device; data in iCloud is removed when you delete it in the app or in iCloud storage settings."),
        ("Children", "Stint is not directed at children under 13 and does not knowingly collect any information from them."),
        ("Changes", "If this policy changes, we will update this page and the date above."),
    ],
    "ru": [
        (None, "Stint не собирает персональные данные. Нет аккаунта, входа, аналитики, рекламы и трекинга. У нас нет серверов, которые получают ваши данные."),
        ("Что остаётся на устройстве", "Машины, заправки и другие записи, пробег, планы обслуживания, напоминания, фото машин и чеков хранятся в закрытом хранилище приложения на вашем iPhone. Они попадают в резервные копии устройства в соответствии с вашими настройками iCloud или компьютера. У нас к ним доступа нет."),
        ("Синхронизация iCloud", "Если вы вошли в iCloud, Stint хранит копию данных в вашей личной базе iCloud, чтобы они были на всех ваших устройствах и сохранялись после переустановки. Эту копию хранит Apple в вашем Apple Account; у нас к ней доступа нет. Отключить iCloud для Stint можно в Настройках → Apple Account → iCloud."),
        ("Камера и фото", "Stint использует камеру или выбор фото, только когда вы добавляете фото машины или чека. Через выбор фото приложение получает доступ лишь к тем снимкам, которые вы выбрали. Фото сжимаются, хранятся на устройстве и, если включён iCloud, вместе с остальными данными попадают в вашу личную базу iCloud."),
        ("Уведомления", "Напоминания — в том числе напоминание перед концом бесплатного пробного периода — планируются локально на iPhone. Push-серверы не используются."),
        ("Виджеты, Siri и Быстрые команды", "Виджеты читают короткую сводку, которую приложение записывает в контейнер, общий только для Stint и его виджетов на вашем устройстве. Запросы Siri и Быстрых команд обрабатывает Apple по своей политике конфиденциальности; Stint получает только значения из запроса — например, сумму или пробег."),
        ("Покупки", "Подписки обрабатывает Apple. Мы не получаем ваши платёжные данные. Приложение проверяет статус подписки через StoreKit на устройстве."),
        ("Экспорт и импорт", "Файлы CSV и PDF создаются на устройстве и отправляются только туда, куда вы их отправите сами. При импорте Stint читает на устройстве только выбранный вами файл, добавляет записи в журнал и не сохраняет и не отправляет сам файл."),
        ("Удаление данных", "Записи и машины можно удалить в приложении. Удаление приложения стирает все его данные с устройства; данные в iCloud удаляются, когда вы удаляете их в приложении или в настройках хранилища iCloud."),
        ("Дети", "Stint не предназначен для детей младше 13 лет и сознательно не собирает о них никакой информации."),
        ("Изменения", "Если политика изменится, мы обновим эту страницу и дату выше."),
    ],
    "uk": [
        (None, "Stint не збирає персональні дані. Немає акаунта, входу, аналітики, реклами й трекінгу. У нас немає серверів, які отримують ваші дані."),
        ("Що залишається на пристрої", "Авто, заправки та інші записи, пробіг, плани обслуговування, нагадування, фото авто й чеків зберігаються в закритому сховищі застосунку на вашому iPhone. Вони потрапляють до резервних копій пристрою відповідно до ваших налаштувань iCloud або компʼютера. Ми не маємо до них доступу."),
        ("Синхронізація iCloud", "Якщо ви увійшли в iCloud, Stint зберігає копію даних у вашій особистій базі iCloud, щоб вони були на всіх ваших пристроях і зберігалися після перевстановлення. Цю копію зберігає Apple у вашому Apple Account; ми не маємо до неї доступу. Вимкнути iCloud для Stint можна в Параметрах → Apple Account → iCloud."),
        ("Камера і фото", "Stint використовує камеру або вибір фото лише тоді, коли ви додаєте фото авто чи чека. Через вибір фото застосунок отримує доступ тільки до знімків, які ви обрали. Фото стискаються, зберігаються на пристрої і, якщо ввімкнено iCloud, разом з іншими даними потрапляють у вашу особисту базу iCloud."),
        ("Сповіщення", "Нагадування — зокрема нагадування перед завершенням безкоштовного пробного періоду — плануються локально на iPhone. Push-сервери не використовуються."),
        ("Віджети, Siri та Швидкі команди", "Віджети читають коротке зведення, яке застосунок записує в контейнер, спільний лише для Stint і його віджетів на вашому пристрої. Запити Siri та Швидких команд обробляє Apple згідно зі своєю політикою конфіденційності; Stint отримує лише значення із запиту — наприклад, суму чи пробіг."),
        ("Покупки", "Підписки обробляє Apple. Ми не отримуємо ваших платіжних даних. Застосунок перевіряє статус підписки через StoreKit на пристрої."),
        ("Експорт та імпорт", "Файли CSV і PDF створюються на пристрої та надсилаються лише туди, куди ви їх надішлете самі. Під час імпорту Stint читає на пристрої лише обраний вами файл, додає записи до журналу й не зберігає та не надсилає сам файл."),
        ("Видалення даних", "Записи й авто можна видалити в застосунку. Видалення застосунку стирає всі його дані з пристрою; дані в iCloud видаляються, коли ви видаляєте їх у застосунку або в налаштуваннях сховища iCloud."),
        ("Діти", "Stint не призначений для дітей до 13 років і свідомо не збирає про них жодної інформації."),
        ("Зміни", "Якщо політика зміниться, ми оновимо цю сторінку й дату вище."),
    ],
}

TERMS = {
    "de": [
        (None, f"Mit der Nutzung von Stint stimmst du diesen Bedingungen und Apples <a href=\"{EULA}\">Endbenutzer-Lizenzvertrag für lizenzierte Apps</a> zu."),
        ("Kostenlos und Pro", "Die kostenlose Version umfasst ein aktives Auto, bis zu drei Wartungspläne, den vollständigen Verlauf sowie CSV-Import und -Export. Stint Pro hebt die Grenzen auf und ergänzt Berichte zu den Kosten pro Kilometer, den PDF-Verlauf und zusätzliche Widgets."),
        ("Abos", "<ul><li>Stint Pro wird als automatisch verlängerbares Wochen-, Monats- und Jahresabo angeboten. Die Preise werden vor dem Kauf in der App angezeigt.</li><li>Das Jahresabo kann einen kostenlosen Testzeitraum enthalten. Ein ungenutzter Teil des Testzeitraums verfällt mit dem Kauf eines Abos.</li><li>Die Zahlung wird bei Bestätigung des Kaufs deinem Apple Account belastet.</li><li>Das Abo verlängert sich automatisch, wenn es nicht mindestens 24 Stunden vor Ende des aktuellen Zeitraums gekündigt wird. Die Verlängerung wird innerhalb von 24 Stunden vor Ende des Zeitraums berechnet.</li><li>Abos verwaltest und kündigst du unter Einstellungen → Apple Account → Abonnements. Erstattungen wickelt Apple ab.</li></ul>"),
        ("Berechnungen, keine Beratung", "Verbrauch, Kosten pro Kilometer, Laufleistungsprognosen und Erinnerungen werden aus deinen Eingaben berechnet und können ungenau sein. Halte dich immer an den Wartungsplan des Herstellers und an gesetzliche Fristen wie Versicherung und Hauptuntersuchung. Wir haften nicht für versäumte Wartung, Bußgelder oder Schäden."),
        ("Deine Daten", "Deine Daten werden auf deinem Gerät gespeichert. Für Backups bist du selbst verantwortlich: Mit dem CSV-Export sicherst du dein Logbuch, mit dem Import holst du es zurück."),
        ("Die App", "Stint wird „wie besehen“ bereitgestellt. Wir können Funktionen ändern oder entfernen. Soweit gesetzlich zulässig, haften wir nicht für indirekte oder Folgeschäden aus der Nutzung der App."),
        ("Änderungen", "Ändern sich diese Bedingungen, aktualisieren wir diese Seite und das Datum oben. Wenn du Stint weiter nutzt, akzeptierst du die aktualisierten Bedingungen."),
    ],
    "en": [
        (None, f"By using Stint you agree to these Terms and to Apple’s <a href=\"{EULA}\">Licensed Application End User License Agreement</a>."),
        ("Free and Pro", "The free version includes one active car, up to three service plans, the full history, and CSV import and export. Stint Pro removes the limits and adds cost-per-kilometre reports, the PDF history and additional widgets."),
        ("Subscriptions", "<ul><li>Stint Pro is offered as weekly, monthly and yearly auto-renewable subscriptions. Prices are shown in the app before purchase.</li><li>The yearly plan may include a free trial. Any unused part of a trial is forfeited when you buy a subscription.</li><li>Payment is charged to your Apple Account at confirmation of purchase.</li><li>A subscription renews automatically unless it is turned off at least 24 hours before the end of the current period. Your account is charged for renewal within 24 hours before the end of the period.</li><li>You can manage or cancel subscriptions in Settings → Apple Account → Subscriptions. Refunds are handled by Apple.</li></ul>"),
        ("Estimates, not advice", "Fuel economy, cost per kilometre, mileage forecasts and reminders are calculated from the data you enter and may be inaccurate. Always follow your vehicle manufacturer’s maintenance schedule and legal deadlines such as insurance and inspection. We are not responsible for missed maintenance, fines or damage."),
        ("Your data", "Your data is stored on your device. You are responsible for keeping backups: CSV export saves your log, and import brings it back."),
        ("The app", "Stint is provided “as is”. We may change or remove features. To the maximum extent permitted by law, we are not liable for indirect or consequential damages arising from the use of the app."),
        ("Changes", "If these Terms change, we will update this page and the date above. Continuing to use Stint means you accept the updated Terms."),
    ],
    "ru": [
        (None, f"Пользуясь Stint, вы соглашаетесь с этими условиями и со <a href=\"{EULA}\">стандартным лицензионным соглашением Apple</a> (Licensed Application EULA)."),
        ("Бесплатно и Pro", "Бесплатная версия включает одну активную машину, до трёх планов обслуживания, полную историю, импорт и экспорт CSV. Stint Pro снимает ограничения и добавляет отчёты о стоимости километра, PDF-историю и дополнительные виджеты."),
        ("Подписки", "<ul><li>Stint Pro доступен как автопродлеваемая подписка на неделю, месяц и год. Цены показываются в приложении до покупки.</li><li>Годовой план может включать бесплатный пробный период. Неиспользованная часть пробного периода сгорает при покупке подписки.</li><li>Оплата списывается с вашего Apple Account при подтверждении покупки.</li><li>Подписка продлевается автоматически, если не отключить её не позднее чем за 24 часа до конца текущего периода. Плата за продление списывается в течение 24 часов до конца периода.</li><li>Управлять подпиской и отменить её можно в Настройках → Apple Account → Подписки. Возвраты обрабатывает Apple.</li></ul>"),
        ("Расчёты, а не рекомендации", "Расход, стоимость километра, прогноз пробега и напоминания считаются по данным, которые вы вводите, и могут быть неточными. Всегда следуйте регламенту производителя машины и юридическим срокам — страховки, техосмотра. Мы не отвечаем за пропущенное обслуживание, штрафы или ущерб."),
        ("Ваши данные", "Данные хранятся на вашем устройстве. За резервные копии отвечаете вы: экспорт CSV сохраняет журнал, а импорт возвращает его обратно."),
        ("Приложение", "Stint предоставляется «как есть». Мы можем менять или убирать функции. В максимальной степени, допустимой законом, мы не несём ответственности за косвенный ущерб от использования приложения."),
        ("Изменения", "Если условия изменятся, мы обновим эту страницу и дату выше. Продолжая пользоваться Stint, вы принимаете обновлённые условия."),
    ],
    "uk": [
        (None, f"Користуючись Stint, ви погоджуєтеся з цими умовами та зі <a href=\"{EULA}\">стандартною ліцензійною угодою Apple</a> (Licensed Application EULA)."),
        ("Безкоштовно і Pro", "Безкоштовна версія включає одне активне авто, до трьох планів обслуговування, повну історію, імпорт та експорт CSV. Stint Pro знімає обмеження й додає звіти про вартість кілометра, PDF-історію та додаткові віджети."),
        ("Підписки", "<ul><li>Stint Pro доступний як автоподовжувана підписка на тиждень, місяць і рік. Ціни показуються в застосунку до покупки.</li><li>Річний план може містити безкоштовний пробний період. Невикористана частина пробного періоду згорає під час покупки підписки.</li><li>Оплата списується з вашого Apple Account під час підтвердження покупки.</li><li>Підписка подовжується автоматично, якщо не вимкнути її щонайменше за 24 години до кінця поточного періоду. Плата за подовження списується протягом 24 годин до кінця періоду.</li><li>Керувати підпискою та скасувати її можна в Параметрах → Apple Account → Підписки. Повернення коштів обробляє Apple.</li></ul>"),
        ("Розрахунки, а не поради", "Витрата пального, вартість кілометра, прогноз пробігу й нагадування розраховуються за даними, які ви вводите, і можуть бути неточними. Завжди дотримуйтеся регламенту виробника авто та юридичних строків — страховки, техогляду. Ми не відповідаємо за пропущене обслуговування, штрафи чи шкоду."),
        ("Ваші дані", "Дані зберігаються на вашому пристрої. За резервні копії відповідаєте ви: експорт CSV зберігає журнал, а імпорт повертає його назад."),
        ("Застосунок", "Stint надається «як є». Ми можемо змінювати або прибирати функції. У максимальному обсязі, дозволеному законом, ми не несемо відповідальності за непрямі збитки від використання застосунку."),
        ("Зміни", "Якщо умови зміняться, ми оновимо цю сторінку й дату вище. Продовжуючи користуватися Stint, ви приймаєте оновлені умови."),
    ],
}



UI2 = {
    "en": {
        "support": "Support", "support_hint": "Answers and a way to reach us",
        "doc": "Document", "hero_title": "Your car, looked after",
        "chips": ["Oil · in 4,200 km", "Insurance · Mar 12", "PDF for resale"],
        "faq": "Questions and answers", "write": "Write to us",
        "write_hint": "Didn’t find an answer? We reply within a couple of days. Please add your app version (Stint → Settings, at the bottom) and your iPhone model.",
        "subject": "Stint support", "legal": "Documents",
    },
    "ru": {
        "support": "Поддержка", "support_hint": "Ответы на вопросы и связь с нами",
        "doc": "Документ", "hero_title": "Машина под присмотром",
        "chips": ["Масло · через 4 200 км", "Страховка · 12 марта", "PDF для продажи"],
        "faq": "Вопросы и ответы", "write": "Написать нам",
        "write_hint": "Не нашли ответ? Отвечаем в течение пары дней. Укажите, пожалуйста, версию приложения (Stint → Настройки, в самом низу) и модель iPhone.",
        "subject": "Stint: поддержка", "legal": "Документы",
    },
    "uk": {
        "support": "Підтримка", "support_hint": "Відповіді на питання й звʼязок з нами",
        "doc": "Документ", "hero_title": "Авто під наглядом",
        "chips": ["Мастило · за 4 200 км", "Страховка · 12 березня", "PDF для продажу"],
        "faq": "Питання й відповіді", "write": "Написати нам",
        "write_hint": "Не знайшли відповідь? Відповідаємо протягом кількох днів. Вкажіть, будь ласка, версію застосунку (Stint → Налаштування, в самому низу) і модель iPhone.",
        "subject": "Stint: підтримка", "legal": "Документи",
    },
    "de": {
        "support": "Support", "support_hint": "Antworten und Kontakt",
        "doc": "Dokument", "hero_title": "Dein Auto bestens im Blick",
        "chips": ["Öl · in 4.200 km", "Versicherung · 12. März", "PDF für den Verkauf"],
        "faq": "Fragen und Antworten", "write": "Schreib uns",
        "write_hint": "Keine Antwort gefunden? Wir antworten innerhalb weniger Tage. Bitte nenne die App-Version (Stint → Einstellungen, ganz unten) und dein iPhone-Modell.",
        "subject": "Stint Support", "legal": "Dokumente",
    },
}

FAQ = {
    "en": [
        ("I got a new iPhone — where is my data?", "Sign in with the same Apple Account and keep iCloud on for Stint (Settings → your name → iCloud). On first launch Stint looks for your data in iCloud for a few seconds and brings your cars back. If sync has a problem, Stint shows it in Settings → Sync."),
        ("How do I restore my subscription?", "Open Stint → Settings → Subscription → Restore purchases. Use the same Apple Account you bought it with."),
        ("How do I cancel the subscription or the free trial?", "On your iPhone open Settings → Apple Account → Subscriptions, or Stint → Settings → Manage subscription. Cancel at least 24 hours before the period ends. Stint reminds you two days before a trial ends."),
        ("Reminders don’t arrive", "Allow notifications for Stint in iPhone Settings → Notifications. The reminder time is in Stint → Settings → Reminders. A plan needs a starting point: mark when you last did the service, then Stint can count the next date."),
        ("How do I move my log from Fuelio or Drivvo?", "Export a CSV in your old app. In Stint open Settings → Data → Import from another app and pick the file. Duplicates are skipped, and the last import can be undone."),
        ("How do I back up or export my data?", "Settings → Data → Export to CSV saves every log entry. A PDF history of a car (Pro) is in the car’s card. With iCloud on, everything is also kept in your private iCloud."),
        ("How do I delete my data?", "Delete entries and cars in the app: a car’s card has Delete. Deleting the app removes its data from the iPhone; the copy in iCloud can be removed in Settings → your name → iCloud → Manage Storage."),
    ],
    "ru": [
        ("Новый iPhone — где мои данные?", "Войдите в тот же Apple Account и оставьте iCloud для Stint включённым (Настройки → ваше имя → iCloud). При первом запуске Stint несколько секунд ищет данные в iCloud и возвращает машины. Если с синхронизацией что-то не так, Stint покажет это в Настройках → Синхронизация."),
        ("Как восстановить подписку?", "Откройте Stint → Настройки → Подписка → Восстановить покупки. Нужен тот же Apple Account, с которого была покупка."),
        ("Как отменить подписку или пробный период?", "На iPhone: Настройки → Apple Account → Подписки, или в Stint → Настройки → Управлять подпиской. Отмените не позже чем за 24 часа до конца периода. За два дня до конца пробного периода Stint напомнит."),
        ("Не приходят напоминания", "Разрешите уведомления для Stint в Настройках iPhone → Уведомления. Время напоминаний — в Stint → Настройки → Напоминания. Плану нужна точка отсчёта: отметьте, когда делали в последний раз, — тогда Stint посчитает следующий срок."),
        ("Как перенести журнал из Fuelio или Drivvo?", "Выгрузите CSV в старом приложении. В Stint откройте Настройки → Данные → Импорт из другого приложения и выберите файл. Повторы пропускаются, последний импорт можно отменить."),
        ("Как сделать резервную копию или выгрузить данные?", "Настройки → Данные → Экспорт в CSV сохраняет все записи журнала. PDF-история машины (Pro) — в карточке машины. С включённым iCloud всё хранится и в вашем личном iCloud."),
        ("Как удалить свои данные?", "Записи и машины удаляются в приложении — в карточке машины есть «Удалить». Удаление приложения стирает его данные с iPhone; копию в iCloud можно удалить в Настройках → ваше имя → iCloud → Управлять хранилищем."),
    ],
    "uk": [
        ("Новий iPhone — де мої дані?", "Увійдіть у той самий Apple Account і залиште iCloud для Stint увімкненим (Параметри → ваше імʼя → iCloud). Під час першого запуску Stint кілька секунд шукає дані в iCloud і повертає авто. Якщо із синхронізацією щось не так, Stint покаже це в Налаштуваннях → Синхронізація."),
        ("Як відновити підписку?", "Відкрийте Stint → Налаштування → Підписка → Відновити покупки. Потрібен той самий Apple Account, з якого була покупка."),
        ("Як скасувати підписку або пробний період?", "На iPhone: Параметри → Apple Account → Підписки, або в Stint → Налаштування → Керувати підпискою. Скасуйте щонайменше за 24 години до кінця періоду. За два дні до кінця пробного періоду Stint нагадає."),
        ("Не приходять нагадування", "Дозвольте сповіщення для Stint у Параметрах iPhone → Сповіщення. Час нагадувань — у Stint → Налаштування → Нагадування. Плану потрібна точка відліку: позначте, коли робили востаннє, — тоді Stint порахує наступний строк."),
        ("Як перенести журнал із Fuelio чи Drivvo?", "Вивантажте CSV у старому застосунку. У Stint відкрийте Налаштування → Дані → Імпорт з іншого застосунку й оберіть файл. Повтори пропускаються, останній імпорт можна скасувати."),
        ("Як зробити резервну копію або вивантажити дані?", "Налаштування → Дані → Експорт у CSV зберігає всі записи журналу. PDF-історія авто (Pro) — у картці авто. З увімкненим iCloud усе зберігається й у вашому особистому iCloud."),
        ("Як видалити свої дані?", "Записи й авто видаляються в застосунку — у картці авто є «Видалити». Видалення застосунку стирає його дані з iPhone; копію в iCloud можна видалити в Параметрах → ваше імʼя → iCloud → Керувати сховищем."),
    ],
    "de": [
        ("Neues iPhone – wo sind meine Daten?", "Melde dich mit demselben Apple Account an und lass iCloud für Stint eingeschaltet (Einstellungen → dein Name → iCloud). Beim ersten Start sucht Stint einige Sekunden in iCloud nach deinen Daten und holt deine Autos zurück. Gibt es ein Problem mit der Synchronisierung, zeigt Stint es unter Einstellungen → Synchronisierung."),
        ("Wie stelle ich mein Abo wieder her?", "Öffne Stint → Einstellungen → Abo → Käufe wiederherstellen. Nutze denselben Apple Account wie beim Kauf."),
        ("Wie kündige ich das Abo oder die Testphase?", "Auf dem iPhone unter Einstellungen → Apple Account → Abonnements oder in Stint → Einstellungen → Abo verwalten. Kündige mindestens 24 Stunden vor Ende des Zeitraums. Zwei Tage vor Ende der Testphase erinnert dich Stint."),
        ("Erinnerungen kommen nicht an", "Erlaube Mitteilungen für Stint in den iPhone-Einstellungen → Mitteilungen. Die Uhrzeit der Erinnerungen findest du in Stint → Einstellungen → Erinnerungen. Ein Plan braucht einen Startpunkt: Trage ein, wann du die Wartung zuletzt gemacht hast, dann berechnet Stint den nächsten Termin."),
        ("Wie übernehme ich mein Logbuch aus Fuelio oder Drivvo?", "Exportiere in der alten App eine CSV-Datei. Öffne in Stint Einstellungen → Daten → Aus anderer App importieren und wähle die Datei. Doppelte Einträge werden übersprungen, der letzte Import lässt sich rückgängig machen."),
        ("Wie sichere oder exportiere ich meine Daten?", "Einstellungen → Daten → Als CSV exportieren speichert alle Einträge. Den PDF-Verlauf eines Autos (Pro) findest du in der Karte des Autos. Mit iCloud wird zusätzlich alles in deiner privaten iCloud gespeichert."),
        ("Wie lösche ich meine Daten?", "Einträge und Autos löschst du in der App – in der Karte des Autos gibt es „Löschen“. Wenn du die App löschst, werden ihre Daten vom iPhone entfernt; die Kopie in iCloud löschst du unter Einstellungen → dein Name → iCloud → Speicher verwalten."),
    ],
}

WAGON = "M8,70 C8,60 12,54 24,52 L64,47 C72,40 86,28 100,27 L212,26 C220,26 224,30 226,36 L232,54 L232,72 C232,74 230,76 228,76 L12,76 C10,76 8,74 8,72 Z"

CHEVRON = '<svg class="chev" width="8" height="14" viewBox="0 0 8 14" aria-hidden="true"><path d="M1 1l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>'


def prefix(lang):
    return "" if lang == "en" else f"{lang}/"


def depth(lang):
    return "" if lang == "en" else "../"


def lang_nav(lang, page):
    links = []
    for other in LANGS:
        href = f"{depth(lang)}{prefix(other)}{page}"
        current = ' aria-current="page"' if other == lang else ""
        links.append(f'<a href="{href}" lang="{other}" hreflang="{other}"{current}>{LANG_NAMES[other]}</a>')
    return '<nav class="lang" aria-label="Language">' + "".join(links) + "</nav>"


def page(lang, name, title, body, description):
    root = depth(lang)
    ui, extra = UI[lang], UI2[lang]
    alternates = "\n".join(f'<link rel="alternate" hreflang="{other}" href="{depth(lang)}{prefix(other)}{name}">' for other in LANGS)
    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="color-scheme" content="light dark">
<meta name="description" content="{html.escape(description)}">
<title>{html.escape(title)} · Stint</title>
{alternates}
<link rel="icon" href="{root}icon.png">
<link rel="apple-touch-icon" href="{root}icon.png">
<link rel="stylesheet" href="{root}style.css">
</head>
<body>
<main>
<header>
<a class="brand" href="{root}{prefix(lang)}index.html"><img src="{root}icon.png" alt="" width="40" height="40">Stint</a>
{lang_nav(lang, name)}
</header>
{body}
<footer>
<nav aria-label="{html.escape(extra['legal'])}">
<a href="privacy.html">{html.escape(ui['privacy'])}</a>
<a href="terms.html">{html.escape(ui['terms'])}</a>
<a href="support.html">{html.escape(extra['support'])}</a>
</nav>
<p>© 2026 Stint</p>
</footer>
</main>
</body>
</html>
"""


def document(lang, title, sections):
    ui, extra = UI[lang], UI2[lang]
    parts = [
        f'<p class="eyebrow">{html.escape(extra["doc"])} · {ui["updated"]} {UPDATED[lang]}</p>',
        f"<h1>{html.escape(title)}</h1>",
    ]
    for heading, text in sections:
        body = text if text.startswith("<ul>") else f"<p>{text}</p>"
        if heading:
            parts.append(f'<section class="card"><h2>{html.escape(heading)}</h2>{body}</section>')
        else:
            parts.append(f'<p class="lead">{text}</p>')
    parts.append(f'<section class="card"><h2>{ui["contact"]}</h2><p><a href="mailto:{CONTACT}">{CONTACT}</a></p></section>')
    return "\n".join(parts)


def hero(lang):
    chips = UI2[lang]["chips"]
    return f"""<div class="hero" aria-hidden="true">
<span class="chip c1"><i class="dot"></i>{html.escape(chips[0])}</span>
<span class="chip c2"><i class="dot calm"></i>{html.escape(chips[1])}</span>
<span class="chip c3 dark"><svg width="11" height="11" viewBox="0 0 24 24"><path d="M7 3h7l5 5v13H7z M14 3v5h5" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linejoin="round"/></svg>{html.escape(chips[2])}</span>
<svg class="car" viewBox="0 0 240 96"><path d="{WAGON}"/><circle cx="58" cy="76" r="16" class="ground"/><circle cx="186" cy="76" r="16" class="ground"/><circle cx="58" cy="76" r="13" class="wheel"/><circle cx="186" cy="76" r="13" class="wheel"/><circle cx="58" cy="76" r="5" class="hub"/><circle cx="186" cy="76" r="5" class="hub"/></svg>
</div>"""


def group(rows):
    items = "".join(f'<a class="row" href="{href}"><span><b>{html.escape(title)}</b><small>{html.escape(hint)}</small></span>{CHEVRON}</a>' for href, title, hint in rows)
    return f'<nav class="group">{items}</nav>'


def index(lang):
    ui, extra = UI[lang], UI2[lang]
    return f"""{hero(lang)}
<h1>{html.escape(extra["hero_title"])}</h1>
<p class="lead">{html.escape(ui["tagline"])}</p>
{group([
    ("support.html", extra["support"], extra["support_hint"]),
    ("privacy.html", ui["privacy"], ui["privacy_hint"]),
    ("terms.html", ui["terms"], ui["terms_hint"]),
])}"""


def support(lang):
    extra = UI2[lang]
    from urllib.parse import quote
    mail = f"mailto:{CONTACT}?subject={quote(extra['subject'])}"
    faq = "".join(
        f'<details><summary><span>{html.escape(q)}</span>{CHEVRON}</summary><p>{html.escape(a)}</p></details>'
        for q, a in FAQ[lang]
    )
    return f"""<p class="eyebrow">Stint</p>
<h1>{html.escape(extra["support"])}</h1>
<p class="lead">{html.escape(extra["support_hint"])}</p>
<h2 class="section">{html.escape(extra["faq"])}</h2>
<div class="group faq">{faq}</div>
<h2 class="section">{html.escape(extra["write"])}</h2>
<section class="card">
<p>{html.escape(extra["write_hint"])}</p>
<a class="button" href="{mail}">{html.escape(extra["write"])}</a>
<p class="mail"><a href="{mail}">{CONTACT}</a></p>
</section>"""


def write(lang, name, content):
    folder = os.path.join(ROOT, prefix(lang))
    os.makedirs(folder, exist_ok=True)
    with open(os.path.join(folder, name), "w", encoding="utf-8") as file:
        file.write(content)


for lang in LANGS:
    ui, extra = UI[lang], UI2[lang]
    write(lang, "index.html", page(lang, "index.html", "Stint", index(lang), ui["tagline"]))
    write(lang, "privacy.html", page(lang, "privacy.html", ui["privacy"], document(lang, ui["privacy"], PRIVACY[lang]), ui["privacy_hint"]))
    write(lang, "terms.html", page(lang, "terms.html", ui["terms"], document(lang, ui["terms"], TERMS[lang]), ui["terms_hint"]))
    write(lang, "support.html", page(lang, "support.html", extra["support"], support(lang), extra["support_hint"]))
