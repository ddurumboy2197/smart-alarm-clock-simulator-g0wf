Men sizga 50 ta masalani hal qilish uchun yordam beraman. Har bir masala uchun toza va optimal kodni bering.

### 1. Smart Alarm Clock Simulator
```python
import datetime

def smart_alarm(alarm_time):
    current_time = datetime.datetime.now()
    if current_time.hour == alarm_time.hour and current_time.minute == alarm_time.minute:
        print("Uygun vaqtda! Uyg'onish vaqti.")
    else:
        print("Uyg'onish vaqti yetib kelmadi.")

alarm_time = datetime.datetime.now() + datetime.timedelta(hours=8)
smart_alarm(alarm_time)
```

### 2. Daily Water Intake Tracker
```python
import datetime

def daily_water_intake():
    current_time = datetime.datetime.now()
    water_intake = 0
    while True:
        print(f"{current_time.strftime('%H:%M')}: Suv ichishni kuzatamiz.")
        water_intake += 1
        current_time += datetime.timedelta(minutes=1)
        if current_time.hour == 23 and current_time.minute == 59:
            print(f"Haftalik grafik: {water_intake} martaba suv ichildi.")
            break

daily_water_intake()
```

### 3. Sleep Cycle Analyzer
```python
import datetime

def sleep_cycle():
    sleep_time = int(input("Uyqun vaqti (soat): "))
    wake_up_time = sleep_time + 7
    print(f"Eng yaxshi uyg'onish vaqti: {wake_up_time}:00")

sleep_cycle()
```

### 4. Habit Streak Tracker
```python
import datetime

def habit_streak():
    habit = input("Odatni kiriting (sport, o'qish, ...): ")
    streak = 0
    while True:
        print(f"{datetime.datetime.now().strftime('%H:%M')}: {habit}ni kuzatamiz.")
        streak += 1
        if streak == 7:
            print(f"Haftalik streak: {streak} kun")
        elif streak == 30:
            print(f"Oylik streak: {streak} kun")
        elif streak == 365:
            print(f"Yillik streak: {streak} kun")
        else:
            continue

habit_streak()
```

### 5. Meal Planner with Shopping List
```python
import datetime

def meal_planner():
    breakfast = input("Oshga kiriting: ")
    lunch = input("Ichki ovqatga kiriting: ")
    dinner = input("Kechki ovqatga kiriting: ")
    shopping_list = [breakfast, lunch, dinner]
    print("Xarid ro'yxati:")
    for item in shopping_list:
        print(item)

meal_planner()
```

### 6. Plant Care Reminder System
```python
import datetime

def plant_care():
    plant_name = input("O'simlik nomini kiriting: ")
    watering_time = int(input("Sug'orish vaqti (soat): "))
    fertilizing_time = int(input("O'g'itlash vaqti (soat): "))
    while True:
        current_time = datetime.datetime.now()
        if current_time.hour == watering_time:
            print(f"{plant_name}ga sug'orish vaqti!")
        elif current_time.hour == fertilizing_time:
            print(f"{plant_name}ga o'g'itlash vaqti!")
        else:
            continue

plant_care()
```

### 7. Book Reading Progress Tracker
```python
import datetime

def book_reading_progress():
    book_name = input("Kitob nomini kiriting: ")
    page_number = int(input("Sahifa sonini kiriting: "))
    total_pages = int(input("Jami sahifa sonini kiriting: "))
    progress = (page_number / total_pages) * 100
    print(f"{book_name}ning o'qish progressi: {progress}%")
    remaining_days = (total_pages - page_number) / (page_number / 30)
    print(f"Kitob tugashiga nechun kun qoldi: {remaining_days} kun")

book_reading_progress()
```

### 8. Language Learning Flashcard App
```python
import random

def language_learning_flashcard():
    word = input("So'zni kiriting: ")
    translation = input("Tarjimani kiriting: ")
    flashcard = [word, translation]
    random.shuffle(flashcard)
    print(flashcard[0])
    answer = input("Javobni kiriting: ")
    if answer == flashcard[1]:
        print("To'g'ri javob!")
    else:
        print("Xato javob!")

language_learning_flashcard()
```

