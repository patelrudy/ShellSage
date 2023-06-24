import argparse
from task_manager import TaskManager

def main():
    task_manager = TaskManager()

    parser = argparse.ArgumentParser(description='ShellSage task manager CLI.')
    parser.add_argument('--add', metavar='TASK', type=str, nargs='+',
                        help='Add a new task')
    parser.add_argument('--complete', metavar='TASK', type=str, nargs='+',
                        help='Mark a task as completed')

    args = parser.parse_args()

    if args.add:
        task_manager.add_task(' '.join(args.add))
    elif args.complete:
        task_manager.complete_task(' '.join(args.complete))

if __name__ == '__main__':
    main()
