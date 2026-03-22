import sys
import json
from pathlib import Path

DATA_FILE = Path("todos.json")


def load_todos():
    if not DATA_FILE.exists():
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_todos(todos):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(todos, f, ensure_ascii=False, indent=2)


def add_todo(text):
    todos = load_todos()
    new_id = (max([t["id"] for t in todos]) + 1) if todos else 1
    todos.append({"id": new_id, "text": text, "done": False})
    save_todos(todos)
    print(f"추가됨: [{new_id}] {text}")


def list_todos():
    todos = load_todos()
    if not todos:
        print("할 일이 없습니다...")
        return

    for t in todos:
        status = "완료" if t["done"] else "미완료"
        print(f"[{t['id']}] {t['text']} ({status})")


def done_todo(todo_id):
    todos = load_todos()
    found = False

    for t in todos:
        if t["id"] == todo_id:
            t["done"] = True
            found = True
            break

    if not found:
        print(f"{todo_id}번 할 일을 찾을 수 없습니다.")
        return

    save_todos(todos)
    print(f"{todo_id}번 할 일을 완료 처리했습니다.")


def main():
    if len(sys.argv) < 2:
        print("사용법: python todo.py [add/list/done] ...")
        return

    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) < 3:
            print("추가할 할 일을 입력하세요.")
            return
        text = " ".join(sys.argv[2:])
        add_todo(text)

    elif command == "list":
        list_todos()

    elif command == "done":
        if len(sys.argv) < 3:
            print("완료할 ID를 입력하세요.")
            return
        try:
            todo_id = int(sys.argv[2])
        except ValueError:
            print("ID는 숫자여야 합니다.")
            return
        done_todo(todo_id)

    else:
        print(f"알 수 없는 명령어: {command}")


if __name__ == "__main__":
    main()

