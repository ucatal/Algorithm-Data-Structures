# Balanced Parentheses Check
# Problem Statement
# Given a string of opening and closing parentheses, check whether it’s balanced. We have 3 types of parentheses: round brackets: (), square brackets: [], and curly brackets: {}. Assume that the string doesn’t contain any other character than these, no spaces words or numbers. As a reminder, balanced parentheses require every opening parenthesis to be closed in the reverse order opened. For example ‘([])’ is balanced but ‘([)]’ is not.
# You can assume the input string has no spaces.
# https://github.com/jmportilla/Python-for-Algorithms--Data-Structures--and-Interviews/blob/master/Stacks%2C%20Queues%20and%20Deques/Stacks%2C%20Queues%2C%20and%20Deques%20Interview%20Problems/Stacks%2C%20Queues%2C%20Deques%20Interview%20Questions%20/Balanced%20Parentheses%20Check%20.ipynb


def balance_check(s):

    if len(s) % 2 != 0:
        return False

    balances = {"(": ")", "[": "]", "": "}"}

    opening = set('([{')
    matches = set([("(", ")"), ("[", "]"), ("{", "}")])

    stack = []

    for paren in s:
        if paren in opening:
            stack.append(paren)
        else:
            if len(stack) == 0:
                return False
            last_open = stack.pop()

            if (last_open, paren) not in matches:
                return False

    isBalanced = (len(stack) == 0)

    print(isBalanced)

    return isBalanced

    pass


# balance_check('[]')
# # True

# balance_check('[](){([[[]]])}')
# # True

balance_check('()(){]}')
# False

"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""
from nose.tools import assert_equal


class TestBalanceCheck(object):

    def test(self, sol):
        assert_equal(sol('[](){([[[]]])}('), False)
        assert_equal(sol('[{{{(())}}}]((()))'), True)
        assert_equal(sol('[[[]])]'), False)
        print('ALL TEST CASES PASSED')

# Run Tests


t = TestBalanceCheck()
t.test(balance_check)