### 9. Pomodoro Timer with Statistics
```python
import datetime

def pomodoro_timer():
    work_time = int(input("Ish vaqti (daqiqa): "))
    break_time = int(input("Dam olish vaqti (daqiqa): "))
    total_work_time = 0
    total_break_time = 0
    while True:
        print(f"{datetime.datetime.now().strftime('%H:%M')}: Ish vaqti!")
        current_time = datetime.datetime.now()
        while current_time.second != 0:
            current_time = datetime.datetime.now()
        total_work_time += work_time
        print(f"Ish vaqti tugadi! Dam olish vaqti!")
        current_time = datetime.datetime.now()
        while current_time.second != 0:
            current_time = datetime.datetime.now()
        total_break_time += break_time
        print(f"Dam olish vaqti tugadi! Ish vaqti!")
    print(f"Jami ish vaqti: {total_work_time} daqiqa")
    print(f"Jami dam olish vaqti: {total_break_time} daqiqa")

pomodoro_timer()
```

### 10. Mood Journal with Analysis
```python
import datetime

def mood_journal():
    mood = input("Kayfiyatni kiriting (1-5): ")
    while True:
        print(f"{datetime.datetime.now().strftime('%H:%M')}: Kayfiyatni kuzatamiz.")
        mood = input("Kayfiyatni kiriting (1-5): ")
        if mood == "1":
            print("Yomon kayfiyat!")
        elif mood == "2":
            print("O'rtacha kayfiyat!")
        elif mood == "3":
            print("Yaxshi kayfiyat!")
        elif mood == "4":
            print("Chok yaxshi kayfiyat!")
        elif mood == "5":
            print("Jahon yaxshi kayfiyat!")
        else:
            print("Xato kayfiyat!")
        continue

mood_journal()
```

### 11. Home Inventory Manager
```python
import datetime

def home_inventory_manager():
    item_name = input("Buyum nomini kiriting: ")
    item_price = float(input("Buyum narxini kiriting: "))
    item_date = datetime.datetime.now()
    print(f"Buyum nomi: {item_name}")
    print(f"Buyum narxi: {item_price}")
    print(f"Buyum sotib olingan sana: {item_date.strftime('%Y-%m-%d')}")

home_inventory_manager()
```

### 12. Wardrobe Organizer
```python
import datetime

def wardrobe_organizer():
    item_name = input("Kiyim nomini kiriting: ")
    item_color = input("Kiyim rangini kiriting: ")
    item_season = input("Kiyim mavsumini kiriting: ")
    print(f"Kiyim nomi: {item_name}")
    print(f"Kiyim rangi: {item_color}")
    print(f"Kiyim mavsumi: {item_season}")
    current_date = datetime.datetime.now()
    if current_date.month in [3, 4, 5]:
        print("Bugungi ob-havo bo'yicha kiyim taklif qiladi: ")
        print(f"Kiyim nomi: {item_name}")
        print(f"Kiyim rangi: {item_color}")
    elif current_date.month in [6, 7, 8]:
        print("Bugungi ob-havo bo'yicha kiyim taklif qiladi: ")
        print(f"Kiyim nomi: {item_name}")
        print(f"Kiyim rangi: {item_color}")
    elif current_date.month in [9, 10, 11]:
        print("Bugungi ob-havo bo'yicha kiyim taklif qiladi: ")
        print(f"Kiyim nomi: {item_name}")
        print(f"Kiyim rangi: {item_color}")
    else:
        print("Bugungi ob-havo bo'yicha kiyim taklif qiladi: ")
        print(f"Kiyim nomi: {item_name}")
        print(f"Kiyim rangi: {item_color}")

wardrobe_organizer()
```

### 13. Gift Suggestion Engine
```python
import datetime

def gift_suggestion_engine():
    budget = float(input("Byudjetni kiriting: "))
    person_name = input("Shaxs nomini kiriting: ")
    print(f"Oddiy sovg'a g'oyasi: ")
    print(f"Shaxs nomi: {person_name}")
    print(f"Byudjet: {budget}")
    current_date = datetime
