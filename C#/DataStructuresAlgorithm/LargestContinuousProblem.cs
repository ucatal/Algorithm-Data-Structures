using NUnit.Framework;
using System;
using System.Linq;

namespace DataStructuresAlgorithm
{
    public class LargestContinuousProblem
    {
        //# Largest Continuous Sum
        //# Kadane's algorithm[edit]

        //# Problem
        //# Given an array of integers (positive and negative) find the largest continuous sum.
        //# Solution
        //# Fill out your solution below:

        [Test]
        public void TestCase1()
        {
            int[] array = new int[] { 1, 2, -1, 3, 4, 10, 10, -10, -1 };

            int result = LargestContinuousSum(array);

            Assert.AreEqual(result, 29);
        }

        private int LargestContinuousSum(int[] array)
        {
            if (array.Length == 0) return 0;

            int currentSum = array[0], maxSum = array[0];

            foreach (var item in array.Skip(1))
            {
                currentSum = Math.Max(item + currentSum, item);
                maxSum = Math.Max(maxSum, currentSum);
            }

            return maxSum;
        }
    }
}