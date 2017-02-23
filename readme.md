# Hunter's Interview Problem Purgatory

Over time I've encountered some very fun software engineering interview questions! I've written (what I perceive to be) thorough solutions here for the enjoyment of others. Please submit pull requests if you believe you can improve any of the solutions!

---

## Python Linter

In the interest of code quality, I've been using Google's python linter which maintains their open-sourced [Python Style Guide](http://google.github.io/styleguide/pyguide.html).

**Installation**

`pip install pylint`

If you haven't installed `pip`, please install it via the instructions at [pip.pypa.io/en/stable/installing](http://pip.pypa.io/en/stable/installing).

**Example Usage**

`pylint --rcfile=pylint_config.rc [myfile1 myfile2 ...]`

When you are `cd`'d into the root of this repository, you can use the following command to lint all python files in this repository.

`pylint --rcfile=pylint_config.rc --reports=n $(find python/ -name *.py)`

Curious what this does? BASH is fun! Find out at [explainshell.com](http://goo.gl/Cu26YB).
