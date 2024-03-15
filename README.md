# `natquiz` - a US naturalization test quiz app

`natquiz` is a tool designed to help you prepare for the US naturalization test. It provides a set of questions that mimic an actual test, allowing you to practice and improve your knowledge of US Civics.

## Features

- Comprehensive question bank: `natquiz` includes the full set of questions covering all sections of the US naturalization test.
- Randomized quizzes: Each quiz you take is randomly generated, ensuring that you get a unique set of questions every time.
- Full question bank: The full question bank can be viewed from the command line.

## Installation

To install the package, issue the command `pip install natquiz` (requires Python >= 3.11 which you can download from [python.org/downloads](https://www.python.org/downloads/)).

## Usage

Upon installation, use the `natquiz` command. On mac/linux computers you can use the `terminal` app; on Windows you can use `Powershell`, `Windows terminal` or any other terminal application you already use.

```shell
$ natquiz --help
usage: natquiz [-h] [-n N] [--show-all] [--clear-scr]

natquiz - a US naturalization quiz app

options:
  -h, --help   show this help message and exit
  -n N         Number of questions to ask (default: 10)
  --show-all   Show all questions and exit
  --clear-scr  Clear screen after answer is shown (default: False unless
               specified)
```

To get a regular, 10-question quiz simply issue the `natquiz` command.
```shell
$ natquiz

- US Naturalization Quiz -    

Number of questions to ask: 10

Question 1 of 10
Category: INTEGRATED CIVICS
What is the capital of the United States?
(Press enter to show answers)
```

As shown, press enter to show the answers to the question. Press enter again to display the next question.
```shell

- US Naturalization Quiz -    

Number of questions to ask: 10

Question 1 of 10
Category: INTEGRATED CIVICS
What is the capital of the United States?
(Press enter to show answers)
        Answer 1: Washington, D.C.

(Press enter for the next question)

Question 2 of 10
Category: Rights and Responsibilities
What are two ways that Americans can participate in their democracy?
(Press enter to show answers)
```

After the last question you get the option to do another quiz or exit.
```shell
Question 10 of 10
Category: Principles of American Democracy
How many amendments does the Constitution have?
(Press enter to show answers)
        Answer 1: twenty-seven (27)


This is the end of the quiz. Would you like to do another quiz? (Yes/No):
|
```

Enter `yes` or `y` to do another quiz or `no` or `n` to exit.

```shell
This is the end of the quiz. Would you like to do another quiz? (Yes/No):
n
Good luck on your interview!
```

If you would like a quiz with fewer than 10 questions, use the `-n` option with the number of questions you would like for the quiz. For example, you would get a two-question quiz with `natquiz -n 2` or `natquiz -n=2`.

To view all the questions issue `natquiz --show-all`. 

To clear the previous question and its answer(s) before displaying the next question, use the `--clear-scr switch`. For example,  `natquiz --clear-scr`.

## Contributing

Contributions are welcome via PRs!

## License

MIT license.
