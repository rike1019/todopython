import os
import json

class Todo:
    def __init__(self):
        self.fileName = "./data.json"
        self.map = {}

    def load(self):
        # ファイルが存在しないとFileNotFoundErrorが発生するのでチェック
        if not os.path.isfile(self.fileName):
            return
        with open(self.fileName, "r") as f:
            self.map = json.load(f)

    def print(self):
        print(self.map)

    def add(self, key):
        self.map[key] = False

    def complete(self, key):
        self.map[key] = True

    def remove(self, key):
        del self.map[key]

    def save(self):
        with open(self.fileName, "w") as f:
            json.dump(self.map, f)

def get_key():
    return input("名前を入力してください: ")

def main():
    todo = Todo()
    todo.load()
    while True:
        order = input("確認: 0 追加: 1 完了: 2 削除: 3 終了: 4\n")
        match order:
            case "0":
                todo.print()
            case "1":
                todo.add(get_key())
            case "2":
                todo.complete(get_key())
            case "3":
                todo.remove(get_key())
            case "4":
                todo.save()
                break
            case "_":
                pass

if __name__ == '__main__':
    main()
