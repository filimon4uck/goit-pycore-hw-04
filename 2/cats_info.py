

def cats_info(path):
    try:
        with open(file=path, mode='r', encoding='utf-8') as file:
            return [{'id': line.strip().split(',')[0], 'name': line.strip().split(',')[1], 'age': line.strip().split(',')[2]} for line in file]
    except FileNotFoundError:
        return "File not found"
