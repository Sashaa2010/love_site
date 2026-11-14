from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Для тебя...</title>
    <!-- Винтажные шрифты с засечками и гротеск -->
    <link href="https://fonts.googleapis.com/css2?family=Cormorant+Infant:ital,wght@0,400;0,700;1,400&family=Oswald:wght@300;500&display=swap" rel="stylesheet">
    <style>
        :root {
            --wine: #4a0b13; /* Глубокий бордовый */
            --dark: #1a0507;
            --cream: #f4f1ea; /* Цвет бумаги/мрамора */
        }

        body {
            margin: 0;
            padding: 0;
            background-color: var(--wine);
            color: var(--cream);
            font-family: 'Cormorant Infant', serif;
            overflow: hidden; /* Чтобы не было скролла */
        }

        /* Контейнер слайдов */
        .slides-container {
            position: relative;
            width: 100vw;
            height: 100vh;
        }

        .slide {
            position: absolute;
            top: 0; left: 0;
            width: 100%;
            height: 100%;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            padding: 20px;
            box-sizing: border-box;
            opacity: 0;
            transition: opacity 1s ease-in-out;
            pointer-events: none; /* Неактивные слайды не кликабельны */
            text-align: center;
        }

        .slide.active {
            opacity: 1;
            pointer-events: auto;
        }

        /* Стили для фото */
        .slide img {
            max-width: 90%;
            max-height: 60vh;
            object-fit: contain;
            border-radius: 10px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.5);
            margin-bottom: 20px;
            border: 2px solid rgba(244, 241, 234, 0.2);
        }

        /* Стили для текста */
        .slide h2 {
            font-size: clamp(1.5rem, 5vw, 3rem);
            font-weight: 400;
            margin: 0 0 20px 0;
            line-height: 1.2;
            max-width: 800px;
            font-style: italic;
        }

        /* Текст на 4 слайде (винтажный журнал) */
        .vintage-text {
            font-family: 'Oswald', sans-serif;
            font-weight: 300;
            text-transform: uppercase;
            letter-spacing: 3px;
            font-size: clamp(1.2rem, 4vw, 2rem);
            line-height: 1.8;
            border-top: 1px solid var(--cream);
            border-bottom: 1px solid var(--cream);
            padding: 40px 20px;
            max-width: 800px;
        }

        .vintage-text span {
            display: block;
            font-family: 'Cormorant Infant', serif;
            font-style: italic;
            text-transform: none;
            letter-spacing: 1px;
            font-size: 0.9em;
            margin-top: 15px;
            color: #d1b8ba;
        }

        /* Кнопки */
        .buttons {
            margin-top: 30px;
            display: flex;
            gap: 20px;
            position: relative;
            width: 100%;
            justify-content: center;
        }

        button {
            background: transparent;
            border: 2px solid var(--cream);
            color: var(--cream);
            padding: 15px 40px;
            font-family: 'Oswald', sans-serif;
            font-size: 1.2rem;
            text-transform: uppercase;
            letter-spacing: 2px;
            cursor: pointer;
            transition: all 0.3s ease;
            border-radius: 5px;
        }

        button:hover {
            background: var(--cream);
            color: var(--wine);
        }

        #btn-yes {
            background: var(--cream);
            color: var(--wine);
        }

        #btn-no {
            /* Позиционирование для убегания */
            position: relative;}

        /* Кнопка Далее */
        .next-btn {
            position: absolute;
            bottom: 30px;
            right: 30px;
            background: var(--cream);
            color: var(--wine);
            border: none;
            padding: 10px 20px;
            font-size: 1rem;
            cursor: pointer;
            z-index: 10;
        }

        /* Финал (сердечко) */
        .final-text {
            font-size: clamp(1.8rem, 6vw, 3.5rem);
            color: #ffb6c1; /* Нежно-розовый */
            margin-top: 20px;
        }

        /* Адаптация под телефоны */
        @media (max-width: 768px) {
            .slide img {
                max-height: 50vh;
            }
            .slide h2 {
                font-size: 1.8rem;
            }
            .next-btn {
                bottom: 20px;
                right: 20px;
            }
        }
    </style>
