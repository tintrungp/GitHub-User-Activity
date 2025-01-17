# Task Tracker CLI
## Overview
Task Tracker is a project used to track and manage your tasks. It is a simple command line interface (CLI) that tracks what you need to do, what you have done, and what you are currently working on. 

## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

1. Clone the repo
```sh
git clone https://github.com/tintrungp/TaskTracker-CLI.git
```

2. Run the program
```sh
python3 main.py 
```

## How to Use It
The Task Tracker has 5 main features that are available to the user:

* Add
* Update
* Delete
* Marking
* Listing

### Add
Add allows the user to add an item to their Task List. When prompted, the user will use the keyword `add` followed by a space and their item enclosed in quotation marks ("").

An example:
``` 
task-cli add "Test item 1"
task-cli add "Hello World"
```
### Update
Update allows the user to update an ***existing** item to their Task List. When prompted, the user will use the keyword `update` followed by a space and the `ID` of the existing item to be updated followed by another space and their updated item description in quotation marks ("").

An example:
``` 
task-cli update 1 "Test item 2"
```

### Delete 
Delete allows the user to delete an **existing** item from their Task List. When prompted, the user will use the keyword `delete` followed by a space and the `ID` of the existing item to be deleted.

An example:
``` 
task-cli delete 1 
```

### Mark 
Mark allows the user to change the status an **existing** item from their Task List. There are 2 options for marking tasks. 
(*Note: there are 3 statuses total, but all items are defaulted to 'todo'*)

* `mark-done`
    * Changes the task's status to **done**
* `mark-in-progress`
    * Changes the task's status to **in-progress**

When prompted, the user will use the keyword `mark-done` or `mark-in-progress` followed by a space and the `ID` of the existing item to be marked accordingly. 

An example:
``` 
task-cli mark-done 1
task-cli mark-in-progress 2 
```

### List 
List allows the user to display all items from their Task List. There are 4 options for displaying items.

* `list`
    * lists all items in the Task List regardless of status
* `list todo`
    * lists items in the Task List with **todo** status
* `list in-progress`
    * lists items in the Task List with **in-progress** status
* `list done`
    * lists items in the Task List with **done** status

When prompted, the user will use any of the 4 keywords options to and a list will be output accordingly. 

An example of `list`:
``` 
task-cli list
1 - This task is todo
2 - This task is in-progress
3 - This task is done
```

An example of `list todo`:
``` 
task-cli list todo
1 - This task is todo
```

An example of `list in-progress`:
``` 
task-cli list in-progress
2 - This task is in-progress
```

An example of `list done`:
``` 
task-cli list done
3 - This task is done
```

## Exiting
Finally, in order to exit the Task Tracker CLI, there are 2 options. When prompted use `q` or `quit` to exit. This is essential as quiting the application properly will allow the program to properly save all data that the user has modified.

## Data Saving
All data will be saved in JSON format under the name `tasks.json`. If this file cannot be found, the program will create a new, empty file. If you would like to change the name of this file you can edit `main.py` and change the variable `file_path` to be set equal to the string of your new file name.

# Conclusion
This is a small project. There are hopes for it to be extended into it's own window gui project with the use of the [Pysimplegui library](https://docs.pysimplegui.com/en/latest/). It's not much, but it's the start of something cool for me.

A future roadmap might look like the following...
- [ ] Add Changelog
- [ ] Add GUI interface
- [ ] Extend functionality


[Link to the project](https://roadmap.sh/projects/task-tracker)
[Link to the my solution entry](https://roadmap.sh/projects/task-tracker/solutions?u=677dc6bc70129741a81de8d9)