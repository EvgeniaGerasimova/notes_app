import csv
import os
from datetime import datetime

NOTES_FILE = 'notes.csv'

def load_notes():
    if os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, 'r', newline='') as file:
            reader = csv.reader(file, delimiter=';')
            return list(reader)
    return []

def save_notes(notes):
    with open(NOTES_FILE, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerows(notes)

def create_note():
    title = input("Введите заголовок: ")
    body = input("Введите текст: ")
    note_id = len(load_notes()) + 1
    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    note = [note_id, title, body, created_at, created_at]
    notes = load_notes()
    notes.append(note)
    save_notes(notes)
    print("Заметка успешно создана")
    
def view_all_notes():
    notes = load_notes()
    if not notes:
        print("Заметки не найдены")
    else:
        note_id = input("Введите ID заметки для просмотра (или оставьте пустым для просмотра всех заметок): ")
        if note_id:
            for note in notes:
                if note[0] == note_id:
                    print(f"ID: {note[0]}; Заголовок: {note[1]}; Текст: {note[2]}; Дата создания: {note[3]}; Дата обновления: {note[4]}")
                    return
            print("Заметка не найдена")
        else:
            for note in notes:
                print(f"ID: {note[0]}; Заголовок: {note[1]}; Текст: {note[2]}; Дата создания: {note[3]}; Дата обновления: {note[4]}")
         
def edit_note():
    note_id = int(input("Введите ID заметки: "))
    notes = load_notes()
    for note in notes:
        if int(note[0]) == note_id:
            note[1] = input("Введите новый заголовок: ")
            note[2] = input("Введите новый текст: ")
            note[4] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_notes(notes)
            print("Заметка успешно обновлена")
            return
    print("Заметка не найдена")

def delete_note():
    note_id = int(input("Введите ID заметки для удаления: "))
    notes = load_notes()
    notes = [note for note in notes if int(note[0]) != note_id]
    save_notes(notes)
    print("Заметка успешно удалена")

def main():
    while True:
        print(" \n 1. Создание заметок \n 2. Просмотр заметок \n 3. Редактирование заметок \n 4. Удаление заметок \n 5. Выход ")

        opt = input("Выберите действие: ")

        if opt == '1':
            create_note()
        elif opt == '2':
            view_all_notes()
        elif opt == '3':
            edit_note()
        elif opt == '4':
            delete_note()
        elif opt == '5':
            break
        else:
            print("Ошибка, пожалуйста, попробуйте снова")

if __name__ == "__main__":
    main()

