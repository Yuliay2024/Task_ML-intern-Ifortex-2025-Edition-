# Text Summarizer App

Реализовано веб-приложение Streamlit, которое использует библиотеку Hugging Face Transformers для генерации самари текста с использованием модели BART.

## Использование

1. GitHub:

   ```bash
   
   
2. Установка зависимостей:
   
    ```bash
   pip install -r requirements.txt

3. Запуск приложения:
   
   ```bash
   streamlit run app.py


# Зависимости
**Streamlit:** Фреймворк для создания интерактивных веб-приложений.

**Transformers:** Hugging Face библиотека для работа с NLP.

# Как это работает
Приложение позволяет ввести пользователю текст в поле ввода и после нажатия кнопки "Generate Summary" сгенерировать самари (поле Summary)

## T5/BART
Обе модели основаны на архитектуре Transformer (encoder-decoder) и являются мощными языковыми моделями, которые отлично справляются с различными задачами обработки естественного языка. 
Плюсы для использования:
+ Универсальность (одна архитектура для множества задач).
+ Возможность использования предобученных весов.
+ Хорошая адаптация к новым задачам с минимальным дообучением.

Самари сгенерированное BART логичное и передает содержание текста:
Самари сгенерированное BART:
Many financial institutions started building conversational AI as part of a digital transformation initiative. As the pandemic hit, the need changed as contact centers were put under increased pressures. New use cases came about as a result of Covid-19 that accelerated adoption.

Самари сгенерированное T5:
financial institutions started building conversational AI, prior to the Covid19 pandemic . they were looking for ways to automate solutions to help get back to “normal” levels of customer service . this resulted in a change from the “future of conversational . AI” to a real tactical assistant that can help in customer service.

