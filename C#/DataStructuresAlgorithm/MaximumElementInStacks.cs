using NUnit.Framework;
using System.Collections.Generic;

namespace DataStructuresAlgorithm
{
    // https://www.hackerrank.com/challenges/maximum-element
    internal class MaximumElementInStacks
    {
        [Test]
        public void TestCase()
        {
            List<string> inputDatas = new List<string>();
            inputDatas.Add("1 97");
            inputDatas.Add("2");
            inputDatas.Add("1 20");
            inputDatas.Add("2");
            inputDatas.Add("1 26");
            inputDatas.Add("1 20");
            inputDatas.Add("2");
            inputDatas.Add("3");
            inputDatas.Add("1 91");
            inputDatas.Add("3");

            List<int> expectedResult = new List<int>() { 26, 91 };
            var result = FindMaximumElement(inputDatas);

            Assert.AreEqual(result, expectedResult);
        }

        private List<int> FindMaximumElement(List<string> inputDatas)
        {
            List<int> results = new List<int>();
            Stack<int> stack = new Stack<int>();
            Stack<int> maxStack = new Stack<int>();
            for (int i = 0; i < inputDatas.Count; i++)
            {
                string data = inputDatas[i];
                var splitted = data.Split(' ');
                string commandType = splitted[0];
                if (commandType == "1")
                {
                    var val = int.Parse(splitted[1]);
                    stack.Push(val);
                    if (maxStack.Count == 0 || val >= maxStack.Peek())
                        maxStack.Push(val);
                }
                else if (commandType == "2")
                {
                    var popped = stack.Pop();
                    if (popped == maxStack.Peek())
                        maxStack.Pop();
                }
                else
                {
                    results.Add(maxStack.Peek());
                }
            }
            return results;
        }
    }
}