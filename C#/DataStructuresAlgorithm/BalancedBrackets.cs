using NUnit.Framework;
using System.Collections.Generic;

namespace DataStructuresAlgorithm
{
    /// <summary>
    /// https://www.hackerrank.com/challenges/balanced-brackets
    /// </summary>
    public class BalancedBrackets
    {
        [TestCase("(())", true)]
        [TestCase("(({[]}))", true)]
        [TestCase("(({{[[]}))", false)]
        public void TestCase(string data, bool expected)
        {
            var result = IsBalanced(data);

            Assert.AreEqual(result, expected);
        }

        private bool IsBalanced(string s)
        {
            Dictionary<char, char> closing = new Dictionary<char, char>()
            {
                {'(',')'},
                {'{','}'},
                {'[',']'}
            };
            if (s.Length == 0 || s.Length % 2 != 0)
                return false;

            Stack<char> openingStack = new Stack<char>();

            char[] letters = s.ToCharArray();
            foreach (char c in letters)
            {
                if (closing.ContainsKey(c))
                    openingStack.Push(c);
                else
                {
                    if (openingStack.Count == 0)
                        return false;

                    var currentOpen = openingStack.Pop();

                    if (closing[currentOpen] != c)
                        return false;
                }
            }

            return openingStack.Count == 0;
        }
    }
}