</head>
<body>

    <div class="slides-container">
        
        <!-- Слайд 1: Роза -->
        <div class="slide active">
            <img src="/static/rose.jpg" alt="Роза">
            <h2>Ксюш, ты стала мне очень близка...</h2>
        </div>

        <!-- Слайд 2: Скрин 1 -->
        <div class="slide">
            <img src="/static/screen1.jpg" alt="Доброе утро">
            <h2>Ты стала причиной, по которой я просыпаюсь каждый день с улыбкой</h2>
        </div>

        <!-- Слайд 3: Скрин 2 -->
        <div class="slide">
            <img src="/static/screen2.jpg" alt="Сладких снов">
            <h2>И причиной, по которой я засыпаю с такой же улыбкой</h2>
        </div>

        <!-- Слайд 4: Винтажный текст -->
        <div class="slide">
            <div class="vintage-text">
                Я всегда жду твоего сообщения
                <span>мне в радость проводить с тобой время</span>
            </div>
        </div>

        <!-- Слайд 5: Котята -->
        <div class="slide">
            <img src="/static/cats.jpg" alt="Котята">
            <h2>Ты стала очень близка мне, мне с тобой очень хорошо и комфортно</h2>
        </div>

        <!-- Слайд 6: Луна -->
        <div class="slide">
            <img src="/static/moon.jpg" alt="Луна">
            <h2>Ты очень красивая, очень хорошая, ты самая лучшая. Ты как свет луны в моем темном мире, как ангел, который спустился с небес</h2>
        </div>

        <!-- Слайд 7: Вопрос -->
        <div class="slide">
            <h2 style="font-size: clamp(2rem, 7vw, 4rem); margin-bottom: 40px;">А теперь вопрос, который важный для меня и, может быть, для тебя...<br><br><span style="color: #ffb6c1;">Ты будешь моей девушкой?</span></h2>
            <div class="buttons" id="button-container">
                <button id="btn-yes">Да</button>
                <button id="btn-no">Нет</button>
            </div>
        </div>

        <!-- Слайд 8: Финал -->
        <div class="slide" id="final-slide">
            <img src="/static/heart.png" alt="Сердце" style="max-height: 30vh; border: none; box-shadow: none;">
            <h2 class="final-text">Я рада, что ты решила стать моей девушкой. Я люблю тебя, мышонок. Спасибо, что ты есть у меня ❤️</h2>
        </div>

        <!-- Кнопка "Далее" -->
        <button class="next-btn" id="next-btn">Далее ➔</button>

    </div>

    <script>
        const slides = document.querySelectorAll('.slide');
        const nextBtn = document.getElementById('next-btn');
        let currentSlide = 0;

        // Логика перелистывания
        nextBtn.addEventListener('click', () => {
            if (currentSlide < slides.length - 1) {
                slides[currentSlide].classList.remove('active');
                currentSlide++;
                slides[currentSlide].classList.add('active');
                
                // Если дошли до вопроса, скрываем кнопку Далее
                if (currentSlide === 6) {
                    nextBtn.style.display = 'none';
                }
            }
        });

        // Логика убегания кнопки "Нет"const btnNo = document.getElementById('btn-no');
        
        const moveButton = () => {
            // Получаем случайные координаты в пределах экрана
            const x = Math.random() * (window.innerWidth - btnNo.offsetWidth - 20);
            const y = Math.random() * (window.innerHeight - btnNo.offsetHeight - 20);
            
            btnNo.style.position = 'fixed';
            btnNo.style.left = x + 'px';
            btnNo.style.top = y + 'px';
        };

        // Убегает при наведении мыши (для ПК)
        btnNo.addEventListener('mouseenter', moveButton);
        // Убегает при клике (для телефонов)
        btnNo.addEventListener('touchstart', (e) => {
            e.preventDefault();
            moveButton();
        });
        btnNo.addEventListener('click', (e) => {
            e.preventDefault();
            moveButton();
        });

        // Логика кнопки "Да"
        const btnYes = document.getElementById('btn-yes');
        btnYes.addEventListener('click', () => {
            // Скрываем текущий слайд
            slides[currentSlide].classList.remove('active');
            // Показываем финальный
            document.getElementById('final-slide').classList.add('active');
        });
    </script>
</body>
    </html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(debug=True , port=8080)