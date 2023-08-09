import os
import json
import csv
import pickle


# Определяем функцию, которая принимает на вход директорию
def dir_walk(dir):
    # Создаем пустой список для хранения результатов обхода
    results = []
    # Используем os.walk для рекурсивного обхода директории и всех вложенных директорий
    for root, dirs, files in os.walk(dir):
        # Для каждой директории добавляем словарь с ее именем, родительской директорией и типом
        results.append({"name": root, "parent": os.path.dirname(root), "type": "directory"})
        # Для каждого файла добавляем словарь с его именем, родительской директорией, типом и размером в байтах
        for file in files:
            results.append(
                {"name": file, "parent": root, "type": "file", "size": os.path.getsize(os.path.join(root, file))})
    # Вычисляем размер каждой директории как сумму размеров всех файлов в ней и всех вложенных директорий
    for result in results:
        if result["type"] == "directory":
            result["size"] = sum(r["size"] for r in results if r["parent"].startswith(result["name"]))
    # Сохраняем результаты в файлы json, csv и pickle
    with open("results.json", "w") as json_file:
        json.dump(results, json_file)
    with open("results.csv", "w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=["name", "parent", "type", "size"])
        writer.writeheader()
        writer.writerows(results)
    with open("results.pickle", "wb") as pickle_file:
        pickle.dump(results, pickle_file)
