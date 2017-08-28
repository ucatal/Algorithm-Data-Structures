using NUnit.Framework;
using System.Collections.Generic;
using System.Linq;

namespace DataStructuresAlgorithm
{
    /// <summary>
    /// Queue using Two Stacks
    ///1 x: Enqueue element  into the end of the queue.
    //2: Dequeue the element at the front of the queue.
    //3: Print the element at the front of the queue.
    /// </summary>

    public class HackerRankQueueWithTwoStack
    {
        //https://www.hackerrank.com/challenges/queue-using-two-stacks
        [Test]
        public void TestCase()
        {
            List<string> input = new List<string> { "1 42", "2", "1 14", "3", "1 28", "3", "1 60", "1 78", "2", "2" };
            List<int> expecetedResult = new List<int> { 14, 14 };

            var result = Result(input);

            Assert.NotNull(result);

            bool isEqual = result.SequenceEqual(expecetedResult);

            Assert.That(isEqual);
        }

        private List<int> Result(IReadOnlyList<string> inputs)
        {
            List<int> result = new List<int>();
            Stack<int> innerStack = new Stack<int>();
            Stack<int> outerStack = new Stack<int>();

            for (int i = 0; i < inputs.Count; i++)
            {
                string data = inputs[i];

                var splitted = data.Split(' ');
                string commandType = splitted[0];
                if (commandType == "1")
                {
                    var val = int.Parse(splitted[1]);

                    innerStack.Push(val);
                }
                else
                {
                    FillQueue(innerStack, outerStack);

                    if (outerStack.Count > 0)
                    {
                        if (commandType == "2")
                        {
                            outerStack.Pop();
                        }
                        else
                        {
                            result.Add(outerStack.Peek());
                        }
                    }
                }

            }
            return result;
        }

        private void FillQueue(Stack<int> innerStack, Stack<int> outerStack)
        {
            if (outerStack.Count == 0)
            {
                while (innerStack.Count > 0)
                {
                    outerStack.Push(innerStack.Pop());
                }
            }
        }
    }
}