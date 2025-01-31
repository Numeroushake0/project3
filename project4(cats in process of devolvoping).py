def get_cats_info(path):
    cats = []
    try:
         with open(path, 'r', encoding='utf-8') as file:
              for line in file:
                   parts = line.strip().split(',')
                   if len(parts) == 3:
                    cat = {
                        "id": parts[0],
                        "name": parts[1],
                        "age": parts[2]
                    }
                    cats.append(cat)
    except FileNotFoundError:
       print(f"Файл за шляхом {path} не знайдено.")
    except IOError:
        print(f"Помилка при відкритті файлу {path}.")
    
    return cats                    

#r"C:\Users\Bogdan\Desktop\cats.txt"