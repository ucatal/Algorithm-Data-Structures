using NUnit.Framework;
using System.Linq;

namespace DataStructuresAlgorithm
{
    //# Consider an array of non-negative integers. A second array is formed by shuffling the elements of the first array and deleting a random element. Given these two arrays, find which element is missing in the second array.
    //# Here is an example input, the first array is shuffled and the number 5 is removed to construct the second array.
    //# Input:
    //# finder([1,2,3,4,5,6,7],[3,7,2,1,4,6])

    //# Output:
    //# 5 is the missing number
    public class FindMissingElementInArrays
    {
        [Test]
        public void TestCase1()
        {
            int[] array1 = new int[] { 1, 2, 3, 4, 5, 6, 7 };
            int[] array2 = new int[] { 3, 7, 2, 1, 4, 6 };

            int expectedResult = 5;
            var result = FinderMy(array1, array2);

            Assert.AreEqual(expectedResult, result);
        }
        public int Finder(int[] array1, int[] array2)
        { //XOR 
            //Linear
            int result = 0;
            foreach (var item in array1)
            {
                result = result ^ item;
            }
            foreach (var item in array2)
            {
                result = result ^ item;
            }
            return result;
        }
        public int FinderMy(int[] array1, int[] array2)
        {//O(N)
            var array1Sorted = array1.OrderBy(s => s).ToArray();
            var array2Sorted = array2.OrderBy(s => s).ToArray();
            int result = 0;
            for (int i = 0; i < array1.Length; i++)
            {
                if (array1Sorted[i] != array2Sorted[i])
                {
                    return array1Sorted[i];
                }
            }



            return result;
        }

    }

}
