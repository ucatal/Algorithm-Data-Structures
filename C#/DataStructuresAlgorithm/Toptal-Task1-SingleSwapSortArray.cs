using NUnit.Framework;

namespace DataStructuresAlgorithm
{
    /// <summary>
    /// Toptal Task-1-1.png Task-1-2.pnt
    /// </summary>
    [TestFixture]
    public class SingleSwapSortArray
    {
        [TestCase(new int[] { 1, 5, 3, 3, 7 }, true)]

        public void TestCase1(int[] input, bool expextedResult)
        {
            bool result = false;
            int leftIndex = FindLeftIndex(input);
            int rightIndex = FindRightIndex(input);
            if (leftIndex == rightIndex || leftIndex == -1 || rightIndex == -1)
                result = false;

            Swap(input, leftIndex, rightIndex);

            result = IsArraySorted(input);

            Assert.AreEqual(result, expextedResult);
        }

        public void Swap(int[] input, int leftIndex, int rightIndex)
        {
            int numberLeft = input[leftIndex];
            int numberRight = input[rightIndex];
            input[rightIndex] = numberLeft;
            input[leftIndex] = numberRight;
        }

        public bool IsArraySorted(int[] input)
        {
            for (int i = 0; i < input.Length - 1; i++)
            {
                if (input[i] > input[i + 1])
                {
                    return false;
                }
            }
            return true;
        }

        private int FindRightIndex(int[] input)
        {
            for (int i = input.Length - 1; i >= 1; i--)
            {
                if (input[i - 1] > input[i])
                {
                    while (i < input.Length - 1 && input[i] == input[i + 1])
                    {
                        i++;
                    }
                    return i;
                }
            }
            return -1;
        }

        private int FindLeftIndex(int[] input)
        {
            for (int i = 0; i < (input.Length - 1); i++)
            {
                if (input[i] > input[i + 1])
                {
                    while (i > 0 && input[i] == input[i - 1])
                    {
                        i--;
                    }
                    return i;
                }
            }
            return -1;
        }
    }
}