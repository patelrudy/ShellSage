# ShellSage: CLI Task Manager

ShellSage is a command-line interface (CLI) productivity app designed to help you manage your tasks efficiently. With ShellSage, you can add tasks, set due dates, assign priorities, categorize tasks, mark tasks as complete, and view your tasks in various ways.

## Installation

To use ShellSage, follow these steps:

1. Clone the repository: `git clone https://github.com/your-username/shellsage.git`
2. Navigate to the project directory: `cd shellsage`
3. Install the required dependencies: `pip install -r requirements.txt`

## Usage

ShellSage provides several command-line options to perform different tasks. Here are the available options:

--add              Add a task
--due_date         Due date for the task being added
--priority         Priority for the task being added (1-5)
--category         Category for the task being added
--complete         Mark a task as complete
--show             Show all tasks
--detail           Show tasks in detail
--completed        Show only completed tasks
--uncompleted      Show only uncompleted tasks
--priority_order   Show tasks ordered by priority

### Examples
1.  Add a task:
        - python shellsage.py --add "Finish project" --due_date "2023-07-15" --priority 3 --category "Work"
2.  Mark a task as complete:
        - python shellsage.py --complete "Finish project"
3.  Show all tasks:
        - python shellsage.py --show
4.  Show tasks in detail
        - python shellsage.py --show --detail
5.  Show only completed tasks
        - python shellsage.py --show --completed
6.  Show only uncompleted tasks
        - python shellsage.py --show --uncompleted
7.  Show task order by priority
        - python shellsage.py --show --priority_order

## Database

ShellSage uses an SQLite database (`tasks.db`) to store tasks. The `TaskManager` class handles the database operations. The database schema consists of the following columns:

- `id` (INTEGER): Unique identifier for each task.
- `name` (TEXT): Name of the task.
- `due_date` (TEXT): Due date of the task (optional).
- `priority` (INTEGER): Priority of the task (1-5, optional).
- `category` (TEXT): Category of the task (optional).
- `completed` (INTEGER): Indicates whether the task is completed (0 for incomplete, 1 for complete).


