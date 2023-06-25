import argparse
from task_manager import TaskManager
from datetime import datetime, timedelta
from rich.table import Table
from rich.console import Console
from rich.panel import Panel

def parse_args():
    parser = argparse.ArgumentParser(description='ShellSage: Your CLI Task Manager')
    parser.add_argument('--add', help='Add a task')
    parser.add_argument('--due_date', help='Due date for the task being added')
    parser.add_argument('--priority', type=int, choices=range(1,6), help='Priority for the task being added (1-5)')
    parser.add_argument('--category', help='Category for the task being added')
    parser.add_argument('--complete', help='Mark a task as complete')
    parser.add_argument('--show', action='store_true', help='Show all tasks')
    parser.add_argument('--detail', action='store_true', help='Show tasks in detail')
    parser.add_argument('--completed', action='store_true', help='Show only completed tasks')
    parser.add_argument('--uncompleted', action='store_true', help='Show only uncompleted tasks')
    parser.add_argument('--priority_order', action='store_true', help='Show tasks ordered by priority')
    return parser.parse_args()

def create_table():
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("ID")
    table.add_column("Name")
    table.add_column("Due Date")
    table.add_column("Priority")
    table.add_column("Category")
    table.add_column("Completed")
    return table

def add_task_to_table(table, task, style):
    table.add_row(
        str(task.id), 
        task.name, 
        task.due_date or '', 
        str(task.priority) if task.priority else '', 
        task.category or '', 
        str(task.completed),
        style=style)
    return table

def main():
    args = parse_args()
    task_manager = TaskManager()
    if args.add:
        task_manager.add_task(args.add, args.due_date, args.priority, args.category)
    elif args.complete:
        task_manager.complete_task(args.complete)
    elif args.show:
        tasks = task_manager.get_tasks()
        console = Console()

        if args.completed:
            tasks = [task for task in tasks if task.completed]
            tasks.sort(key=lambda x: x.priority if x.priority else 5)
        elif args.uncompleted:
            tasks = [task for task in tasks if not task.completed]
            tasks.sort(key=lambda x: x.priority if x.priority else 5)
        elif args.priority_order:
            tasks.sort(key=lambda x: (x.completed, x.priority if x.priority else 5))
        else:
            tasks.sort(key=lambda x: x.completed)

        if args.detail:
            for task in tasks:
                style = ""
                if task.priority == 1 and task.due_date and datetime.strptime(task.due_date, '%Y-%m-%d') <= datetime.today():
                    style = "bold red"
                elif task.priority and task.priority <= 3 and task.due_date and datetime.strptime(task.due_date, '%Y-%m-%d') <= datetime.today() + timedelta(days=2):
                    style = "bold yellow"

                table = create_table()
                table = add_task_to_table(table, task, style)
                console.print(Panel(table, title="Task Detail"))
        else:
            table = create_table()
            for task in tasks:
                style = ""
                if task.priority == 1 and task.due_date and datetime.strptime(task.due_date, '%Y-%m-%d') <= datetime.today():
                    style = "bold red"
                elif task.priority and task.priority <= 3 and task.due_date and datetime.strptime(task.due_date, '%Y-%m-%d') <= datetime.today() + timedelta(days=2):
                    style = "bold yellow"
                table = add_task_to_table(table, task, style)

            console.print(Panel(table, title="All Tasks"))

if __name__ == "__main__":
    main()
